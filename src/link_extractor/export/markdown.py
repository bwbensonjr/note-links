"""Cache a Markdown version of each article under category directories in docs/.

Each link is written to ``docs/<category>/<slug>-<id>.md`` where the category
comes from the link's highest-confidence tag. Files carry YAML front matter with
the link metadata followed by the article body (a true HTML->Markdown render
captured at fetch time, falling back to the stored plain text for legacy links).
"""

import re
from pathlib import Path
from typing import Optional

import yaml

from ..storage.models import LinkRecord

_SLUG_STRIP = re.compile(r"[^a-z0-9]+")


def slugify(text: str, max_length: int = 60) -> str:
    """Lowercase, collapse non-alphanumeric runs to hyphens, and truncate.

    Returns "" when nothing usable remains.
    """
    slug = _SLUG_STRIP.sub("-", (text or "").lower()).strip("-")
    if len(slug) > max_length:
        slug = slug[:max_length].rsplit("-", 1)[0].strip("-") or slug[:max_length]
    return slug


def category_dir_for(tags: list[tuple[str, str, float]]) -> str:
    """Pick the highest-confidence tag's category as a slugified directory name.

    ``tags`` is db.get_tags_for_link() output (name, category, confidence),
    already confidence-DESC ordered. Returns "uncategorized" when empty.
    """
    if not tags:
        return "uncategorized"
    return slugify(tags[0][1]) or "uncategorized"


def markdown_filename(link: LinkRecord) -> str:
    """Filename "<slug>-<id>.md"; slug is cosmetic, the id ensures uniqueness."""
    base = slugify(link.page_title or link.title or link.description or "") or "article"
    return f"{base}-{link.id}.md"


def relative_markdown_path(tags: list[tuple[str, str, float]], link: LinkRecord) -> str:
    """Repo-relative POSIX path stored in markdown_path, e.g.
    'docs/programming-language/rust-ownership-42.md'."""
    return f"docs/{category_dir_for(tags)}/{markdown_filename(link)}"


def _heading(link: LinkRecord) -> str:
    return link.page_title or link.title or link.description or link.url


def build_front_matter(link: LinkRecord, tag_names: list[str]) -> str:
    """Return a YAML front-matter block delimited by '---' lines."""
    data = {
        "id": link.id,
        "url": link.url,
        "title": _heading(link),
        "domain": link.domain,
        "source_date": link.source_date.isoformat() if link.source_date else None,
        "tags": tag_names,
        "summary": link.summary,
        "fetch_status": link.fetch_status.value if link.fetch_status else None,
        "fetched_at": link.fetched_at.isoformat() if link.fetched_at else None,
        "summarizer_model": link.summarizer_model,
        "summarized_at": link.summarized_at.isoformat() if link.summarized_at else None,
    }
    clean = {k: v for k, v in data.items() if v is not None}
    body = yaml.safe_dump(clean, sort_keys=False, allow_unicode=True).strip()
    return f"---\n{body}\n---\n"


def render_markdown_file(link: LinkRecord, tag_names: list[str], body: str) -> str:
    """Full file content: front matter + H1 heading + body."""
    front = build_front_matter(link, tag_names)
    return f"{front}\n# {_heading(link)}\n\n{(body or '').strip()}\n"


def write_markdown_for_link(db, link: LinkRecord, repo_root: Path) -> Optional[str]:
    """Render and write the cached markdown file for a link.

    Handles stale files: if the link already has a recorded markdown_path that
    differs from the newly computed path (category or slug changed), the old
    file is deleted before the new one is written. Returns the new
    repo-relative path, or None if the link has no id.
    """
    if link.id is None:
        return None

    tags = db.get_tags_for_link(link.id)
    tag_names = [name for name, _cat, _conf in tags]
    body = link.markdown_content or link.page_content or ""

    new_rel = relative_markdown_path(tags, link)

    # Stale handling: remove the previous file if it moved (move-by-rewrite).
    if link.markdown_path and link.markdown_path != new_rel:
        old_abs = repo_root / link.markdown_path
        try:
            old_abs.unlink(missing_ok=True)
            # Drop the old category dir if it is now empty.
            old_abs.parent.rmdir()
        except OSError:
            pass

    out = repo_root / new_rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_markdown_file(link, tag_names, body), encoding="utf-8")

    db.set_markdown_path(link.id, new_rel)
    return new_rel
