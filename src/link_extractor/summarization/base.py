"""Abstract base class for summarizers."""

from abc import ABC, abstractmethod


class BaseSummarizer(ABC):
    """Abstract base class for content summarizers."""

    @abstractmethod
    async def summarize(
        self,
        content: str,
        title: str | None = None,
        description: str | None = None,
        url: str | None = None,
    ) -> str:
        """Generate a summary of the content."""
        pass

    @property
    @abstractmethod
    def model_name(self) -> str:
        """Return the model identifier."""
        pass
