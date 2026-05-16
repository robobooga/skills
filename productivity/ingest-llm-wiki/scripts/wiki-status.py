#!/usr/bin/env python3
"""Wiki status: pending ingestions, page counts, and recent log entries."""

import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent  # scripts/ -> repo root


def find_ingested(sources_dir: Path) -> set:
    ingested = set()
    pattern = re.compile(r'\*\*Source:\*\*\s+`raw/(.+?)`')
    if sources_dir.exists():
        for page in sources_dir.glob("*.md"):
            text = page.read_text(encoding="utf-8", errors="replace")
            for match in pattern.finditer(text):
                ingested.add(match.group(1))
    return ingested


def page_counts(wiki_dir: Path) -> dict:
    folders = ["concepts", "principles", "topics", "sources", "entities", "syntheses"]
    return {
        folder: len(list((wiki_dir / folder).glob("*.md")))
        if (wiki_dir / folder).exists() else 0
        for folder in folders
    }


def recent_log(log_path: Path, n: int = 3) -> list:
    if not log_path.exists():
        return []
    entries = [line for line in log_path.read_text(encoding="utf-8").splitlines()
               if line.startswith("## [")]
    return entries[-n:]


def main():
    raw_dir = REPO / "raw"
    wiki_dir = REPO / "wiki"
    sources_dir = wiki_dir / "sources"

    raw_files = sorted(
        [f for f in raw_dir.iterdir() if f.is_file() and not f.name.startswith(".")],
        key=lambda f: f.name.lower()
    ) if raw_dir.exists() else []

    ingested = find_ingested(sources_dir)
    pending = [f for f in raw_files if f.name not in ingested]

    print("=== PENDING INGESTION ===")
    if pending:
        for f in pending:
            print(f"  {f.name}")
    else:
        print("  (none — all raw files have been ingested)")

    print("\n=== WIKI PAGE COUNTS ===")
    for folder, count in page_counts(wiki_dir).items():
        print(f"  {folder:<12}  {count}")

    print("\n=== RECENT LOG ===")
    entries = recent_log(REPO / "log.md")
    if entries:
        for entry in entries:
            print(f"  {entry}")
    else:
        print("  (log.md not found or empty)")


if __name__ == "__main__":
    main()
