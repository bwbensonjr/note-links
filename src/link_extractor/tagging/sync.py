"""Sync TAGS.md to AVAILABLE_TAGS in llm_tagger.py."""

import re
from pathlib import Path

from .audit import CATEGORY_HEADERS


def parse_tags_md(tags_md_path: Path) -> dict[str, list[tuple[str, str]]]:
    """Parse accepted tags from TAGS.md (ignoring suggested sections).

    Returns {category_key: [(tag_name, description), ...]}.
    """
    content = tags_md_path.read_text()
    result: dict[str, list[tuple[str, str]]] = {}
    current_category = None
    in_suggested = False

    for line in content.split("\n"):
        if line.startswith("## "):
            header = line[3:].strip()
            if header in CATEGORY_HEADERS:
                current_category = CATEGORY_HEADERS[header]
                result.setdefault(current_category, [])
                in_suggested = False

        if line.startswith("### Suggested"):
            in_suggested = True
            continue

        if line.startswith("## "):
            in_suggested = False

        if current_category and not in_suggested:
            match = re.match(r"^- `([^`]+)` - (.+)$", line)
            if match:
                result[current_category].append((match.group(1), match.group(2)))

    return result


def _build_available_tags_source(tags: dict[str, list[tuple[str, str]]]) -> str:
    """Generate the Python source for AVAILABLE_TAGS dict."""
    lines = ["AVAILABLE_TAGS: dict[str, list[str]] = {"]

    for category, tag_list in tags.items():
        lines.append(f"    \"{category}\": [")
        for name, _ in tag_list:
            lines.append(f"        \"{name}\",")
        lines.append("    ],")

    lines.append("}")
    return "\n".join(lines)


def _build_category_map_source(tags: dict[str, list[tuple[str, str]]]) -> str:
    """Generate the Python source for CATEGORY_MAP dict."""
    lines = ["CATEGORY_MAP = {"]
    for category in tags:
        enum_name = category.upper()
        lines.append(f"    \"{category}\": TagCategory.{enum_name},")
    lines.append("}")
    return "\n".join(lines)


def sync_tags_to_code(tags_md_path: Path, llm_tagger_path: Path) -> dict[str, int]:
    """Read TAGS.md and rewrite AVAILABLE_TAGS and CATEGORY_MAP in llm_tagger.py.

    Returns {"categories": N, "tags": N} with the new counts.
    """
    tags = parse_tags_md(tags_md_path)
    code = llm_tagger_path.read_text()

    # Replace AVAILABLE_TAGS block
    new_available = _build_available_tags_source(tags)
    code = re.sub(
        r"AVAILABLE_TAGS: dict\[str, list\[str\]\] = \{.*?\}",
        new_available,
        code,
        flags=re.DOTALL,
    )

    # Replace CATEGORY_MAP block
    new_category_map = _build_category_map_source(tags)
    code = re.sub(
        r"CATEGORY_MAP = \{.*?\}",
        new_category_map,
        code,
        flags=re.DOTALL,
    )

    llm_tagger_path.write_text(code)

    total_tags = sum(len(tag_list) for tag_list in tags.values())
    return {"categories": len(tags), "tags": total_tags}


def sync_tags_md_enum(tags_md_path: Path, models_path: Path) -> None:
    """Ensure TagCategory enum in models.py matches TAGS.md categories."""
    tags = parse_tags_md(tags_md_path)
    code = models_path.read_text()

    # Build new enum body
    enum_lines = []
    for category in tags:
        enum_name = category.upper()
        enum_lines.append(f"    {enum_name} = \"{category}\"")

    new_enum_body = "\n".join(enum_lines)

    # Replace the enum body
    code = re.sub(
        r"(class TagCategory\(Enum\):\n)(.*?)(\n\n)",
        rf"\g<1>{new_enum_body}\n\n",
        code,
        flags=re.DOTALL,
    )

    models_path.write_text(code)
