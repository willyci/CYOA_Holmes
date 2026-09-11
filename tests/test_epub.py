"""Unit tests for EPUB 3 compliance, archive format, and internal hyperlinking (EN & CN)."""

import re
import tempfile
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
import pytest

from src.content.hound_story import create_hound_story
from src.exporters.epub_exporter import EpubExporter


@pytest.mark.parametrize("lang,expected_lang_code", [("en", "en"), ("cn", "zh-CN")])
def test_epub_archive_standards(lang, expected_lang_code):
    story = create_hound_story(lang)
    exporter = EpubExporter(story)

    with tempfile.TemporaryDirectory() as tmp_dir:
        epub_path = Path(tmp_dir) / f"test_book_{lang}.epub"
        exporter.export(epub_path)

        assert epub_path.exists()
        assert epub_path.stat().st_size > 10000

        with zipfile.ZipFile(epub_path, "r") as zf:
            infolist = zf.infolist()
            filenames = [info.filename for info in infolist]

            # 1. First file MUST be mimetype and uncompressed
            assert infolist[0].filename == "mimetype"
            assert infolist[0].compress_type == zipfile.ZIP_STORED
            assert zf.read("mimetype") == b"application/epub+zip"

            # 2. Required EPUB files
            assert "META-INF/container.xml" in filenames
            assert "OEBPS/content.opf" in filenames
            assert "OEBPS/nav.xhtml" in filenames
            assert "OEBPS/toc.ncx" in filenames
            assert "OEBPS/style.css" in filenames
            assert "OEBPS/title.xhtml" in filenames
            assert "OEBPS/start.xhtml" in filenames

            # 3. All passage files exist
            for node_id in story.nodes.keys():
                assert f"OEBPS/passages/{node_id}.xhtml" in filenames

            # 4. Parse XML documents to ensure well-formedness
            ET.fromstring(zf.read("META-INF/container.xml"))
            opf_root = ET.fromstring(zf.read("OEBPS/content.opf"))
            assert expected_lang_code in zf.read("OEBPS/content.opf").decode("utf-8")
            ET.fromstring(zf.read("OEBPS/nav.xhtml"))
            ET.fromstring(zf.read("OEBPS/toc.ncx"))

            # 5. Verify all internal href targets in passage XHTML files resolve to existing files
            passage_pattern = re.compile(r'href="([^"#]+)(?:#[^"]+)?"')
            for node_id in story.nodes.keys():
                content = zf.read(f"OEBPS/passages/{node_id}.xhtml").decode("utf-8")
                ET.fromstring(content)

                matches = passage_pattern.findall(content)
                for target in matches:
                    if target.startswith("http"):
                        continue
                    if target.startswith("../"):
                        target_path = f"OEBPS/{target[3:]}"
                    else:
                        target_path = f"OEBPS/passages/{target}"
                    assert target_path in filenames, (
                        f"Broken hyperlink in {node_id}.xhtml pointing to {target_path}"
                    )
