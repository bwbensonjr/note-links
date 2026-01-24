"""Async web fetcher with rate limiting."""

import asyncio
import html
import re
from dataclasses import dataclass, field
from datetime import datetime
from urllib.parse import urlparse

import aiohttp

from ..storage.models import FetchStatus


@dataclass
class FetchResult:
    """Result of a fetch operation."""

    status: FetchStatus
    content: str | None = None
    title: str | None = None
    error: str | None = None
    content_type: str | None = None
    fetched_at: datetime = field(default_factory=datetime.now)


class RateLimitedFetcher:
    """Async web fetcher with per-domain rate limiting."""

    SKIP_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".mp4", ".mp3", ".wav"}
    PDF_EXTENSIONS = {".pdf"}

    def __init__(
        self,
        requests_per_second: float = 1.0,
        timeout_seconds: int = 30,
        max_content_length: int = 1_000_000,
        user_agent: str = "ObsidianLinkExtractor/1.0",
    ):
        self.min_interval = 1.0 / requests_per_second
        self.timeout = aiohttp.ClientTimeout(total=timeout_seconds)
        self.max_content_length = max_content_length
        self.user_agent = user_agent
        self._domain_last_request: dict[str, float] = {}
        self._lock = asyncio.Lock()

    def is_pdf(self, url: str) -> bool:
        """Check if URL points to a PDF."""
        path = urlparse(url).path.lower()
        return any(path.endswith(ext) for ext in self.PDF_EXTENSIONS)

    def should_skip(self, url: str) -> bool:
        """Check if URL should be skipped based on extension."""
        path = urlparse(url).path.lower()
        return any(path.endswith(ext) for ext in self.SKIP_EXTENSIONS)

    async def fetch(self, url: str) -> FetchResult:
        """Fetch a URL with rate limiting."""
        # Skip media files
        if self.should_skip(url):
            return FetchResult(
                status=FetchStatus.SKIPPED, error="Non-HTML content type (media file)"
            )

        # PDFs handled separately
        if self.is_pdf(url):
            return FetchResult(
                status=FetchStatus.SKIPPED,
                error="PDF - use pdf_extractor",
                content_type="application/pdf",
            )

        domain = urlparse(url).netloc
        await self._rate_limit(domain)

        try:
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                headers = {"User-Agent": self.user_agent}
                async with session.get(
                    url, headers=headers, allow_redirects=True
                ) as response:
                    if response.status != 200:
                        return FetchResult(
                            status=FetchStatus.FAILED, error=f"HTTP {response.status}"
                        )

                    content_type = response.headers.get("content-type", "")
                    if "text/html" not in content_type.lower():
                        return FetchResult(
                            status=FetchStatus.SKIPPED,
                            error=f"Non-HTML content: {content_type}",
                            content_type=content_type,
                        )

                    content = await response.text()
                    if len(content) > self.max_content_length:
                        content = content[: self.max_content_length]

                    title = self._extract_title(content)

                    return FetchResult(
                        status=FetchStatus.SUCCESS,
                        content=content,
                        title=title,
                        content_type=content_type,
                    )

        except asyncio.TimeoutError:
            return FetchResult(status=FetchStatus.TIMEOUT, error="Request timed out")
        except aiohttp.ClientError as e:
            return FetchResult(status=FetchStatus.FAILED, error=str(e))
        except Exception as e:
            return FetchResult(status=FetchStatus.FAILED, error=f"Unexpected: {e}")

    async def _rate_limit(self, domain: str) -> None:
        """Apply per-domain rate limiting."""
        async with self._lock:
            now = asyncio.get_event_loop().time()
            last_request = self._domain_last_request.get(domain, 0)
            wait_time = self.min_interval - (now - last_request)
            if wait_time > 0:
                await asyncio.sleep(wait_time)
            self._domain_last_request[domain] = asyncio.get_event_loop().time()

    def _extract_title(self, html_content: str) -> str | None:
        """Extract title from HTML."""
        match = re.search(r"<title[^>]*>([^<]+)</title>", html_content, re.IGNORECASE)
        if match:
            raw_title = match.group(1).strip()
            return html.unescape(raw_title)
        return None
