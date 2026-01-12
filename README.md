# Obsidian Link Extractor

Extract, summarize, and tag links from Obsidian daily notes. Stores results in a searchable SQLite database with full-text search.

## Features

- **Link Extraction**: Parses the `## Links` section from daily notes, supporting both markdown links `[Title](url)` and bare URLs `description - https://...`
- **Web Fetching**: Async HTTP fetching with per-domain rate limiting
- **PDF Support**: Downloads and extracts text from PDF files
- **Summarization**: Generates 2-3 sentence summaries using Claude via AWS Bedrock
  - Falls back to metadata-based summaries when page content can't be extracted
- **Auto-Tagging**: LLM-based categorization (programming languages, technical topics, culture)
- **Full-Text Search**: SQLite FTS5 for fast searching across titles, descriptions, content, and summaries
- **Incremental Processing**: Only processes new/pending items on each run
- **Web Interface**: Browse and search links in a web UI

## Installation

Requires Python 3.10+ and [uv](https://github.com/astral-sh/uv).

```bash
uv sync
```

## Configuration

### Environment Variables (.env)

Create a `.env` file in the project root (see `.env.example`):

```bash
# Required: Path to directory containing daily notes (YYYY-MM-DD.md files)
DAILY_NOTES_PATH=/path/to/your/daily/notes

# Optional: Path to SQLite database (defaults to ./links.db)
DATABASE_PATH=./links.db
```

### Additional Settings (config.yaml)

Other settings can be configured in `config.yaml`:

```yaml
database_path: ./links.db
rate_limit_per_second: 1.0
fetch_timeout_seconds: 30
bedrock_model: us.anthropic.claude-3-5-sonnet-20241022-v2:0
bedrock_region: us-east-1
batch_size: 50
```

Environment variables take precedence over `config.yaml` values.

### AWS Credentials

Ensure AWS credentials are configured for Bedrock access (for summarization and tagging features).

## Usage

### Extract links from daily notes

```bash
# Full pipeline: extract, fetch, summarize, tag
uv run link-extractor extract

# Extract from specific date range
uv run link-extractor extract --date-from 2025-01-01 --date-to 2025-12-31

# Skip summarization (faster, no API costs)
uv run link-extractor extract --no-summarize

# Skip fetching (just extract URLs from markdown)
uv run link-extractor extract --no-fetch
```

### Re-fetch and re-tag

```bash
# Re-fetch links that have empty content (e.g., after fixing extraction bugs)
uv run link-extractor refetch --dry-run  # Preview what would be refetched
uv run link-extractor refetch            # Reset links, then run extract

# Re-tag all links using LLM
uv run link-extractor retag --clear-existing
```

### Search and query

```bash
# Full-text search
uv run link-extractor search "rust compiler"

# List links by tag
uv run link-extractor by-tag python
uv run link-extractor by-tag llm

# Show all tags with counts
uv run link-extractor tags

# Database statistics
uv run link-extractor stats
```

### Web interface

```bash
uv run link-extractor web              # Start at http://127.0.0.1:5000
uv run link-extractor web --port 8080  # Custom port
```

## Project Structure

```
note-links/
├── .env                        # Local configuration (not committed)
├── .env.example                # Example environment variables
├── config.yaml                 # Runtime configuration
├── pyproject.toml              # Dependencies and CLI entry point
├── links.db                    # SQLite database (created on first run)
├── src/link_extractor/
│   ├── main.py                 # CLI and pipeline orchestration
│   ├── config.py               # Configuration loading (.env + YAML)
│   ├── extraction/
│   │   ├── parser.py           # Markdown link parsing
│   │   └── scanner.py          # Daily notes directory traversal
│   ├── fetching/
│   │   ├── fetcher.py          # Async HTTP with rate limiting
│   │   ├── content.py          # HTML text extraction
│   │   └── pdf.py              # PDF text extraction
│   ├── summarization/
│   │   ├── base.py             # Abstract summarizer interface
│   │   └── bedrock.py          # AWS Bedrock Claude implementation
│   ├── tagging/
│   │   └── llm_tagger.py       # LLM-based auto-tagging via Bedrock
│   ├── storage/
│   │   ├── models.py           # Dataclasses (ExtractedLink, LinkRecord, Tag)
│   │   └── database.py         # SQLite operations with FTS5
│   └── web/
│       ├── app.py              # Flask app factory
│       ├── routes.py           # Web routes
│       └── templates/          # HTML templates
└── tests/
```

## Tag Categories

Tags are auto-assigned by the LLM based on page content:

- **Programming Languages**: python, rust, typescript, javascript, go, etc.
- **Technical Topics**: compilers, ai, llm, databases, web-development, etc.
- **Culture**: tv, movie, fiction-book, nonfiction-book, music, etc.

## Daily Note Format

The extractor looks for a `## Links` section in daily notes:

```markdown
## Links
- Description of link - https://example.com
- [Article Title](https://example.com/article) by Author Name
  - [Nested link](https://example.com/related)
```

## Database

Links are stored in SQLite with FTS5 full-text search. The database file (`links.db`) contains:

- `links` - Main table with URL, title, description, content, summary
- `tags` - Tag definitions with categories
- `link_tags` - Link-tag associations with confidence scores
- `links_fts` - Full-text search index

Query the database directly:

```bash
sqlite3 links.db "SELECT url, summary FROM links WHERE summary IS NOT NULL LIMIT 5"

# Full-text search
sqlite3 links.db "SELECT url FROM links_fts WHERE links_fts MATCH 'rust AND compiler'"
```
