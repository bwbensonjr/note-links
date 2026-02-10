"""Extract readable text content from HTML."""

import re

from bs4 import BeautifulSoup

MIN_CONTENT_LENGTH = 50


class ContentExtractor:
    """Extract main text content from HTML."""

    REMOVE_TAGS = {"script", "style", "nav", "header", "footer", "aside", "form", "noscript"}

    def extract(self, html: str, max_length: int = 10000) -> str:
        """Extract main text content from HTML."""
        soup = BeautifulSoup(html, "html.parser")

        # Remove unwanted elements
        for tag in self.REMOVE_TAGS:
            for element in soup.find_all(tag):
                element.decompose()

        # Try to find main content area, with fallback if empty.
        # Use find_all for divs so all matching divs are tried, not just the first.
        candidates = [
            soup.find("article"),
            soup.find("main"),
            *soup.find_all("div", class_=re.compile(r"content|article|post", re.I)),
            soup.body,
        ]

        text = ""
        for candidate in candidates:
            if candidate:
                raw = candidate.get_text(separator=" ", strip=True)
                if raw:
                    normalized = re.sub(r"\s+", " ", raw)
                    if len(normalized) >= MIN_CONTENT_LENGTH:
                        text = normalized
                        break

        if not text:
            return ""

        return text[:max_length]
