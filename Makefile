all: extract update rss

extract:
	uv run link-extractor extract

update:
	uv run link-extractor export-json

rss:
	uv run link-extractor export-rss

tag-audit:
	uv run link-extractor tag-audit

tag-audit-stats:
	uv run link-extractor tag-audit --skip-llm

sync-tags:
	uv run link-extractor sync-tags

sync-tags-retag:
	uv run link-extractor sync-tags --retag

