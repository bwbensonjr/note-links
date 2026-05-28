"""Runtime tag vocabulary loaded from TAGS.md (single source of truth)."""

import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Category:
    header: str
    key: str
    tags: list[str]


_TAG_LINE = re.compile(r"^- `([^`]+)` - .+$")
_cache: dict[Path, list[Category]] = {}


def _default_path() -> Path:
    return Path(__file__).resolve().parents[3] / "TAGS.md"


def _header_to_key(header: str) -> str:
    return header.strip().lower().replace(" ", "_").replace("-", "_")


def load_vocabulary(path: Path | None = None) -> list[Category]:
    """Parse TAGS.md into a list of Category. Cached per path."""
    path = (path or _default_path()).resolve()
    if path in _cache:
        return _cache[path]

    categories: list[Category] = []
    current_header: str | None = None
    current_tags: list[str] = []
    in_suggested = False

    def flush() -> None:
        if current_header is not None:
            categories.append(
                Category(
                    header=current_header,
                    key=_header_to_key(current_header),
                    tags=list(current_tags),
                )
            )

    for line in path.read_text().splitlines():
        if line.startswith("## "):
            flush()
            current_header = line[3:].strip()
            current_tags = []
            in_suggested = False
            continue

        if line.startswith("### Suggested"):
            in_suggested = True
            continue

        if line.startswith("### "):
            in_suggested = False
            continue

        if current_header is None or in_suggested:
            continue

        match = _TAG_LINE.match(line)
        if match:
            current_tags.append(match.group(1))

    flush()
    _cache[path] = categories
    return categories


def available_tags(path: Path | None = None) -> dict[str, list[str]]:
    """Return {category_key: [tag, ...]} for runtime vocabulary lookups."""
    return {c.key: list(c.tags) for c in load_vocabulary(path)}


def reload_vocabulary(path: Path | None = None) -> list[Category]:
    """Drop the cache and re-parse. Useful for long-running processes."""
    target = (path or _default_path()).resolve()
    _cache.pop(target, None)
    return load_vocabulary(target)
