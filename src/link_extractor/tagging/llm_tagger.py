"""LLM-based content tagging using AWS Bedrock Claude."""

import json
import logging
from typing import Any

import boto3

from ..storage.models import LinkRecord, Tag, TagCategory

logger = logging.getLogger(__name__)

# Complete tag vocabulary organized by category
AVAILABLE_TAGS: dict[str, list[str]] = {
    "programming_language": [
        "python",
        "rust",
        "typescript",
        "javascript",
        "lisp",
        "common-lisp",
        "clojure",
        "scheme",
        "haskell",
        "go",
        "c",
        "cpp",
        "nix",
        "sql",
        "swift",
        "java",
        "ruby",
        "elixir",
        "zig",
    ],
    "technical_topic": [
        "ai",
        "llm",
        "compilers",
        "github-repo",
        "database",
        "devops",
        "web-dev",
        "academic-paper",
        "tutorial",
        "cli-tool",
        "distributed-systems",
        "security",
        "emulator",
    ],
    "culture": [
        "tv",
        "movie",
        "fiction-book",
        "nonfiction-book",
        "music",
        "news",
        "politics",
        "podcast",
        "video",
        "gaming",
        "social-media",
    ],
}

# Mapping from category string to TagCategory enum
CATEGORY_MAP = {
    "programming_language": TagCategory.PROGRAMMING_LANGUAGE,
    "technical_topic": TagCategory.TECHNICAL_TOPIC,
    "culture": TagCategory.CULTURE,
}


def _build_tag_list() -> str:
    """Build a formatted list of available tags for the prompt."""
    lines = []
    for category, tags in AVAILABLE_TAGS.items():
        lines.append(f"\n{category}:")
        for tag in tags:
            lines.append(f"  - {tag}")
    return "\n".join(lines)


class LLMTagger:
    """Tag links using Claude via AWS Bedrock."""

    def __init__(
        self,
        model_id: str = "us.anthropic.claude-3-5-sonnet-20241022-v2:0",
        region: str = "us-east-1",
        max_tokens: int = 500,
    ):
        self.model_id = model_id
        self.region = region
        self.max_tokens = max_tokens
        self._client: Any = None
        self._tag_list = _build_tag_list()

    @property
    def client(self) -> Any:
        """Lazy initialization of Bedrock client."""
        if self._client is None:
            self._client = boto3.client(
                "bedrock-runtime",
                region_name=self.region,
            )
        return self._client

    async def tag(self, link: LinkRecord) -> list[tuple[Tag, float]]:
        """
        Generate tags for a link using LLM analysis.

        Returns list of (Tag, confidence) tuples.
        """
        prompt = self._build_prompt(link)

        import asyncio

        loop = asyncio.get_event_loop()
        try:
            response = await loop.run_in_executor(None, self._invoke_model, prompt)
            return self._parse_response(response)
        except Exception as e:
            logger.error(f"LLM tagging failed for {link.url}: {e}")
            return []

    def _build_prompt(self, link: LinkRecord) -> str:
        """Build the tagging prompt for a link."""
        # Gather all available text about the link
        title = link.title or link.page_title or "Unknown"
        summary = link.summary or ""
        description = link.description or ""
        url = link.url
        domain = link.domain

        return f"""Analyze this web link and assign appropriate tags from the available categories.

AVAILABLE TAGS:{self._tag_list}

LINK INFORMATION:
- Title: {title}
- URL: {url}
- Domain: {domain}
- User's description: {description or "None"}
- Summary: {summary or "None"}

INSTRUCTIONS:
1. Select 1-5 tags that best describe this content
2. Only use tags from the AVAILABLE TAGS list above
3. Assign a confidence score (0.0-1.0) for each tag
4. Higher confidence for explicit mentions, lower for inferred topics
5. Return ONLY valid JSON, no other text

Return your response as JSON in this exact format:
{{"tags": [{{"name": "tag-name", "category": "category_name", "confidence": 0.9}}]}}

JSON response:"""

    def _invoke_model(self, prompt: str) -> str:
        """Invoke the Bedrock model synchronously."""
        body = json.dumps(
            {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": self.max_tokens,
                "messages": [{"role": "user", "content": prompt}],
            }
        )

        response = self.client.invoke_model(
            modelId=self.model_id,
            body=body,
            contentType="application/json",
            accept="application/json",
        )

        response_body = json.loads(response["body"].read())
        return response_body["content"][0]["text"].strip()

    def _parse_response(self, response: str) -> list[tuple[Tag, float]]:
        """Parse the LLM response into Tag objects."""
        tags = []

        try:
            # Handle potential markdown code blocks
            if response.startswith("```"):
                lines = response.split("\n")
                response = "\n".join(lines[1:-1])

            data = json.loads(response)

            for tag_data in data.get("tags", []):
                name = tag_data.get("name", "").lower().strip()
                category_str = tag_data.get("category", "").lower().strip()
                confidence = float(tag_data.get("confidence", 0.5))

                # Validate tag exists in our vocabulary
                if category_str not in AVAILABLE_TAGS:
                    logger.warning(f"Unknown category: {category_str}")
                    continue

                if name not in AVAILABLE_TAGS[category_str]:
                    logger.warning(f"Unknown tag: {name} in {category_str}")
                    continue

                category = CATEGORY_MAP[category_str]
                tags.append((Tag(name=name, category=category), min(confidence, 1.0)))

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse LLM response: {e}")
            logger.debug(f"Response was: {response}")
        except (KeyError, ValueError) as e:
            logger.error(f"Invalid tag data in response: {e}")

        return tags
