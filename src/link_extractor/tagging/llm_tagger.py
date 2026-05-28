"""LLM-based content tagging using AWS Bedrock Claude."""

import json
import logging
from typing import Any

import boto3

from ..storage.models import LinkRecord, Tag
from .vocabulary import available_tags

# Represents a tag the LLM suggested but wasn't in the vocabulary
RejectedTag = tuple[str, str | None]  # (name, category_or_none)

logger = logging.getLogger(__name__)


def _build_tag_list(vocab: dict[str, list[str]]) -> str:
    """Build a formatted list of available tags for the prompt."""
    lines = []
    for category, tags in vocab.items():
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
        self._vocab = available_tags()
        self._tag_list = _build_tag_list(self._vocab)

    @property
    def client(self) -> Any:
        """Lazy initialization of Bedrock client."""
        if self._client is None:
            self._client = boto3.client(
                "bedrock-runtime",
                region_name=self.region,
            )
        return self._client

    async def tag(
        self, link: LinkRecord
    ) -> tuple[list[tuple[Tag, float]], list[RejectedTag]]:
        """
        Generate tags for a link using LLM analysis.

        Returns (accepted_tags, rejected_tags) where accepted_tags is a list
        of (Tag, confidence) tuples and rejected_tags is a list of
        (name, category) tuples for tags the LLM suggested but aren't in
        the vocabulary.
        """
        prompt = self._build_prompt(link)

        import asyncio

        loop = asyncio.get_event_loop()
        try:
            response = await loop.run_in_executor(None, self._invoke_model, prompt)
            return self._parse_response(response)
        except Exception as e:
            logger.error(f"LLM tagging failed for {link.url}: {e}")
            return [], []

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
5. If — and only if — no tag in the vocabulary applies to this content, propose 1-2 hypothetical tag names with a plausible category (existing or new) in a separate `proposed_tags` array. Leave `proposed_tags` empty whenever any vocabulary tag fits.
6. Return ONLY valid JSON, no other text

Return your response as JSON in this exact format:
{{"tags": [{{"name": "tag-name", "category": "category_name", "confidence": 0.9}}], "proposed_tags": [{{"name": "hypothetical-tag", "category": "category_name", "confidence": 0.7}}]}}

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

    def _parse_response(
        self, response: str
    ) -> tuple[list[tuple[Tag, float]], list[RejectedTag]]:
        """Parse the LLM response into Tag objects and rejected tags."""
        tags = []
        rejected = []

        try:
            # Handle potential markdown code blocks — extract content
            # between opening and closing ``` fences only
            if response.startswith("```"):
                lines = response.split("\n")
                # Find the closing fence
                end = len(lines) - 1
                for i in range(1, len(lines)):
                    if lines[i].strip() == "```":
                        end = i
                        break
                response = "\n".join(lines[1:end])

            data = json.loads(response)

            for tag_data in data.get("tags", []):
                name = tag_data.get("name", "").lower().strip()
                category_str = tag_data.get("category", "").lower().strip()
                confidence = float(tag_data.get("confidence", 0.5))

                if category_str not in self._vocab:
                    logger.warning(f"Unknown category: {category_str}")
                    rejected.append((name, category_str if category_str else None))
                    continue

                if name not in self._vocab[category_str]:
                    logger.warning(f"Unknown tag: {name} in {category_str}")
                    rejected.append((name, category_str))
                    continue

                tags.append((Tag(name=name, category=category_str), min(confidence, 1.0)))

            for proposed in data.get("proposed_tags", []):
                name = proposed.get("name", "").lower().strip()
                category_str = proposed.get("category", "").lower().strip()
                if not name:
                    continue
                rejected.append((name, category_str if category_str else None))

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse LLM response: {e}")
            logger.debug(f"Response was: {response}")
        except (KeyError, ValueError) as e:
            logger.error(f"Invalid tag data in response: {e}")

        return tags, rejected
