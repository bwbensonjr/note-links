"""Scan daily notes directory for markdown files."""

import re
from datetime import date
from pathlib import Path


class DailyNotesScanner:
    """Scan the daily notes directory structure."""

    DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}\.md$")

    def __init__(self, daily_notes_path: Path):
        self.daily_notes_path = Path(daily_notes_path)

    def scan(
        self, date_from: str | None = None, date_to: str | None = None
    ) -> list[Path]:
        """
        Scan for daily note files, optionally filtered by date range.

        Args:
            date_from: Start date in YYYY-MM-DD format
            date_to: End date in YYYY-MM-DD format

        Returns:
            List of paths to daily note files, sorted by date descending
        """
        start_date = date.fromisoformat(date_from) if date_from else None
        end_date = date.fromisoformat(date_to) if date_to else None

        files = []
        for file_path in self.daily_notes_path.rglob("*.md"):
            if not self.DATE_PATTERN.match(file_path.name):
                continue

            file_date = self._extract_date(file_path)
            if file_date is None:
                continue

            if start_date and file_date < start_date:
                continue
            if end_date and file_date > end_date:
                continue

            files.append(file_path)

        # Sort by date descending (newest first)
        return sorted(files, key=lambda p: p.stem, reverse=True)

    def _extract_date(self, path: Path) -> date | None:
        """Extract date from filename like 2025-03-15.md"""
        try:
            parts = path.stem.split("-")
            return date(int(parts[0]), int(parts[1]), int(parts[2]))
        except (ValueError, IndexError):
            return None
