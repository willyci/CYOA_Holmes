"""Unit tests for the Bilingual Kindle Web Reader generation."""

import json
import re
import tempfile
from pathlib import Path

from src.content.hound_story import create_hound_story
from src.exporters.kindle_web import KindleWebExporter


def test_bilingual_kindle_web_generation():
    story_en = create_hound_story("en")
    story_cn = create_hound_story("cn")
    exporter = KindleWebExporter(story_en, story_cn)

    with tempfile.TemporaryDirectory() as tmp_dir:
        dummy_en = Path(tmp_dir) / "dummy_en.epub"
        dummy_en.write_text("dummy epub content en", encoding="utf-8")
        dummy_cn = Path(tmp_dir) / "dummy_cn.epub"
        dummy_cn.write_text("dummy epub content cn", encoding="utf-8")

        web_dir = Path(tmp_dir) / "web"
        index_file = exporter.export(
            web_dir,
            epub_en_path=dummy_en,
            epub_cn_path=dummy_cn,
        )

        assert index_file.exists()
        assert (web_dir / "hound_of_the_baskervilles_en.epub").exists()
        assert (web_dir / "hound_of_the_baskervilles_cn.epub").exists()

        content = index_file.read_text(encoding="utf-8")

        # Verify e-ink Kindle optimizations
        assert "Bookerly" in content
        assert "PingFang SC" in content
        assert "transition: none !important" in content
        assert "btn-download" in content
        assert "hound_of_the_baskervilles_en.epub" in content
        assert "hound_of_the_baskervilles_cn.epub" in content

        # Verify embedded JSON story data has both EN and CN
        match = re.search(r'const STORY_DATA = ({.+?});', content)
        assert match, "Could not locate embedded STORY_DATA JSON in HTML"
        data = json.loads(match.group(1))

        assert "en" in data
        assert "cn" in data
        assert len(data["en"]["nodes"]) == 54
        assert len(data["cn"]["nodes"]) == 54

        # Verify Chinese names and English names
        assert data["en"]["start_nodes"]["watson"] == "watson_ch1_baker_street"
        assert data["cn"]["start_nodes"]["watson"] == "watson_ch1_baker_street"
        assert data["en"]["start_nodes"]["holmes"] == "holmes_ch1_baker_street"
        assert data["cn"]["start_nodes"]["holmes"] == "holmes_ch1_baker_street"
        assert data["en"]["start_nodes"]["stapleton"] == "stapleton_ch1_london"
        assert data["cn"]["start_nodes"]["stapleton"] == "stapleton_ch1_london"
        assert data["cn"]["pov_roles"]["watson"]["name"] == "约翰·H·华生医生"
        assert data["en"]["pov_roles"]["watson"]["name"] == "Dr. John H. Watson"
