"""CLI entry point and main pipeline."""

import asyncio
import hashlib
import logging
from pathlib import Path

import click

from .config import Config
from .extraction.parser import MarkdownLinkParser
from .extraction.scanner import DailyNotesScanner
from .fetching.content import ContentExtractor
from .fetching.fetcher import RateLimitedFetcher
from .fetching.pdf import PDFExtractor
from .storage.database import Database
from .storage.models import FetchStatus
from .summarization.bedrock import BedrockSummarizer
from .tagging.llm_tagger import LLMTagger

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class LinkExtractorPipeline:
    """Main pipeline orchestrating the extraction process."""

    def __init__(self, config: Config):
        self.config = config
        self.db = Database(config.database_path)
        self.parser = MarkdownLinkParser()
        self.scanner = DailyNotesScanner(config.daily_notes_path)
        self.fetcher = RateLimitedFetcher(
            requests_per_second=config.rate_limit_per_second,
            timeout_seconds=config.fetch_timeout_seconds,
        )
        self.pdf_extractor = PDFExtractor(timeout_seconds=config.fetch_timeout_seconds)
        self.content_extractor = ContentExtractor()
        self.summarizer = BedrockSummarizer(
            model_id=config.bedrock_model, region=config.bedrock_region
        )
        self.tagger = LLMTagger(
            model_id=config.bedrock_model, region=config.bedrock_region
        )

    async def run(
        self,
        skip_existing: bool = True,
        fetch: bool = True,
        summarize: bool = True,
        tag: bool = True,
        date_from: str | None = None,
        date_to: str | None = None,
    ) -> None:
        """Run the full pipeline."""
        # Step 1: Extract links from daily notes
        logger.info("Scanning daily notes for links...")
        files = self.scanner.scan(date_from=date_from, date_to=date_to)
        logger.info(f"Found {len(files)} daily note files")

        new_links = 0
        for file_path in files:
            file_hash = self._file_hash(file_path)

            if skip_existing and not self.db.file_needs_processing(
                str(file_path), file_hash
            ):
                continue

            links = self.parser.parse_file(file_path)
            for link in links:
                if not self.db.link_exists(link.url):
                    self.db.insert_link(link)
                    new_links += 1

            self.db.mark_file_processed(str(file_path), file_hash)

        logger.info(f"Extracted {new_links} new links")

        # Step 2: Fetch web pages
        if fetch:
            await self._fetch_links()

        # Step 3: Summarize content
        if summarize:
            await self._summarize_links()

        # Step 4: Auto-tag
        if tag:
            await self._tag_links()

        # Print stats
        stats = self.db.get_stats()
        logger.info(
            f"Database stats: {stats['total_links']} total, "
            f"{stats['fetched']} fetched, {stats['summarized']} summarized, "
            f"{stats['tagged']} tagged"
        )

    async def _fetch_links(self) -> None:
        """Fetch unfetched links."""
        links = self.db.get_unfetched_links(limit=self.config.batch_size)
        if not links:
            logger.info("No unfetched links")
            return

        logger.info(f"Fetching {len(links)} links...")

        for link in links:
            # Check if it's a PDF
            if self.fetcher.is_pdf(link.url):
                result = await self.pdf_extractor.extract(link.url)
                self.db.update_fetch_result(
                    link.id,  # type: ignore
                    result.status,
                    content=result.content,
                    page_title=result.title,
                    error=result.error,
                )
            else:
                result = await self.fetcher.fetch(link.url)
                content = None
                if result.content:
                    content = self.content_extractor.extract(result.content)

                self.db.update_fetch_result(
                    link.id,  # type: ignore
                    result.status,
                    content=content,
                    page_title=result.title,
                    error=result.error,
                )

            status_str = "OK" if result.status == FetchStatus.SUCCESS else result.status.value
            logger.info(f"  [{status_str}] {link.url[:60]}...")

    async def _summarize_links(self) -> None:
        """Summarize fetched links."""
        links = self.db.get_unsummarized_links(limit=self.config.batch_size)
        if not links:
            logger.info("No links to summarize")
            return

        logger.info(f"Summarizing {len(links)} links...")

        for link in links:
            # If no page content, create summary from available metadata
            if not link.page_content:
                summary = self._create_metadata_summary(link)
                if summary:
                    self.db.update_summary(link.id, summary, "metadata")  # type: ignore
                    logger.info(f"  [metadata] {link.url[:60]}...")
                continue

            try:
                summary = await self.summarizer.summarize(
                    content=link.page_content,
                    title=link.page_title or link.title,
                    description=link.description,
                    url=link.url,
                )
                self.db.update_summary(
                    link.id, summary, self.summarizer.model_name  # type: ignore
                )
                logger.info(f"  Summarized: {link.url[:60]}...")
            except Exception as e:
                logger.error(f"  Failed to summarize {link.url}: {e}")

    def _create_metadata_summary(self, link) -> str | None:
        """Create a summary from available metadata when page content is unavailable."""
        parts = []
        if link.page_title:
            parts.append(link.page_title)
        if link.description and link.description != link.page_title:
            parts.append(link.description)
        if link.title and link.title not in parts:
            parts.append(link.title)

        if not parts:
            return None
        return " - ".join(parts)

    async def _tag_links(self) -> None:
        """Auto-tag links that have content but no tags yet."""
        links = self.db.get_untagged_links(limit=self.config.batch_size)
        if not links:
            logger.info("No untagged links")
            return

        logger.info(f"Tagging {len(links)} links...")
        tagged_count = 0

        for i, link in enumerate(links):
            tags = await self.tagger.tag(link)
            for tag, confidence in tags:
                self.db.add_tag(link.id, tag, confidence, source="llm")  # type: ignore
                tagged_count += 1

            if tags:
                tag_names = [t.name for t, _ in tags]
                logger.info(f"  [{i+1}/{len(links)}] {link.url[:50]}... -> {tag_names}")
            else:
                logger.info(f"  [{i+1}/{len(links)}] {link.url[:50]}... -> no tags")

        logger.info(f"Applied {tagged_count} tags")

    def _file_hash(self, path: Path) -> str:
        """Calculate MD5 hash of file content."""
        return hashlib.md5(path.read_bytes()).hexdigest()


@click.group()
def cli() -> None:
    """Obsidian Link Extractor - Extract, summarize, and tag links from daily notes."""
    pass


@cli.command()
@click.option("--config", "-c", default="config.yaml", help="Config file path")
@click.option("--no-fetch", is_flag=True, help="Skip fetching web pages")
@click.option("--no-summarize", is_flag=True, help="Skip summarization")
@click.option("--no-tag", is_flag=True, help="Skip auto-tagging")
@click.option("--date-from", help="Start date (YYYY-MM-DD)")
@click.option("--date-to", help="End date (YYYY-MM-DD)")
def extract(
    config: str,
    no_fetch: bool,
    no_summarize: bool,
    no_tag: bool,
    date_from: str | None,
    date_to: str | None,
) -> None:
    """Extract and process links from daily notes."""
    cfg = Config.from_yaml(config)
    pipeline = LinkExtractorPipeline(cfg)
    asyncio.run(
        pipeline.run(
            fetch=not no_fetch,
            summarize=not no_summarize,
            tag=not no_tag,
            date_from=date_from,
            date_to=date_to,
        )
    )


@cli.command()
@click.argument("query")
@click.option("--config", "-c", default="config.yaml", help="Config file path")
@click.option("--limit", "-n", default=20, help="Max results")
def search(query: str, config: str, limit: int) -> None:
    """Full-text search links."""
    cfg = Config.from_yaml(config)
    db = Database(cfg.database_path)
    results = db.search(query, limit=limit)

    if not results:
        click.echo("No results found.")
        return

    click.echo(f"Found {len(results)} results:\n")
    for link in results:
        click.echo(f"[{link.source_date}] {link.title or link.description or link.url}")
        click.echo(f"  {link.url}")
        if link.summary:
            click.echo(f"  Summary: {link.summary[:100]}...")
        click.echo()


@cli.command("by-tag")
@click.argument("tag_name")
@click.option("--config", "-c", default="config.yaml", help="Config file path")
def by_tag(tag_name: str, config: str) -> None:
    """List links by tag."""
    cfg = Config.from_yaml(config)
    db = Database(cfg.database_path)
    results = db.get_links_by_tag(tag_name)

    if not results:
        click.echo(f"No links with tag '{tag_name}'")
        return

    click.echo(f"Links tagged '{tag_name}' ({len(results)}):\n")
    for link in results:
        click.echo(f"[{link.source_date}] {link.title or link.description or link.url}")
        click.echo(f"  {link.url}")
        click.echo()


@cli.command()
@click.option("--config", "-c", default="config.yaml", help="Config file path")
def tags(config: str) -> None:
    """List all tags with counts."""
    cfg = Config.from_yaml(config)
    db = Database(cfg.database_path)
    all_tags = db.get_all_tags()

    if not all_tags:
        click.echo("No tags found.")
        return

    click.echo("Tags:\n")
    for name, category, count in all_tags:
        click.echo(f"  {name} ({category}): {count} links")


@cli.command()
@click.option("--config", "-c", default="config.yaml", help="Config file path")
def stats(config: str) -> None:
    """Show database statistics."""
    cfg = Config.from_yaml(config)
    db = Database(cfg.database_path)
    s = db.get_stats()

    click.echo("Database Statistics:")
    click.echo(f"  Total links:  {s['total_links']}")
    click.echo(f"  Fetched:      {s['fetched']}")
    click.echo(f"  Summarized:   {s['summarized']}")
    click.echo(f"  Tagged:       {s['tagged']}")


@cli.command()
@click.option("--config", "-c", default="config.yaml", help="Config file path")
@click.option("--host", default="127.0.0.1", help="Host to bind")
@click.option("--port", "-p", default=5001, type=int, help="Port to bind")
@click.option("--debug/--no-debug", default=False, help="Enable debug mode")
def web(config: str, host: str, port: int, debug: bool) -> None:
    """Start the web interface."""
    from .web.app import create_app

    app = create_app(config)
    click.echo(f"Starting web interface at http://{host}:{port}")
    app.run(host=host, port=port, debug=debug)


@cli.command()
@click.option("--config", "-c", default="config.yaml", help="Config file path")
@click.option("--clear-existing", is_flag=True, help="Clear existing tags first")
@click.option("--limit", "-n", default=None, type=int, help="Limit number of links")
def retag(config: str, clear_existing: bool, limit: int | None) -> None:
    """Re-tag all links using LLM-based tagging."""
    cfg = Config.from_yaml(config)
    db = Database(cfg.database_path)
    tagger = LLMTagger(model_id=cfg.bedrock_model, region=cfg.bedrock_region)

    if clear_existing:
        click.echo("Clearing existing tags...")
        db.clear_all_tags()

    links = db.get_all_links_with_content(limit=limit)
    click.echo(f"Re-tagging {len(links)} links...")

    async def run_tagging() -> int:
        tagged_count = 0
        for i, link in enumerate(links):
            tags = await tagger.tag(link)
            for tag, confidence in tags:
                db.add_tag(link.id, tag, confidence, source="llm")  # type: ignore
                tagged_count += 1

            if tags:
                tag_names = [t.name for t, _ in tags]
                click.echo(f"  [{i+1}/{len(links)}] {link.url[:50]}... -> {tag_names}")
            else:
                click.echo(f"  [{i+1}/{len(links)}] {link.url[:50]}... -> no tags")
        return tagged_count

    tagged_count = asyncio.run(run_tagging())
    click.echo(f"\nApplied {tagged_count} tags to {len(links)} links")

    # Show tag stats
    all_tags = db.get_all_tags()
    click.echo("\nTag distribution:")
    for name, category, count in all_tags[:15]:
        click.echo(f"  {name} ({category}): {count}")


@cli.command()
@click.option("--config", "-c", default="config.yaml", help="Config file path")
@click.option("--limit", "-n", default=None, type=int, help="Limit number of links to refetch")
@click.option("--dry-run", is_flag=True, help="Show what would be refetched without doing it")
def refetch(config: str, limit: int | None, dry_run: bool) -> None:
    """Re-fetch links that have empty content."""
    cfg = Config.from_yaml(config)
    db = Database(cfg.database_path)

    links = db.get_empty_content_links(limit=limit or 1000)
    if not links:
        click.echo("No links with empty content to refetch.")
        return

    click.echo(f"Found {len(links)} links with empty content")

    if dry_run:
        click.echo("\nWould refetch:")
        for link in links[:20]:
            click.echo(f"  {link.url[:70]}...")
        if len(links) > 20:
            click.echo(f"  ... and {len(links) - 20} more")
        return

    # Reset fetch status for these links
    click.echo("Resetting fetch status...")
    for link in links:
        db.reset_fetch_status(link.id)  # type: ignore

    click.echo(f"Reset {len(links)} links. Run 'extract' to refetch them.")


if __name__ == "__main__":
    cli()
