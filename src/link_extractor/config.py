"""Configuration management."""

import os
from dataclasses import dataclass
from pathlib import Path

import yaml
from dotenv import load_dotenv

# Load .env file from current working directory
load_dotenv()


@dataclass
class Config:
    """Application configuration."""

    daily_notes_path: Path
    database_path: Path
    rate_limit_per_second: float = 1.0
    fetch_timeout_seconds: int = 30
    max_content_length: int = 1_000_000
    bedrock_model: str = "anthropic.claude-3-5-sonnet-20241022-v2:0"
    bedrock_region: str = "us-east-1"
    skip_existing: bool = True
    batch_size: int = 50

    @classmethod
    def from_yaml(cls, path: str | Path) -> "Config":
        """Load configuration from YAML file.

        Environment variables take precedence over YAML values:
        - DAILY_NOTES_PATH: Path to daily notes directory
        - DATABASE_PATH: Path to SQLite database file
        """
        with open(path) as f:
            data = yaml.safe_load(f)

        # Environment variables take precedence over YAML config
        daily_notes_path = os.environ.get("DAILY_NOTES_PATH") or data.get("daily_notes_path")
        database_path = os.environ.get("DATABASE_PATH") or data.get("database_path", "./links.db")

        if not daily_notes_path:
            raise ValueError(
                "daily_notes_path must be set via DAILY_NOTES_PATH environment variable "
                "or in config.yaml"
            )

        return cls(
            daily_notes_path=Path(daily_notes_path).expanduser(),
            database_path=Path(database_path).expanduser(),
            rate_limit_per_second=data.get("rate_limit_per_second", 1.0),
            fetch_timeout_seconds=data.get("fetch_timeout_seconds", 30),
            max_content_length=data.get("max_content_length", 1_000_000),
            bedrock_model=data.get(
                "bedrock_model", "anthropic.claude-3-5-sonnet-20241022-v2:0"
            ),
            bedrock_region=data.get("bedrock_region", "us-east-1"),
            skip_existing=data.get("skip_existing", True),
            batch_size=data.get("batch_size", 50),
        )
