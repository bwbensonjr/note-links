"""Extract readable text content from HTML."""

import re

from bs4 import BeautifulSoup
from markdownify import markdownify as html_to_markdown

MIN_CONTENT_LENGTH = 50


class ContentExtractor:
    """Extract main text content from HTML."""

    REMOVE_TAGS = {"script", "style", "nav", "header", "footer", "aside", "form", "noscript"}

    def _main_content_element(self, html: str):
        """Strip boilerplate and return the element holding the main content.

        Returns a BeautifulSoup element whose text is at least
        MIN_CONTENT_LENGTH, or None if nothing suitable is found.
        """
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

        for candidate in candidates:
            if candidate and candidate.get_text(strip=True):
                return candidate
        return None

    def extract(self, html: str, max_length: int = 10000) -> str:
        """Extract main text content from HTML."""
        element = self._main_content_element(html)
        if not element:
            return ""

        raw = element.get_text(separator=" ", strip=True)
        normalized = re.sub(r"\s+", " ", raw)
        if len(normalized) < MIN_CONTENT_LENGTH:
            return ""

        return normalized[:max_length]

    def extract_markdown(self, html: str) -> str:
        """Render the main content area as Markdown (chrome stripped).

        Reuses the same boilerplate removal and content selection as extract(),
        but converts the chosen element's HTML to Markdown rather than flat
        text. Returns "" when no main content can be found.
        """
        element = self._main_content_element(html)
        if not element:
            return ""

        return html_to_markdown(str(element), strip=["script", "style"]).strip()
