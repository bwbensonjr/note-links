"""Data models for link extraction."""

from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from typing import Optional


class FetchStatus(Enum):
    NOT_FETCHED = "not_fetched"
    SUCCESS = "success"
    FAILED = "failed"
    TIMEOUT = "timeout"
    SKIPPED = "skipped"


class TagCategory(Enum):
    PROGRAMMING_LANGUAGE = "programming_language"
    TECHNICAL_TOPIC = "technical_topic"
    CULTURE = "culture"


@dataclass
class ExtractedLink:
    """Raw link extracted from markdown."""

    url: str
    source_date: date
    source_file: str
    description: Optional[str] = None
    title: Optional[str] = None
    indent_level: int = 0
    parent_url: Optional[str] = None


@dataclass
class Tag:
    """A categorization tag."""

    name: str
    category: TagCategory
    id: Optional[int] = None


@dataclass
class LinkRecord:
    """Full link record with all metadata."""

    id: Optional[int]
    url: str
    domain: str
    source_date: date
    source_file: str
    title: Optional[str] = None
    description: Optional[str] = None
    parent_url: Optional[str] = None
    indent_level: int = 0

    # Fetch data
    page_title: Optional[str] = None
    page_content: Optional[str] = None
    fetch_status: FetchStatus = FetchStatus.NOT_FETCHED
    fetch_error: Optional[str] = None
    fetched_at: Optional[datetime] = None

    # Summary data
    summary: Optional[str] = None
    summarized_at: Optional[datetime] = None
    summarizer_model: Optional[str] = None

    # Tags
    tags: list[Tag] = field(default_factory=list)

    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
