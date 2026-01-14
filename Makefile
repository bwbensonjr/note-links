all: extract update

extract:
	uv run link-extractor extract

update:
	uv run link-extractor export-json

