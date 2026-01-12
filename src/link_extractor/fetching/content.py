"""Extract readable text content from HTML."""

import re

from bs4 import BeautifulSoup


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

        # Try to find main content area, with fallback if empty
        candidates = [
            soup.find("article"),
            soup.find("main"),
            soup.find("div", class_=re.compile(r"content|article|post", re.I)),
            soup.body,
        ]

        text = ""
        for candidate in candidates:
            if candidate:
                text = candidate.get_text(separator=" ", strip=True)
                if text:  # Use first non-empty match
                    break

        if not text:
            return ""
        text = re.sub(r"\s+", " ", text)  # Normalize whitespace

        return text[:max_length]
