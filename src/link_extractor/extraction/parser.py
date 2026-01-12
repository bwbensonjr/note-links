"""Parse links from Obsidian daily note markdown files."""

import re
from datetime import date
from pathlib import Path

from ..storage.models import ExtractedLink


class MarkdownLinkParser:
    """Parse links from the ## Links section of daily notes."""

    # Regex patterns
    MARKDOWN_LINK = re.compile(r"\[([^\]]+)\]\((https?://[^\)]+)\)")
    BARE_URL = re.compile(r"(https?://[^\s\)]+)")
    LINKS_SECTION = re.compile(r"^## Links\s*$", re.MULTILINE)
    NEXT_SECTION = re.compile(r"^## ", re.MULTILINE)
    LIST_ITEM = re.compile(r"^(\s*)-\s+(.+)$")

    def parse_file(self, file_path: Path) -> list[ExtractedLink]:
        """Parse all links from a daily note file."""
        content = file_path.read_text(encoding="utf-8")
        source_date = self._extract_date_from_path(file_path)

        links_section = self._extract_links_section(content)
        if not links_section:
            return []

        return self._parse_links_section(links_section, source_date, str(file_path))

    def _extract_date_from_path(self, path: Path) -> date:
        """Extract date from path like .../2025/03/2025-03-15.md"""
        stem = path.stem  # "2025-03-15"
        parts = stem.split("-")
        return date(int(parts[0]), int(parts[1]), int(parts[2]))

    def _extract_links_section(self, content: str) -> str | None:
        """Extract the ## Links section content."""
        match = self.LINKS_SECTION.search(content)
        if not match:
            return None

        start = match.end()
        next_section = self.NEXT_SECTION.search(content, start)
        end = next_section.start() if next_section else len(content)

        return content[start:end].strip()

    def _parse_links_section(
        self, section: str, source_date: date, source_file: str
    ) -> list[ExtractedLink]:
        """Parse individual link items from the section."""
        links = []
        parent_stack: list[tuple[int, str]] = []

        for line in section.split("\n"):
            list_match = self.LIST_ITEM.match(line)
            if not list_match:
                continue

            indent_str = list_match.group(1)
            # Handle tabs (count as 1 level) and spaces (4 spaces = 1 level)
            indent_level = indent_str.count("\t") + len(
                indent_str.replace("\t", "")
            ) // 4
            content = list_match.group(2).strip()

            # Update parent stack
            while parent_stack and parent_stack[-1][0] >= indent_level:
                parent_stack.pop()

            parent_url = parent_stack[-1][1] if parent_stack else None

            # Try to extract link
            link = self._parse_link_content(
                content, source_date, source_file, indent_level, parent_url
            )

            if link:
                links.append(link)
                parent_stack.append((indent_level, link.url))

        return links

    def _parse_link_content(
        self,
        content: str,
        source_date: date,
        source_file: str,
        indent_level: int,
        parent_url: str | None,
    ) -> ExtractedLink | None:
        """Parse a single line to extract link and description."""
        # Try markdown link format: [Title](url)
        md_match = self.MARKDOWN_LINK.search(content)
        if md_match:
            title = md_match.group(1)
            url = md_match.group(2)
            # Description is everything except the markdown link
            description = self.MARKDOWN_LINK.sub("", content).strip(" -")
            return ExtractedLink(
                url=url,
                title=title,
                description=description if description else None,
                source_date=source_date,
                source_file=source_file,
                indent_level=indent_level,
                parent_url=parent_url,
            )

        # Try bare URL format: description - https://...
        url_match = self.BARE_URL.search(content)
        if url_match:
            url = url_match.group(1)
            # Description is everything before the URL
            description = content[: url_match.start()].strip(" -")
            return ExtractedLink(
                url=url,
                title=None,
                description=description if description else None,
                source_date=source_date,
                source_file=source_file,
                indent_level=indent_level,
                parent_url=parent_url,
            )

        # No URL found - skip this line
        return None
