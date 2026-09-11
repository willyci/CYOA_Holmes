"""Converter utility for generating native Amazon Kindle formats (.azw3 and .mobi).

Leverages Amazon's `kindlegen` or Calibre's `ebook-convert` when available.
- AZW3 (Kindle Format 8 / KF8): Modern native Kindle format supporting HTML5, CSS3, CJK serif, and USB sideloading.
- MOBI (Dual Master MOBI): Hybrid format containing both MOBI 7 (legacy Kindles) and KF8 (modern Kindles).
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional


def find_converter_tool() -> tuple[Optional[str], Optional[Path]]:
    """Locates an available ebook conversion tool.

    Priority:
    1. Local project tools directory (tools/kindlegen.exe)
    2. System PATH kindlegen
    3. Calibre ebook-convert on PATH or standard install paths

    Returns:
        tuple of (tool_type, executable_path), or (None, None) if not found.
        tool_type is either 'kindlegen' or 'calibre'.
    """
    project_root = Path(__file__).resolve().parent.parent.parent
    local_kindlegen = project_root / "tools" / "kindlegen.exe"
    if local_kindlegen.exists():
        return "kindlegen", local_kindlegen

    path_kindlegen = shutil.which("kindlegen")
    if path_kindlegen:
        return "kindlegen", Path(path_kindlegen)

    ebook_convert = shutil.which("ebook-convert")
    if ebook_convert:
        return "calibre", Path(ebook_convert)

    candidates = [
        Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "Calibre2" / "ebook-convert.exe",
        Path(os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")) / "Calibre2" / "ebook-convert.exe",
        Path(os.environ.get("LOCALAPPDATA", "")) / "Calibre2" / "ebook-convert.exe",
    ]
    for c in candidates:
        if c.exists():
            return "calibre", c

    return None, None


def convert_epub_to_mobi(epub_path: Path, output_path: Optional[Path] = None) -> Optional[Path]:
    """Converts an EPUB 3 file to MOBI format.

    Args:
        epub_path: Path to the source .epub file.
        output_path: Destination path for .mobi. Defaults to same name with .mobi extension.

    Returns:
        Path to the generated .mobi file, or None if conversion failed or tool unavailable.
    """
    if output_path is None:
        output_path = epub_path.with_suffix(".mobi")

    tool_type, tool_path = find_converter_tool()
    if not tool_path:
        return None

    output_path.parent.mkdir(parents=True, exist_ok=True)

    if tool_type == "kindlegen":
        # kindlegen places output in the same folder as input when using -o filename
        cmd = [str(tool_path), str(epub_path), "-o", output_path.name]
        try:
            res = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
                timeout=120,
            )
            # kindlegen produces the file in epub_path.parent / output_path.name
            produced = epub_path.parent / output_path.name
            if res.returncode in (0, 1) and produced.exists():
                if produced.resolve() != output_path.resolve():
                    shutil.move(str(produced), str(output_path))
                return output_path
            err_msg = res.stderr.decode("utf-8", errors="replace")[:200]
            print(f"[WARN] KindleGen MOBI conversion failed (exit {res.returncode}): {err_msg}", file=sys.stderr)
        except Exception as e:
            print(f"[WARN] Error executing KindleGen MOBI conversion: {e}", file=sys.stderr)

    elif tool_type == "calibre":
        cmd = [
            str(tool_path),
            str(epub_path),
            str(output_path),
            "--mobi-file-type",
            "both",
            "--no-inline-toc",
        ]
        try:
            res = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
                timeout=120,
            )
            if res.returncode == 0 and output_path.exists():
                return output_path
            err_msg = res.stderr.decode("utf-8", errors="replace")[:200]
            print(f"[WARN] Calibre MOBI conversion failed (exit {res.returncode}): {err_msg}", file=sys.stderr)
        except Exception as e:
            print(f"[WARN] Error executing Calibre MOBI conversion: {e}", file=sys.stderr)

    return None


def convert_epub_to_azw3(epub_path: Path, output_path: Optional[Path] = None) -> Optional[Path]:
    """Converts an EPUB 3 file to AZW3 (Kindle Format 8).

    Args:
        epub_path: Path to the source .epub file.
        output_path: Destination path for .azw3. Defaults to same name with .azw3 extension.

    Returns:
        Path to the generated .azw3 file, or None if conversion failed or tool unavailable.
    """
    if output_path is None:
        output_path = epub_path.with_suffix(".azw3")

    tool_type, tool_path = find_converter_tool()
    if not tool_path:
        return None

    output_path.parent.mkdir(parents=True, exist_ok=True)

    if tool_type == "calibre":
        cmd = [
            str(tool_path),
            str(epub_path),
            str(output_path),
            "--no-inline-toc",
        ]
        try:
            res = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
                timeout=120,
            )
            if res.returncode == 0 and output_path.exists():
                return output_path
            err_msg = res.stderr.decode("utf-8", errors="replace")[:200]
            print(f"[WARN] Calibre AZW3 conversion failed (exit {res.returncode}): {err_msg}", file=sys.stderr)
        except Exception as e:
            print(f"[WARN] Error executing Calibre AZW3 conversion: {e}", file=sys.stderr)

    elif tool_type == "kindlegen":
        # Generate the dual-format file with kindlegen and copy to .azw3 destination
        temp_name = output_path.stem + ".temp.mobi"
        cmd = [str(tool_path), str(epub_path), "-o", temp_name]
        try:
            res = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
                timeout=120,
            )
            produced = epub_path.parent / temp_name
            if res.returncode in (0, 1) and produced.exists():
                if output_path.exists():
                    output_path.unlink()
                shutil.move(str(produced), str(output_path))
                return output_path
            err_msg = res.stderr.decode("utf-8", errors="replace")[:200]
            print(f"[WARN] KindleGen AZW3 conversion failed (exit {res.returncode}): {err_msg}", file=sys.stderr)
        except Exception as e:
            print(f"[WARN] Error executing KindleGen AZW3 conversion: {e}", file=sys.stderr)

    return None
