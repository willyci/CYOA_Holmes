"""Command-line interface for the Multi-POV Interactive Fiction Generator."""

import argparse
import http.server
import os
import socketserver
import sys
from pathlib import Path

from src.content.hound_story import create_hound_story
from src.exporters.epub_exporter import EpubExporter
from src.exporters.kindle_converter import (
    convert_epub_to_azw3,
    convert_epub_to_mobi,
    find_converter_tool,
)
from src.exporters.kindle_web import KindleWebExporter
from src.exporters.twee_exporter import TweeExporter
from src.graph import StoryGraphManager, GraphValidationError


# Ensure UTF-8 output on Windows terminals
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def build_all(output_dir: str = "dist") -> dict:
    """Builds all distribution targets: Bilingual Kindle Web, Offline EPUBs, AZW3, MOBI, and Twee 3."""
    dist = Path(output_dir)
    dist.mkdir(parents=True, exist_ok=True)
    web_dist = dist / "web"

    print("=" * 65)
    print("Multi-POV Interactive Fiction Generator: The Hound of the Baskervilles")
    print("Bilingual Edition: English & Chinese (The Hound of the Baskervilles)")
    print("=" * 65)

    # 1. Load and validate both English and Chinese story graphs
    print("\n[1/5] Loading story graphs and running NetworkX safety validation...")
    story_en = create_hound_story("en")
    manager_en = StoryGraphManager(story_en)
    stats_en = manager_en.validate_graph()

    story_cn = create_hound_story("cn")
    manager_cn = StoryGraphManager(story_cn)
    stats_cn = manager_cn.validate_graph()

    print(f"  [OK] English Story Graph Validated: {stats_en['total_nodes']} nodes, {stats_en['endings_count']} endings")
    print(f"  [OK] Chinese Story Graph Validated: {stats_cn['total_nodes']} nodes, {stats_cn['endings_count']} endings")
    print(f"    - Shared Canon Anchors: {', '.join(stats_en['anchors'])}")

    # 2. Export Offline EPUB 3 archives (EN & CN)
    print("\n[2/5] Compiling Offline EPUB 3 archives (English & Chinese)...")
    epub_en_path = dist / "hound_of_the_baskervilles_en.epub"
    epub_exporter_en = EpubExporter(story_en)
    epub_exporter_en.export(epub_en_path)
    epub_en_kb = epub_en_path.stat().st_size / 1024
    print(f"  [OK] English EPUB generated: {epub_en_path} ({epub_en_kb:.1f} KB)")

    epub_cn_path = dist / "hound_of_the_baskervilles_cn.epub"
    epub_exporter_cn = EpubExporter(story_cn)
    epub_exporter_cn.export(epub_cn_path)
    epub_cn_kb = epub_cn_path.stat().st_size / 1024
    print(f"  [OK] Chinese EPUB generated: {epub_cn_path} ({epub_cn_kb:.1f} KB)")
    print("    - Standard EPUB 3 + NCX fallback")
    print("    - Compatible with Send-to-Kindle, Apple Books, Kobo, and Calibre")

    # 3. Compile Native Kindle Formats (.azw3 and .mobi)
    print("\n[3/5] Compiling Native Kindle Formats (.azw3 & .mobi)...")
    tool_type, tool_path = find_converter_tool()
    azw3_en_path = None
    azw3_cn_path = None
    mobi_en_path = None
    mobi_cn_path = None

    if tool_path:
        print(f"  Using converter engine: {tool_type} ({tool_path.name})")
        # English AZW3 and MOBI
        azw3_en_path = convert_epub_to_azw3(epub_en_path, dist / "hound_of_the_baskervilles_en.azw3")
        mobi_en_path = convert_epub_to_mobi(epub_en_path, dist / "hound_of_the_baskervilles_en.mobi")
        if azw3_en_path:
            print(f"  [OK] English AZW3 generated: {azw3_en_path} ({azw3_en_path.stat().st_size / 1024:.1f} KB)")
        if mobi_en_path:
            print(f"  [OK] English MOBI generated: {mobi_en_path} ({mobi_en_path.stat().st_size / 1024:.1f} KB)")

        # Chinese AZW3 and MOBI
        azw3_cn_path = convert_epub_to_azw3(epub_cn_path, dist / "hound_of_the_baskervilles_cn.azw3")
        mobi_cn_path = convert_epub_to_mobi(epub_cn_path, dist / "hound_of_the_baskervilles_cn.mobi")
        if azw3_cn_path:
            print(f"  [OK] Chinese AZW3 generated: {azw3_cn_path} ({azw3_cn_path.stat().st_size / 1024:.1f} KB)")
        if mobi_cn_path:
            print(f"  [OK] Chinese MOBI generated: {mobi_cn_path} ({mobi_cn_path.stat().st_size / 1024:.1f} KB)")
    else:
        print("  [SKIP] Neither KindleGen nor Calibre ebook-convert found. Run tools setup to enable.")

    # 4. Export Bilingual Kindle Web Reader
    print("\n[4/5] Generating Bilingual Kindle-Optimized Web Reader...")
    web_exporter = KindleWebExporter(story_en, story_cn)
    web_path = web_exporter.export(
        web_dist,
        epub_en_path=epub_en_path,
        epub_cn_path=epub_cn_path,
        azw3_en_path=azw3_en_path,
        azw3_cn_path=azw3_cn_path,
        mobi_en_path=mobi_en_path,
        mobi_cn_path=mobi_cn_path,
    )
    web_size_kb = web_path.stat().st_size / 1024
    print(f"  [OK] Kindle Web Reader generated: {web_path} ({web_size_kb:.1f} KB)")
    print("    - Language selector at startup (English / 中文)")
    print("    - Instant mid-story language toggle preserving reading position")
    print("    - Bundled offline download links: EPUB, AZW3, and MOBI")

    # 5. Export Twee 3 (EN & CN)
    print("\n[5/5] Generating Twee 3 source files for Twine/Tweego...")
    twee_en_path = dist / "hound_of_the_baskervilles_en.twee"
    TweeExporter(story_en).export(twee_en_path)
    print(f"  [OK] English Twee 3 file: {twee_en_path} ({twee_en_path.stat().st_size / 1024:.1f} KB)")

    twee_cn_path = dist / "hound_of_the_baskervilles_cn.twee"
    TweeExporter(story_cn).export(twee_cn_path)
    print(f"  [OK] Chinese Twee 3 file: {twee_cn_path} ({twee_cn_path.stat().st_size / 1024:.1f} KB)")

    print("\n" + "=" * 65)
    print("BUILD COMPLETE! Targets available in ./dist/:")
    print("  1. Bilingual Web Reader:       dist/web/index.html")
    print("  2. English Offline EPUB:       dist/hound_of_the_baskervilles_en.epub")
    print("  3. Chinese Offline EPUB:       dist/hound_of_the_baskervilles_cn.epub")
    if azw3_en_path:
        print("  4. English Offline AZW3:       dist/hound_of_the_baskervilles_en.azw3")
        print("  5. Chinese Offline AZW3:       dist/hound_of_the_baskervilles_cn.azw3")
    if mobi_en_path:
        print("  6. English Offline MOBI:       dist/hound_of_the_baskervilles_en.mobi")
        print("  7. Chinese Offline MOBI:       dist/hound_of_the_baskervilles_cn.mobi")
    print("  8. English Twine Source:       dist/hound_of_the_baskervilles_en.twee")
    print("  9. Chinese Twine Source:       dist/hound_of_the_baskervilles_cn.twee")
    print("=" * 65)

    return {
        "stats_en": stats_en,
        "stats_cn": stats_cn,
        "epub_en_path": epub_en_path,
        "epub_cn_path": epub_cn_path,
        "azw3_en_path": azw3_en_path,
        "azw3_cn_path": azw3_cn_path,
        "mobi_en_path": mobi_en_path,
        "mobi_cn_path": mobi_cn_path,
        "web_path": web_path,
    }


def serve_web(port: int = 8080, directory: str = "dist/web"):
    """Starts a local HTTP server to preview the Kindle Web Reader."""
    web_dir = Path(directory)
    if not web_dir.exists() or not (web_dir / "index.html").exists():
        print(f"Directory {directory} not found. Running build first...")
        build_all()

    class QuietHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(web_dir.resolve()), **kwargs)

    print(f"\nStarting Kindle Web Preview Server at http://localhost:{port}/")
    print(f"Serving directory: {web_dir.resolve()}")
    print("Open this URL on your local PC or through your Kindle browser (on same Wi-Fi).")
    print("Press Ctrl+C to stop.")

    with socketserver.TCPServer(("", port), QuietHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")


def validate_only():
    """Validates both story graphs without building."""
    for lang in ("en", "cn"):
        story = create_hound_story(lang)
        manager = StoryGraphManager(story)
        try:
            stats = manager.validate_graph()
            print(f"[OK] {lang.upper()} Story Validation Succeeded! Total nodes: {stats['total_nodes']}")
        except GraphValidationError as e:
            print(f"[FAIL] {lang.upper()} Validation Failed:\n{e}", file=sys.stderr)
            sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Multi-POV Interactive Fiction Generator (The Hound of the Baskervilles - Bilingual)"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.add_parser("build", help="Build Web, EPUB (EN/CN), and Twee distributions")
    subparsers.add_parser("validate", help="Run NetworkX structural graph validation")

    serve_parser = subparsers.add_parser("serve", help="Launch local preview server for Kindle web reader")
    serve_parser.add_argument("--port", type=int, default=8080, help="Port to serve on (default: 8080)")

    args = parser.parse_args()

    if args.command == "build" or args.command is None:
        build_all()
    elif args.command == "validate":
        validate_only()
    elif args.command == "serve":
        serve_web(port=args.port)


if __name__ == "__main__":
    main()
