"""AWS Bedrock Claude summarizer."""

import json
from typing import Any

import boto3

from .base import BaseSummarizer


class BedrockSummarizer(BaseSummarizer):
    """Summarizer using AWS Bedrock Claude models."""

    def __init__(
        self,
        model_id: str = "anthropic.claude-3-5-sonnet-20241022-v2:0",
        region: str = "us-east-1",
        max_tokens: int = 300,
    ):
        self.model_id = model_id
        self.region = region
        self.max_tokens = max_tokens
        self._client = None

    @property
    def client(self) -> Any:
        """Lazy initialization of Bedrock client."""
        if self._client is None:
            self._client = boto3.client(
                "bedrock-runtime",
                region_name=self.region,
            )
        return self._client

    @property
    def model_name(self) -> str:
        return self.model_id

    async def summarize(
        self,
        content: str,
        title: str | None = None,
        description: str | None = None,
        url: str | None = None,
    ) -> str:
        """Generate a summary using Bedrock Claude."""
        # Truncate content if too long
        max_content = 8000
        if len(content) > max_content:
            content = content[:max_content] + "..."

        prompt = f"""Summarize this web page in 2-3 sentences. Focus on the main topic and key takeaways.

Title: {title or 'Unknown'}
URL: {url or 'Unknown'}
User's note: {description or 'None provided'}

Content:
{content}

Summary:"""

        # Bedrock uses sync API, wrap in executor for async compatibility
        import asyncio

        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._invoke_model, prompt)

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
