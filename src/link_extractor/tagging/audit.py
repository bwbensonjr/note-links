"""Tag vocabulary audit — analyzes corpus and suggests TAGS.md changes."""

import json
import logging
import re
from pathlib import Path
from typing import Any

import boto3

from ..storage.database import Database
from .llm_tagger import AVAILABLE_TAGS

logger = logging.getLogger(__name__)

# Section headers in TAGS.md mapped to category keys
CATEGORY_HEADERS = {
    "Programming Language": "programming_language",
    "Technical Topic": "technical_topic",
    "Culture": "culture",
}


def _build_audit_stats(db: Database) -> dict[str, Any]:
    """Gather all statistics needed for the audit."""
    stats = db.get_stats()
    tag_dist = db.get_tag_distribution()
    rejected = db.get_rejected_tag_counts(min_count=2)
    untagged_count = db.get_untagged_link_count()

    # Find unused tags (in vocabulary but never applied)
    used_tag_names = {name for name, _, count in tag_dist if count > 0}
    all_vocab_tags = set()
    for tags in AVAILABLE_TAGS.values():
        all_vocab_tags.update(tags)
    unused_tags = all_vocab_tags - used_tag_names

    # Find low-use tags (applied to fewer than 2 links)
    low_use = [(name, cat, count) for name, cat, count in tag_dist if 0 < count <= 2]

    return {
        "total_links": stats["total_links"],
        "tagged_count": stats["tagged"],
        "untagged_count": untagged_count,
        "tag_distribution": tag_dist,
        "rejected_tags": rejected,
        "unused_tags": unused_tags,
        "low_use_tags": low_use,
    }


def _ask_llm_for_suggestions(
    audit_stats: dict[str, Any],
    model_id: str,
    region: str,
) -> dict[str, Any]:
    """Ask the LLM to review the tag vocabulary and suggest changes."""
    # Build a summary of the current state
    current_tags = ""
    for category, tags in AVAILABLE_TAGS.items():
        current_tags += f"\n{category}: {', '.join(tags)}"

    rejected_summary = ""
    if audit_stats["rejected_tags"]:
        lines = [
            f"  {name} (category: {cat or 'unknown'}, suggested {count} times)"
            for name, cat, count in audit_stats["rejected_tags"][:30]
        ]
        rejected_summary = "\n".join(lines)
    else:
        rejected_summary = "  (none recorded)"

    unused_summary = ", ".join(sorted(audit_stats["unused_tags"])) or "(none)"

    low_use_summary = ""
    if audit_stats["low_use_tags"]:
        lines = [f"  {name} ({count} links)" for name, _, count in audit_stats["low_use_tags"]]
        low_use_summary = "\n".join(lines)
    else:
        low_use_summary = "  (none)"

    prompt = f"""You are reviewing a tag vocabulary used to categorize web links saved from daily notes.

CURRENT TAG VOCABULARY:{current_tags}

CORPUS STATISTICS:
- Total links: {audit_stats["total_links"]}
- Tagged: {audit_stats["tagged_count"]}
- Untagged (no tags assigned): {audit_stats["untagged_count"]}

TAGS THE LLM TRIED TO USE BUT WERE REJECTED (not in vocabulary):
{rejected_summary}

UNUSED TAGS (in vocabulary but never applied):
{unused_summary}

LOW-USE TAGS (applied to 2 or fewer links):
{low_use_summary}

INSTRUCTIONS:
Analyze this data and suggest vocabulary changes. Be conservative — only suggest changes with strong evidence. The goal is a compact, useful vocabulary (roughly 40-60 tags total), not exhaustive coverage.

Consider:
1. Frequently rejected tags that should be added (suggested 3+ times)
2. Unused or very low-use tags that could be removed or merged
3. Whether any new categories are needed
4. Whether any existing tags are too broad and should be split

Return ONLY valid JSON in this format:
{{
  "additions": [
    {{"name": "tag-name", "category": "category_name", "description": "Short description", "reason": "Why this should be added"}}
  ],
  "removals": [
    {{"name": "tag-name", "category": "category_name", "reason": "Why this could be removed"}}
  ],
  "new_categories": [
    {{"name": "category_name", "description": "What this category covers", "initial_tags": ["tag1", "tag2"]}}
  ],
  "summary": "Brief overall assessment of vocabulary health"
}}

JSON response:"""

    client = boto3.client("bedrock-runtime", region_name=region)
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1500,
        "messages": [{"role": "user", "content": prompt}],
    })

    response = client.invoke_model(
        modelId=model_id,
        body=body,
        contentType="application/json",
        accept="application/json",
    )

    response_body = json.loads(response["body"].read())
    text = response_body["content"][0]["text"].strip()

    # Handle markdown code blocks
    if text.startswith("```"):
        lines = text.split("\n")
        end = len(lines) - 1
        for i in range(1, len(lines)):
            if lines[i].strip() == "```":
                end = i
                break
        text = "\n".join(lines[1:end])

    return json.loads(text)


def update_tags_md(
    tags_md_path: Path,
    suggestions: dict[str, Any],
) -> str:
    """Update TAGS.md with suggested changes. Returns the new content."""
    content = tags_md_path.read_text()

    # Remove any existing suggested sections
    content = _strip_suggested_sections(content)

    # Build suggestion blocks per category
    additions_by_cat: dict[str, list[dict]] = {}
    for addition in suggestions.get("additions", []):
        cat = addition["category"]
        additions_by_cat.setdefault(cat, []).append(addition)

    removals_by_cat: dict[str, list[dict]] = {}
    for removal in suggestions.get("removals", []):
        cat = removal["category"]
        removals_by_cat.setdefault(cat, []).append(removal)

    # Reverse mapping: category_key -> header
    key_to_header = {v: k for k, v in CATEGORY_HEADERS.items()}

    # Insert suggestions after each category's tag list
    for cat_key, header in key_to_header.items():
        suggestion_block = ""

        if cat_key in additions_by_cat:
            suggestion_block += "\n### Suggested Additions\n\n"
            for add in additions_by_cat[cat_key]:
                suggestion_block += (
                    f"- `{add['name']}` - {add['description']} "
                    f"({add['reason']})\n"
                )

        if cat_key in removals_by_cat:
            suggestion_block += "\n### Suggested Removals\n\n"
            for rem in removals_by_cat[cat_key]:
                suggestion_block += (
                    f"- `{rem['name']}` - {rem['reason']}\n"
                )

        if suggestion_block:
            # Find the end of this category's tag list
            content = _insert_after_category(content, header, suggestion_block)

    # Add new categories at the end if suggested
    for new_cat in suggestions.get("new_categories", []):
        cat_block = f"\n## {new_cat['name']}\n\n"
        cat_block += f"{new_cat['description']}\n\n"
        cat_block += "### Suggested Additions\n\n"
        for tag in new_cat.get("initial_tags", []):
            cat_block += f"- `{tag}` - (new category suggestion)\n"
        content = content.rstrip() + "\n" + cat_block

    # Add audit summary at the bottom
    summary = suggestions.get("summary", "")
    if summary:
        # Remove any existing audit summary
        content = re.sub(
            r"\n---\n\n_Audit summary.*?$",
            "",
            content,
            flags=re.DOTALL,
        )
        content = content.rstrip() + f"\n\n---\n\n_Audit summary: {summary}_\n"

    return content


def _strip_suggested_sections(content: str) -> str:
    """Remove all ### Suggested ... sections and audit summary from TAGS.md."""
    lines = content.split("\n")
    result = []
    skipping = False

    for line in lines:
        if line.startswith("### Suggested"):
            skipping = True
            # Also remove the blank line before the suggested section
            while result and result[-1].strip() == "":
                result.pop()
            continue

        if skipping:
            # Stop skipping when we hit a new ## header or another ### that isn't Suggested
            if line.startswith("## ") or (line.startswith("### ") and not line.startswith("### Suggested")):
                skipping = False
            else:
                continue

        result.append(line)

    # Remove audit summary
    text = "\n".join(result)
    text = re.sub(
        r"\n---\n\n_Audit summary.*?$",
        "",
        text,
        flags=re.DOTALL,
    )

    return text.rstrip() + "\n"


def _insert_after_category(content: str, header: str, block: str) -> str:
    """Insert a block of text after the last tag line in a category section."""
    lines = content.split("\n")
    result = []
    found_header = False
    last_tag_idx = -1

    for i, line in enumerate(lines):
        if line.strip() == f"## {header}":
            found_header = True
            last_tag_idx = -1

        if found_header and re.match(r"^- `[^`]+`", line):
            last_tag_idx = i

        # When we hit the next ## header after our target, insert before it
        if found_header and last_tag_idx >= 0 and line.startswith("## ") and line.strip() != f"## {header}":
            # Insert the block after last_tag_idx
            result_with_insert = result[:last_tag_idx + 1]
            result_with_insert.append(block)
            result_with_insert.extend(result[last_tag_idx + 1:])
            result_with_insert.append(line)
            # Process remaining lines normally
            for remaining in lines[i + 1:]:
                result_with_insert.append(remaining)
            return "\n".join(result_with_insert)

        result.append(line)

    # If this was the last category (no next ## found), append at end
    if found_header and last_tag_idx >= 0:
        result_with_insert = result[:last_tag_idx + 1]
        result_with_insert.append(block)
        result_with_insert.extend(result[last_tag_idx + 1:])
        return "\n".join(result_with_insert)

    return content


def run_audit(
    db: Database,
    tags_md_path: Path,
    model_id: str,
    region: str,
    skip_llm: bool = False,
) -> dict[str, Any]:
    """Run the full tag audit. Returns the audit stats and suggestions."""
    stats = _build_audit_stats(db)

    if skip_llm:
        suggestions = {"additions": [], "removals": [], "new_categories": [], "summary": ""}
    else:
        logger.info("Asking LLM to review tag vocabulary...")
        suggestions = _ask_llm_for_suggestions(stats, model_id, region)

    # Update TAGS.md
    new_content = update_tags_md(tags_md_path, suggestions)
    tags_md_path.write_text(new_content)

    return {"stats": stats, "suggestions": suggestions}
