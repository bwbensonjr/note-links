"""PDF text extraction."""

import tempfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import aiohttp
import pymupdf

from ..storage.models import FetchStatus


@dataclass
class PDFResult:
    """Result of PDF extraction."""

    status: FetchStatus
    content: str | None = None
    title: str | None = None
    error: str | None = None
    fetched_at: datetime | None = None


class PDFExtractor:
    """Download and extract text from PDF files."""

    def __init__(
        self,
        timeout_seconds: int = 60,
        max_pages: int = 50,
        max_content_length: int = 50000,
        user_agent: str = "ObsidianLinkExtractor/1.0",
    ):
        self.timeout = aiohttp.ClientTimeout(total=timeout_seconds)
        self.max_pages = max_pages
        self.max_content_length = max_content_length
        self.user_agent = user_agent

    async def extract(self, url: str) -> PDFResult:
        """Download PDF and extract text."""
        try:
            # Download PDF to temp file
            pdf_bytes = await self._download(url)
            if pdf_bytes is None:
                return PDFResult(
                    status=FetchStatus.FAILED,
                    error="Failed to download PDF",
                    fetched_at=datetime.now(),
                )

            # Extract text
            text, title = self._extract_text(pdf_bytes)

            return PDFResult(
                status=FetchStatus.SUCCESS,
                content=text,
                title=title,
                fetched_at=datetime.now(),
            )

        except Exception as e:
            return PDFResult(
                status=FetchStatus.FAILED,
                error=str(e),
                fetched_at=datetime.now(),
            )

    async def _download(self, url: str) -> bytes | None:
        """Download PDF file."""
        try:
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                headers = {"User-Agent": self.user_agent}
                async with session.get(url, headers=headers) as response:
                    if response.status != 200:
                        return None
                    return await response.read()
        except Exception:
            return None

    def _extract_text(self, pdf_bytes: bytes) -> tuple[str, str | None]:
        """Extract text from PDF bytes."""
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=True) as tmp:
            tmp.write(pdf_bytes)
            tmp.flush()

            doc = pymupdf.open(tmp.name)
            title = doc.metadata.get("title") if doc.metadata else None

            text_parts = []
            for page_num, page in enumerate(doc):
                if page_num >= self.max_pages:
                    break
                text_parts.append(page.get_text())

            doc.close()

            full_text = "\n".join(text_parts)
            # Clean up whitespace
            full_text = " ".join(full_text.split())

            if len(full_text) > self.max_content_length:
                full_text = full_text[: self.max_content_length]

            return full_text, title
