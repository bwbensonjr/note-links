"""RSS 2.0 feed generation."""

import html
from datetime import date, datetime
from email.utils import format_datetime
from typing import Optional
from xml.etree.ElementTree import Element, SubElement, tostring

from ..storage.models import LinkRecord


def _date_to_rfc822(d: date | datetime) -> str:
    """Convert a date to RFC 822 format for RSS pubDate."""
    if isinstance(d, datetime):
        dt = d
    else:
        dt = datetime(d.year, d.month, d.day, 12, 0, 0)
    return format_datetime(dt)


def generate_rss(
    links: list[LinkRecord],
    tags_by_link: dict[int, list[str]],
    title: str,
    description: str,
    site_url: str,
    limit: Optional[int] = None,
) -> str:
    """Generate RSS 2.0 XML from link records.

    Args:
        links: List of LinkRecord objects to include
        tags_by_link: Dict mapping link ID to list of tag names
        title: Feed title
        description: Feed description
        site_url: Base URL for the feed
        limit: Maximum number of items (None for all)

    Returns:
        RSS 2.0 XML as a string
    """
    # Sort by source_date descending (newest first)
    sorted_links = sorted(
        links,
        key=lambda x: x.source_date if x.source_date else date.min,
        reverse=True,
    )

    if limit:
        sorted_links = sorted_links[:limit]

    # Build RSS structure
    rss = Element("rss", version="2.0")
    channel = SubElement(rss, "channel")

    # Channel metadata
    SubElement(channel, "title").text = title
    SubElement(channel, "link").text = site_url
    SubElement(channel, "description").text = description
    SubElement(channel, "lastBuildDate").text = format_datetime(datetime.now())

    # Add items
    for link in sorted_links:
        item = SubElement(channel, "item")

        # Title: prefer page_title, fall back to title/description/url
        # Decode HTML entities that may be stored in older database records
        item_title = link.page_title or link.title or link.description or link.url
        SubElement(item, "title").text = html.unescape(item_title) if item_title else None

        # Link
        SubElement(item, "link").text = link.url

        # Description: prefer summary, fall back to description
        item_desc = link.summary or link.description or ""
        if item_desc:
            SubElement(item, "description").text = item_desc

        # pubDate from source_date
        if link.source_date:
            SubElement(item, "pubDate").text = _date_to_rfc822(link.source_date)

        # guid (use URL as permalink)
        guid = SubElement(item, "guid", isPermaLink="true")
        guid.text = link.url

        # Categories (tags)
        link_tags = tags_by_link.get(link.id, []) if link.id else []
        for tag_name in link_tags:
            SubElement(item, "category").text = tag_name

    # Convert to string with XML declaration
    xml_bytes = tostring(rss, encoding="unicode")
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + xml_bytes
