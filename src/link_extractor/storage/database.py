"""SQLite database operations with full-text search."""

import sqlite3
from contextlib import contextmanager
from datetime import date, datetime
from pathlib import Path
from typing import Generator
from urllib.parse import urlparse

from .models import ExtractedLink, FetchStatus, LinkRecord, Tag, TagCategory

SCHEMA_SQL = """
-- Main links table
CREATE TABLE IF NOT EXISTS links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT UNIQUE NOT NULL,
    title TEXT,
    description TEXT,
    domain TEXT NOT NULL,
    source_date DATE NOT NULL,
    source_file TEXT NOT NULL,
    parent_url TEXT,
    indent_level INTEGER DEFAULT 0,

    page_title TEXT,
    page_content TEXT,
    fetch_status TEXT DEFAULT 'not_fetched',
    fetch_error TEXT,
    fetched_at TIMESTAMP,

    summary TEXT,
    summarized_at TIMESTAMP,
    summarizer_model TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tags table
CREATE TABLE IF NOT EXISTS tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    category TEXT NOT NULL
);

-- Link-tag association
CREATE TABLE IF NOT EXISTS link_tags (
    link_id INTEGER REFERENCES links(id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES tags(id) ON DELETE CASCADE,
    confidence REAL DEFAULT 1.0,
    source TEXT DEFAULT 'auto',
    PRIMARY KEY (link_id, tag_id)
);

-- Processing log for incremental updates
CREATE TABLE IF NOT EXISTS processing_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_file TEXT UNIQUE NOT NULL,
    file_hash TEXT NOT NULL,
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_links_source_date ON links(source_date);
CREATE INDEX IF NOT EXISTS idx_links_domain ON links(domain);
CREATE INDEX IF NOT EXISTS idx_links_fetch_status ON links(fetch_status);

-- Full-text search virtual table
CREATE VIRTUAL TABLE IF NOT EXISTS links_fts USING fts5(
    title,
    description,
    page_content,
    summary,
    content='links',
    content_rowid='id'
);

-- Triggers to keep FTS in sync
CREATE TRIGGER IF NOT EXISTS links_ai AFTER INSERT ON links BEGIN
    INSERT INTO links_fts(rowid, title, description, page_content, summary)
    VALUES (new.id, new.title, new.description, new.page_content, new.summary);
END;

CREATE TRIGGER IF NOT EXISTS links_au AFTER UPDATE ON links BEGIN
    INSERT INTO links_fts(links_fts, rowid, title, description, page_content, summary)
    VALUES ('delete', old.id, old.title, old.description, old.page_content, old.summary);
    INSERT INTO links_fts(rowid, title, description, page_content, summary)
    VALUES (new.id, new.title, new.description, new.page_content, new.summary);
END;

CREATE TRIGGER IF NOT EXISTS links_ad AFTER DELETE ON links BEGIN
    INSERT INTO links_fts(links_fts, rowid, title, description, page_content, summary)
    VALUES ('delete', old.id, old.title, old.description, old.page_content, old.summary);
END;
"""


class Database:
    """SQLite database operations for link storage."""

    def __init__(self, db_path: Path):
        self.db_path = Path(db_path)
        self._init_schema()

    @contextmanager
    def _connection(self) -> Generator[sqlite3.Connection, None, None]:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()

    def _init_schema(self) -> None:
        """Initialize database schema."""
        with self._connection() as conn:
            conn.executescript(SCHEMA_SQL)

    def link_exists(self, url: str) -> bool:
        """Check if a link already exists."""
        with self._connection() as conn:
            result = conn.execute(
                "SELECT 1 FROM links WHERE url = ?", (url,)
            ).fetchone()
            return result is not None

    def insert_link(self, link: ExtractedLink) -> int:
        """Insert a new link, return its ID."""
        domain = urlparse(link.url).netloc

        with self._connection() as conn:
            cursor = conn.execute(
                """
                INSERT INTO links (url, title, description, domain, source_date,
                                   source_file, parent_url, indent_level, fetch_status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    link.url,
                    link.title,
                    link.description,
                    domain,
                    link.source_date.isoformat(),
                    link.source_file,
                    link.parent_url,
                    link.indent_level,
                    FetchStatus.NOT_FETCHED.value,
                ),
            )
            return cursor.lastrowid  # type: ignore

    def update_fetch_result(
        self,
        link_id: int,
        status: FetchStatus,
        content: str | None = None,
        page_title: str | None = None,
        error: str | None = None,
    ) -> None:
        """Update link with fetch results."""
        with self._connection() as conn:
            conn.execute(
                """
                UPDATE links
                SET fetch_status = ?, page_content = ?, page_title = ?,
                    fetch_error = ?, fetched_at = datetime('now'),
                    updated_at = datetime('now')
                WHERE id = ?
                """,
                (status.value, content, page_title, error, link_id),
            )

    def update_summary(self, link_id: int, summary: str, model: str) -> None:
        """Update link with summary."""
        with self._connection() as conn:
            conn.execute(
                """
                UPDATE links
                SET summary = ?, summarizer_model = ?,
                    summarized_at = datetime('now'),
                    updated_at = datetime('now')
                WHERE id = ?
                """,
                (summary, model, link_id),
            )

    def add_tag(
        self, link_id: int, tag: Tag, confidence: float, source: str = "auto"
    ) -> None:
        """Add a tag to a link."""
        with self._connection() as conn:
            # Ensure tag exists
            conn.execute(
                "INSERT OR IGNORE INTO tags (name, category) VALUES (?, ?)",
                (tag.name, tag.category.value),
            )

            tag_row = conn.execute(
                "SELECT id FROM tags WHERE name = ?", (tag.name,)
            ).fetchone()
            tag_id = tag_row[0]

            conn.execute(
                """
                INSERT OR REPLACE INTO link_tags (link_id, tag_id, confidence, source)
                VALUES (?, ?, ?, ?)
                """,
                (link_id, tag_id, confidence, source),
            )

    def clear_tags_for_link(self, link_id: int) -> None:
        """Remove all tags for a specific link."""
        with self._connection() as conn:
            conn.execute("DELETE FROM link_tags WHERE link_id = ?", (link_id,))

    def clear_all_tags(self) -> None:
        """Remove all link-tag associations."""
        with self._connection() as conn:
            conn.execute("DELETE FROM link_tags")

    def get_all_links_with_content(self, limit: int | None = None) -> list[LinkRecord]:
        """Get all links that have been processed (fetched, failed, or skipped)."""
        with self._connection() as conn:
            query = """
                SELECT * FROM links
                WHERE fetch_status != ?
                ORDER BY source_date DESC
            """
            if limit:
                query += f" LIMIT {limit}"
            rows = conn.execute(query, (FetchStatus.NOT_FETCHED.value,)).fetchall()
            return [self._row_to_link(row) for row in rows]

    def get_untagged_links(self, limit: int | None = None) -> list[LinkRecord]:
        """Get processed links that have no tags yet."""
        with self._connection() as conn:
            query = """
                SELECT * FROM links
                WHERE fetch_status != ?
                  AND id NOT IN (SELECT DISTINCT link_id FROM link_tags)
                ORDER BY source_date DESC
            """
            if limit:
                query += f" LIMIT {limit}"
            rows = conn.execute(query, (FetchStatus.NOT_FETCHED.value,)).fetchall()
            return [self._row_to_link(row) for row in rows]

    def get_link_by_id(self, link_id: int) -> LinkRecord | None:
        """Get a link by ID."""
        with self._connection() as conn:
            row = conn.execute(
                "SELECT * FROM links WHERE id = ?", (link_id,)
            ).fetchone()
            return self._row_to_link(row) if row else None

    def get_unfetched_links(self, limit: int = 100) -> list[LinkRecord]:
        """Get links that haven't been fetched yet."""
        with self._connection() as conn:
            rows = conn.execute(
                """
                SELECT * FROM links
                WHERE fetch_status = ?
                ORDER BY source_date DESC
                LIMIT ?
                """,
                (FetchStatus.NOT_FETCHED.value, limit),
            ).fetchall()
            return [self._row_to_link(row) for row in rows]

    def get_empty_content_links(self, limit: int = 100, min_length: int = 50) -> list[LinkRecord]:
        """Get links that were fetched successfully but have empty or too-short content."""
        with self._connection() as conn:
            rows = conn.execute(
                """
                SELECT * FROM links
                WHERE fetch_status = ?
                  AND (page_content IS NULL OR page_content = '' OR LENGTH(page_content) < ?)
                ORDER BY source_date DESC
                LIMIT ?
                """,
                (FetchStatus.SUCCESS.value, min_length, limit),
            ).fetchall()
            return [self._row_to_link(row) for row in rows]

    def reset_fetch_status(self, link_id: int) -> None:
        """Reset a link's fetch status to allow re-fetching."""
        with self._connection() as conn:
            conn.execute(
                """
                UPDATE links
                SET fetch_status = ?, page_content = NULL, page_title = NULL,
                    fetch_error = NULL, fetched_at = NULL, updated_at = datetime('now')
                WHERE id = ?
                """,
                (FetchStatus.NOT_FETCHED.value, link_id),
            )

    def reset_summary(self, link_id: int) -> None:
        """Clear summary data for a link so it can be re-summarized."""
        with self._connection() as conn:
            conn.execute(
                """
                UPDATE links
                SET summary = NULL, summarizer_model = NULL,
                    summarized_at = NULL, updated_at = datetime('now')
                WHERE id = ?
                """,
                (link_id,),
            )

    def get_unsummarized_links(self, limit: int = 100) -> list[LinkRecord]:
        """Get links that have been fetched (any status) but not summarized."""
        with self._connection() as conn:
            rows = conn.execute(
                """
                SELECT * FROM links
                WHERE fetch_status != ? AND summary IS NULL
                ORDER BY source_date DESC
                LIMIT ?
                """,
                (FetchStatus.NOT_FETCHED.value, limit),
            ).fetchall()
            return [self._row_to_link(row) for row in rows]

    def search(self, query: str, limit: int = 50) -> list[LinkRecord]:
        """Full-text search across links."""
        with self._connection() as conn:
            rows = conn.execute(
                """
                SELECT links.* FROM links
                JOIN links_fts ON links.id = links_fts.rowid
                WHERE links_fts MATCH ?
                ORDER BY rank
                LIMIT ?
                """,
                (query, limit),
            ).fetchall()
            return [self._row_to_link(row) for row in rows]

    def get_links_by_tag(self, tag_name: str) -> list[LinkRecord]:
        """Get all links with a specific tag."""
        with self._connection() as conn:
            rows = conn.execute(
                """
                SELECT links.* FROM links
                JOIN link_tags ON links.id = link_tags.link_id
                JOIN tags ON link_tags.tag_id = tags.id
                WHERE tags.name = ?
                ORDER BY links.source_date DESC
                """,
                (tag_name,),
            ).fetchall()
            return [self._row_to_link(row) for row in rows]

    def get_links_by_date_range(
        self, start_date: date, end_date: date
    ) -> list[LinkRecord]:
        """Get links from a date range."""
        with self._connection() as conn:
            rows = conn.execute(
                """
                SELECT * FROM links
                WHERE source_date BETWEEN ? AND ?
                ORDER BY source_date DESC
                """,
                (start_date.isoformat(), end_date.isoformat()),
            ).fetchall()
            return [self._row_to_link(row) for row in rows]

    def get_all_tags(self) -> list[tuple[str, str, int]]:
        """Get all tags with their counts."""
        with self._connection() as conn:
            rows = conn.execute(
                """
                SELECT t.name, t.category, COUNT(lt.link_id) as count
                FROM tags t
                LEFT JOIN link_tags lt ON t.id = lt.tag_id
                GROUP BY t.id
                ORDER BY count DESC
                """
            ).fetchall()
            return [(row["name"], row["category"], row["count"]) for row in rows]

    def get_stats(self) -> dict:
        """Get database statistics."""
        with self._connection() as conn:
            total = conn.execute("SELECT COUNT(*) FROM links").fetchone()[0]
            fetched = conn.execute(
                "SELECT COUNT(*) FROM links WHERE fetch_status = ?",
                (FetchStatus.SUCCESS.value,),
            ).fetchone()[0]
            summarized = conn.execute(
                "SELECT COUNT(*) FROM links WHERE summary IS NOT NULL"
            ).fetchone()[0]
            tagged = conn.execute(
                "SELECT COUNT(DISTINCT link_id) FROM link_tags"
            ).fetchone()[0]

            return {
                "total_links": total,
                "fetched": fetched,
                "summarized": summarized,
                "tagged": tagged,
            }

    def file_needs_processing(self, file_path: str, file_hash: str) -> bool:
        """Check if file needs to be (re)processed."""
        with self._connection() as conn:
            result = conn.execute(
                "SELECT file_hash FROM processing_log WHERE source_file = ?",
                (file_path,),
            ).fetchone()

            if result is None:
                return True
            return result[0] != file_hash

    def mark_file_processed(self, file_path: str, file_hash: str) -> None:
        """Mark a file as processed."""
        with self._connection() as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO processing_log (source_file, file_hash, processed_at)
                VALUES (?, ?, datetime('now'))
                """,
                (file_path, file_hash),
            )

    def _row_to_link(self, row: sqlite3.Row) -> LinkRecord:
        """Convert database row to LinkRecord."""
        return LinkRecord(
            id=row["id"],
            url=row["url"],
            title=row["title"],
            description=row["description"],
            domain=row["domain"],
            source_date=date.fromisoformat(row["source_date"]),
            source_file=row["source_file"],
            parent_url=row["parent_url"],
            indent_level=row["indent_level"],
            page_title=row["page_title"],
            page_content=row["page_content"],
            fetch_status=FetchStatus(row["fetch_status"]),
            fetch_error=row["fetch_error"],
            summary=row["summary"],
            summarizer_model=row["summarizer_model"],
        )

    # ---- Web UI methods ----

    def get_recent_links(self, limit: int = 20) -> list[LinkRecord]:
        """Get most recent links by source_date."""
        with self._connection() as conn:
            rows = conn.execute(
                "SELECT * FROM links ORDER BY source_date DESC, id DESC LIMIT ?",
                (limit,),
            ).fetchall()
            return [self._row_to_link(row) for row in rows]

    def get_links_paginated(
        self,
        page: int = 1,
        per_page: int = 25,
        sort_by: str = "date_desc",
        tags: list[str] | None = None,
        domain: str | None = None,
        date_from: date | None = None,
        date_to: date | None = None,
    ) -> tuple[list[LinkRecord], int]:
        """Get paginated links with filters. Returns (links, total_count)."""
        conditions = []
        params: list = []

        if tags:
            # Find links that have ALL specified tags (AND logic)
            placeholders = ",".join("?" * len(tags))
            conditions.append(f"""
                id IN (
                    SELECT link_id FROM link_tags
                    JOIN tags ON link_tags.tag_id = tags.id
                    WHERE tags.name IN ({placeholders})
                    GROUP BY link_id
                    HAVING COUNT(DISTINCT tags.name) = ?
                )
            """)
            params.extend(tags)
            params.append(len(tags))

        if domain:
            conditions.append("domain = ?")
            params.append(domain)

        if date_from:
            conditions.append("source_date >= ?")
            params.append(date_from.isoformat())

        if date_to:
            conditions.append("source_date <= ?")
            params.append(date_to.isoformat())

        where_clause = " AND ".join(conditions) if conditions else "1=1"

        sort_map = {
            "date_desc": "source_date DESC, id DESC",
            "date_asc": "source_date ASC, id ASC",
            "title": "COALESCE(title, description, url) ASC",
            "domain": "domain ASC, source_date DESC",
        }
        order_by = sort_map.get(sort_by, "source_date DESC, id DESC")

        offset = (page - 1) * per_page

        with self._connection() as conn:
            # Get total count
            count_row = conn.execute(
                f"SELECT COUNT(*) FROM links WHERE {where_clause}", params
            ).fetchone()
            total = count_row[0]

            # Get paginated results
            rows = conn.execute(
                f"""
                SELECT * FROM links
                WHERE {where_clause}
                ORDER BY {order_by}
                LIMIT ? OFFSET ?
                """,
                params + [per_page, offset],
            ).fetchall()

            return [self._row_to_link(row) for row in rows], total

    def get_tags_for_link(self, link_id: int) -> list[tuple[str, str, float]]:
        """Get all tags for a specific link. Returns [(name, category, confidence), ...]."""
        with self._connection() as conn:
            rows = conn.execute(
                """
                SELECT t.name, t.category, lt.confidence
                FROM tags t
                JOIN link_tags lt ON t.id = lt.tag_id
                WHERE lt.link_id = ?
                ORDER BY lt.confidence DESC
                """,
                (link_id,),
            ).fetchall()
            return [(r["name"], r["category"], r["confidence"]) for r in rows]

    def get_all_domains(self) -> list[tuple[str, int]]:
        """Get all domains with link counts."""
        with self._connection() as conn:
            rows = conn.execute(
                """
                SELECT domain, COUNT(*) as count
                FROM links
                GROUP BY domain
                ORDER BY count DESC
                """
            ).fetchall()
            return [(r["domain"], r["count"]) for r in rows]

    def get_date_counts(self) -> list[tuple[str, int]]:
        """Get link counts per date."""
        with self._connection() as conn:
            rows = conn.execute(
                """
                SELECT source_date, COUNT(*) as count
                FROM links
                GROUP BY source_date
                ORDER BY source_date DESC
                """
            ).fetchall()
            return [(r["source_date"], r["count"]) for r in rows]
