all: extract update rss

extract:
	uv run link-extractor extract

update:
	uv run link-extractor export-json

rss:
	uv run link-extractor export-rss

