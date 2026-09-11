"""Unit tests for the Kindle format converter (AZW3 and MOBI)."""

from pathlib import Path
import pytest
from src.exporters.kindle_converter import (
    find_converter_tool,
    convert_epub_to_azw3,
    convert_epub_to_mobi,
)


def test_converter_tool_detection():
    tool_type, tool_path = find_converter_tool()
    assert tool_type in ("kindlegen", "calibre")
    assert tool_path is not None
    assert tool_path.exists()


def test_azw3_and_mobi_conversion(tmp_path):
    epub_path = Path("dist/hound_of_the_baskervilles_en.epub")
    if not epub_path.exists():
        pytest.skip("Base English EPUB not found; run build first.")

    target_azw3 = tmp_path / "test.azw3"
    result_azw3 = convert_epub_to_azw3(epub_path, target_azw3)
    assert result_azw3 is not None
    assert result_azw3.exists()
    assert result_azw3.stat().st_size > 10000

    target_mobi = tmp_path / "test.mobi"
    result_mobi = convert_epub_to_mobi(epub_path, target_mobi)
    assert result_mobi is not None
    assert result_mobi.exists()
    assert result_mobi.stat().st_size > 10000
