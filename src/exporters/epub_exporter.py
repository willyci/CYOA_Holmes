"""Standard EPUB 3 Interactive Fiction Exporter.

Generates an EPUB 3 archive with internal hyperlinking, validated for:
- Amazon Kindle ("Send to Kindle" and direct sideloading)
- Apple Books, Kobo, and Calibre
- EPUB 3 nav.xhtml + backwards-compatible EPUB 2 toc.ncx
"""

import html
import os
import uuid
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from src.models import NodeType, POV, PassageNode, StoryGraph


class EpubExporter:
    """Exports a StoryGraph into a valid interactive EPUB 3 e-book."""

    def __init__(self, story: StoryGraph):
        self.story = story
        self.is_cn = story.language.lower() in ("cn", "zh")
        self.lang_code = "zh-CN" if self.is_cn else "en"
        self.book_id = f"urn:uuid:{uuid.uuid5(uuid.NAMESPACE_DNS, f'cyoa.hound.{self.story.language}')}"
        self.pub_date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    def export(self, output_path: str | Path) -> Path:
        """Compiles and writes the interactive EPUB file to output_path."""
        out_file = Path(output_path)
        out_file.parent.mkdir(parents=True, exist_ok=True)

        with zipfile.ZipFile(out_file, "w") as zf:
            # 1. mimetype MUST be the first file and uncompressed (ZIP_STORED)
            zf.writestr(
                "mimetype",
                "application/epub+zip",
                compress_type=zipfile.ZIP_STORED
            )

            # 2. META-INF/container.xml
            zf.writestr(
                "META-INF/container.xml",
                self._generate_container_xml(),
                compress_type=zipfile.ZIP_DEFLATED
            )

            # 3. OEBPS/style.css
            zf.writestr(
                "OEBPS/style.css",
                self._generate_css(),
                compress_type=zipfile.ZIP_DEFLATED
            )

            # 4. Cover / Title page
            zf.writestr(
                "OEBPS/title.xhtml",
                self._generate_title_xhtml(),
                compress_type=zipfile.ZIP_DEFLATED
            )

            # 5. Starting / POV Selection page
            zf.writestr(
                "OEBPS/start.xhtml",
                self._generate_start_xhtml(),
                compress_type=zipfile.ZIP_DEFLATED
            )

            # 6. All Passage XHTML files
            for node_id, node in self.story.nodes.items():
                zf.writestr(
                    f"OEBPS/passages/{node_id}.xhtml",
                    self._generate_passage_xhtml(node),
                    compress_type=zipfile.ZIP_DEFLATED
                )

            # 7. Navigation document (EPUB 3 nav.xhtml)
            zf.writestr(
                "OEBPS/nav.xhtml",
                self._generate_nav_xhtml(),
                compress_type=zipfile.ZIP_DEFLATED
            )

            # 8. NCX Table of Contents (EPUB 2 backward compatibility)
            zf.writestr(
                "OEBPS/toc.ncx",
                self._generate_toc_ncx(),
                compress_type=zipfile.ZIP_DEFLATED
            )

            # 9. Package document (content.opf)
            zf.writestr(
                "OEBPS/content.opf",
                self._generate_content_opf(),
                compress_type=zipfile.ZIP_DEFLATED
            )

        return out_file

    def _generate_container_xml(self) -> str:
        return (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">\n'
            '  <rootfiles>\n'
            '    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>\n'
            '  </rootfiles>\n'
            '</container>'
        )

    def _generate_css(self) -> str:
        font_stack = (
            "'PingFang SC', 'Hiragino Sans GB', 'Source Han Serif SC', 'Songti SC', 'SimSun', 'Bookerly', serif"
            if self.is_cn
            else "'Bookerly', 'Georgia', 'Times New Roman', serif"
        )
        indent = "2em" if self.is_cn else "1.5em"
        line_height = "1.75" if self.is_cn else "1.6"

        return (
            "/* Interactive CYOA Stylesheet for E-Readers & Kindle */\n"
            f"body {{\n"
            f"    font-family: {font_stack};\n"
            f"    margin: 5%;\n"
            f"    line-height: {line_height};\n"
            f"    color: #111111;\n"
            f"    background-color: #ffffff;\n"
            f"}}\n"
            f"h1, h2, h3 {{\n"
            f"    font-family: {font_stack};\n"
            f"    line-height: 1.3;\n"
            f"    color: #000000;\n"
            f"    text-align: center;\n"
            f"    margin-top: 1.2em;\n"
            f"    margin-bottom: 0.6em;\n"
            f"}}\n"
            ".subtitle {\n"
            "    text-align: center;\n"
            "    font-style: italic;\n"
            "    margin-bottom: 1.5em;\n"
            "    color: #444444;\n"
            "}\n"
            ".pov-badge {\n"
            "    display: block;\n"
            "    text-align: center;\n"
            "    font-size: 0.9em;\n"
            "    font-weight: bold;\n"
            "    letter-spacing: 1px;\n"
            "    border: 1px solid #333333;\n"
            "    padding: 4px 10px;\n"
            "    margin: 0 auto 1.5em auto;\n"
            "    max-width: 320px;\n"
            "    background-color: #f4f4f4;\n"
            "}\n"
            f".content p {{\n"
            f"    text-indent: {indent};\n"
            f"    margin-top: 0;\n"
            f"    margin-bottom: 0.8em;\n"
            f"    text-align: justify;\n"
            f"}}\n"
            ".choices-heading {\n"
            "    margin-top: 2em;\n"
            "    padding-top: 0.8em;\n"
            "    border-top: 2px solid #222222;\n"
            "    font-weight: bold;\n"
            "    font-size: 1.1em;\n"
            "    text-align: center;\n"
            "    letter-spacing: 1px;\n"
            "}\n"
            ".choices-list {\n"
            "    list-style-type: none;\n"
            "    padding-left: 0;\n"
            "    margin-top: 1em;\n"
            "}\n"
            ".choice-item {\n"
            "    margin-bottom: 1.2em;\n"
            "    padding: 10px 14px;\n"
            "    border: 2px solid #222222;\n"
            "    background-color: #fafafa;\n"
            "}\n"
            ".choice-link {\n"
            "    font-weight: bold;\n"
            "    text-decoration: none;\n"
            "    color: #000000;\n"
            "    display: block;\n"
            "}\n"
            ".choice-link:hover {\n"
            "    text-decoration: underline;\n"
            "}\n"
            ".ending-box {\n"
            "    margin-top: 2em;\n"
            "    padding: 15px;\n"
            "    border: 3px double #000000;\n"
            "    background-color: #f8f8f8;\n"
            "    text-align: center;\n"
            "}\n"
            ".ending-box h3 {\n"
            "    margin-top: 0;\n"
            "}\n"
            ".clues-box {\n"
            "    margin-top: 1.5em;\n"
            "    padding: 8px 12px;\n"
            "    border-left: 3px solid #555555;\n"
            "    background-color: #f7f7f7;\n"
            "    font-size: 0.9em;\n"
            "}\n"
            ".nav-links {\n"
            "    margin-top: 2.5em;\n"
            "    padding-top: 1em;\n"
            "    border-top: 1px dashed #777777;\n"
            "    text-align: center;\n"
            "    font-size: 0.85em;\n"
            "}\n"
            ".nav-links a {\n"
            "    color: #333333;\n"
            "    margin: 0 10px;\n"
            "}\n"
        )

    def _generate_title_xhtml(self) -> str:
        safe_title = html.escape(self.story.title)
        safe_author = html.escape(self.story.author)
        safe_desc = html.escape(self.story.description)
        btn_text = "开始多视角互动调查 &#8594;" if self.is_cn else "Begin Interactive Investigation &#8594;"
        return (
            '<?xml version="1.0" encoding="utf-8"?>\n'
            f'<!DOCTYPE html>\n'
            f'<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{self.lang_code}">\n'
            '<head>\n'
            f'  <title>{safe_title}</title>\n'
            '  <link rel="stylesheet" type="text/css" href="style.css"/>\n'
            '</head>\n'
            '<body>\n'
            '  <div style="text-align:center; margin-top:20%;">\n'
            f'    <h1 style="font-size: 2em; margin-bottom: 0.3em;">{safe_title}</h1>\n'
            f'    <p class="subtitle">{safe_author}</p>\n'
            '    <hr style="width: 60%; margin: 2em auto; border: 0; border-top: 1px solid #333;"/>\n'
            f'    <p style="max-width: 80%; margin: 0 auto 2.5em auto; font-style: italic;">{safe_desc}</p>\n'
            '    <div class="choice-item" style="display:inline-block; margin: 0 auto; text-align:center;">\n'
            f'      <a class="choice-link" href="start.xhtml">{btn_text}</a>\n'
            '    </div>\n'
            '  </div>\n'
            '</body>\n'
            '</html>'
        )

    def _generate_start_xhtml(self) -> str:
        safe_title = html.escape(self.story.title)
        if self.is_cn:
            heading = "选择你的人物视角"
            sub = "穿过德文郡达特沼地的迷雾，自侦探、护卫与主谋的三重目光亲历谜案。"
            watson_title = "约翰·H·华生医生 &#8212; 实地观察与护卫侦查"
            watson_desc = "在巴斯克维尔庄园贴身保护亨利爵士，问询证人，夜探荒原。"
            holmes_title = "歇洛克·福尔摩斯 &#8212; 隐蔽监视与法网推演"
            holmes_desc = "潜伏在史前石屋据点，化验神秘化学涂层，布下苏格兰场致命杀局。"
            stapleton_title = "杰克·斯台普吞 &#8212; 幕后主谋的反派视角"
            stapleton_desc = "穿行大格林盆泥潭险道，训育发光嗜血恶犬，谋夺百万英镑家产。"
        else:
            heading = "Select Your Point of View"
            sub = "Experience the Devonshire mystery through the eyes of the investigators or the mastermind."
            watson_title = "Dr. John H. Watson &#8212; Field Observation &amp; Investigation"
            watson_desc = "Stand guard over Sir Henry at Baskerville Hall, interview suspects, and brave the moor."
            holmes_title = "Sherlock Holmes &#8212; Covert Surveillance &amp; Deduction"
            holmes_desc = "Operate incognito from the stone hut, analyze chemical traces, and orchestrate the legal trap."
            stapleton_title = "Jack Stapleton &#8212; The Antagonist"
            stapleton_desc = "Navigate the Great Grimpen Mire, groom the phosphorescent hound, and secure the Baskerville fortune."

        return (
            '<?xml version="1.0" encoding="utf-8"?>\n'
            f'<!DOCTYPE html>\n'
            f'<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{self.lang_code}">\n'
            '<head>\n'
            f'  <title>{heading} - {safe_title}</title>\n'
            '  <link rel="stylesheet" type="text/css" href="style.css"/>\n'
            '</head>\n'
            '<body>\n'
            f'  <h1>{heading}</h1>\n'
            f'  <p class="subtitle">{sub}</p>\n'
            '  <ul class="choices-list">\n'
            '    <li class="choice-item">\n'
            f'      <a class="choice-link" href="passages/{self.story.start_nodes[POV.WATSON]}.xhtml">\n'
            f'        <strong>{watson_title}</strong>\n'
            '      </a>\n'
            f'      <p style="margin: 4px 0 0 0; font-size: 0.9em; color: #444;">{watson_desc}</p>\n'
            '    </li>\n'
            '    <li class="choice-item">\n'
            f'      <a class="choice-link" href="passages/{self.story.start_nodes[POV.HOLMES]}.xhtml">\n'
            f'        <strong>{holmes_title}</strong>\n'
            '      </a>\n'
            f'      <p style="margin: 4px 0 0 0; font-size: 0.9em; color: #444;">{holmes_desc}</p>\n'
            '    </li>\n'
            '    <li class="choice-item">\n'
            f'      <a class="choice-link" href="passages/{self.story.start_nodes[POV.STAPLETON]}.xhtml">\n'
            f'        <strong>{stapleton_title}</strong>\n'
            '      </a>\n'
            f'      <p style="margin: 4px 0 0 0; font-size: 0.9em; color: #444;">{stapleton_desc}</p>\n'
            '    </li>\n'
            '  </ul>\n'
            '</body>\n'
            '</html>'
        )

    def _generate_passage_xhtml(self, node: PassageNode) -> str:
        safe_title = html.escape(node.title)
        pov_name = html.escape(node.pov.display_name(self.story.language))

        # Format paragraphs
        paragraphs = node.content.split("\n\n")
        body_html = "\n".join(f"    <p>{html.escape(p.strip())}</p>" for p in paragraphs if p.strip())

        # Clues section
        clues_html = ""
        if node.clues_discovered:
            clues_label = "案件线索与观察记录：" if self.is_cn else "Observations &amp; Clues Recorded:"
            clues_items = "".join(f"<li>{html.escape(c)}</li>" for c in node.clues_discovered)
            clues_html = (
                '  <div class="clues-box">\n'
                f'    <strong>{clues_label}</strong>\n'
                f'    <ul style="margin: 4px 0 0 1.2em; padding: 0;">{clues_items}</ul>\n'
                '  </div>\n'
            )

        # Choices or Ending box
        choices_html = ""
        if node.is_ending:
            ending_title = "~ 终局 ~" if self.is_cn else "~ The End ~"
            ending_desc = "你已在此线索分支中达成了案情终局。" if self.is_cn else "You have reached a conclusion in this interactive chronicle."
            replay_text = "&#8592; 选择其他人物视角 / 重玩" if self.is_cn else "&#8592; Choose Another Perspective / Replay"
            choices_html = (
                '  <div class="ending-box">\n'
                f'    <h3>{ending_title}</h3>\n'
                f'    <p>{ending_desc}</p>\n'
                '    <div style="margin-top: 1em;">\n'
                f'      <a class="choice-link" href="../start.xhtml" style="display:inline-block; border: 1px solid #000; padding: 6px 12px; background: #fff;">\n'
                f'        {replay_text}\n'
                '      </a>\n'
                '    </div>\n'
                '  </div>\n'
            )
        else:
            choice_heading = "决定你的下一步行动：" if self.is_cn else "What will you do?"
            choice_items = []
            for c in node.choices:
                safe_choice_text = html.escape(c.text)
                switch_tag = ""
                if c.pov_switch:
                    sw_name = html.escape(c.pov_switch.display_name(self.story.language))
                    switch_tag = f" <em>【视角切换至：{sw_name}】</em>" if self.is_cn else f" <em>[Switch to {sw_name}]</em>"

                choice_items.append(
                    '    <li class="choice-item">\n'
                    f'      <a class="choice-link" href="{c.target_node_id}.xhtml">{safe_choice_text}{switch_tag} &#8594;</a>\n'
                    '    </li>'
                )
            choices_list = "\n".join(choice_items)
            choices_html = (
                '  <div class="choices-section">\n'
                f'    <div class="choices-heading">{choice_heading}</div>\n'
                f'    <ul class="choices-list">\n{choices_list}\n    </ul>\n'
                '  </div>\n'
            )

        pov_tag_label = f"当前视角：{pov_name}" if self.is_cn else f"Perspective: {pov_name}"
        back_start_label = "&#8592; 返回视角选择" if self.is_cn else "&#8592; Return to POV Selection"
        title_page_label = "书名页" if self.is_cn else "Title Page"

        return (
            '<?xml version="1.0" encoding="utf-8"?>\n'
            f'<!DOCTYPE html>\n'
            f'<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{self.lang_code}">\n'
            '<head>\n'
            f'  <title>{safe_title}</title>\n'
            '  <link rel="stylesheet" type="text/css" href="../style.css"/>\n'
            '</head>\n'
            '<body>\n'
            f'  <div class="pov-badge">{pov_tag_label}</div>\n'
            f'  <h2>{safe_title}</h2>\n'
            f'  <div class="content">\n{body_html}\n  </div>\n'
            f'{clues_html}'
            f'{choices_html}'
            '  <div class="nav-links">\n'
            f'    <a href="../start.xhtml">{back_start_label}</a>\n'
            '    <span>&#8226;</span>\n'
            f'    <a href="../title.xhtml">{title_page_label}</a>\n'
            '  </div>\n'
            '</body>\n'
            '</html>'
        )

    def _generate_nav_xhtml(self) -> str:
        safe_title = html.escape(self.story.title)
        toc_heading = "目录" if self.is_cn else "Table of Contents"
        title_label = "书名页" if self.is_cn else "Title Page"
        start_label = "开始阅读 / 视角选择" if self.is_cn else "Start Reading / Perspective"

        chapters_toc = [
            ("ch01_part1_stick", "第一章 歇洛克·福尔摩斯先生" if self.is_cn else "Chapter 1: Mr. Sherlock Holmes"),
            ("ch02_part1_legend", "第二章 巴斯克维尔的灾祸" if self.is_cn else "Chapter 2: The Curse of the Baskervilles"),
            ("ch03_problem", "第三章 疑案" if self.is_cn else "Chapter 3: The Problem"),
            ("ch04_part1_warning", "第四章 亨利·巴斯克维尔爵士" if self.is_cn else "Chapter 4: Sir Henry Baskerville"),
            ("ch05_threads", "第五章 三条断了的线索" if self.is_cn else "Chapter 5: Three Broken Threads"),
            ("ch06_part1_arrival", "第六章 巴斯克维尔庄园" if self.is_cn else "Chapter 6: Baskerville Hall"),
            ("ch07_part1_naturalist", "第七章 梅利琵宅邸的主人斯台普吞" if self.is_cn else "Chapter 7: The Stapletons of Merripit House"),
            ("ch08_watson_report", "第八章 华生医生的第一份报告" if self.is_cn else "Chapter 8: First Report of Dr. Watson"),
            ("ch09_part1_midnight_watch", "第九章 沼地上的烛光" if self.is_cn else "Chapter 9: The Light upon the Moor"),
            ("ch10_diary_and_laura", "第十章 华生医生日记摘录" if self.is_cn else "Chapter 10: Extract from the Diary of Dr. Watson"),
            ("ch11_part1_lyons", "第十一章 岩岗上的人" if self.is_cn else "Chapter 11: The Man on the Tor"),
            ("ch12_part1_revelations", "第十二章 沼地的惨剧" if self.is_cn else "Chapter 12: Death on the Moor"),
            ("ch13_portrait", "第十三章 设网" if self.is_cn else "Chapter 13: Fixing the Nets"),
            ("ch14_part1_fog_ambush", "第十四章 巴斯克维尔的猎犬" if self.is_cn else "Chapter 14: The Hound of the Baskervilles"),
            ("ch15_victory", "第十五章 回顾" if self.is_cn else "Chapter 15: A Retrospection"),
        ]

        chapter_items = "\n".join(
            f'      <li><a href="passages/{nid}.xhtml">{html.escape(label)}</a></li>'
            for nid, label in chapters_toc
            if nid in self.story.nodes
        )

        return (
            '<?xml version="1.0" encoding="utf-8"?>\n'
            f'<!DOCTYPE html>\n'
            f'<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{self.lang_code}">\n'
            '<head>\n'
            f'  <title>{safe_title} - Navigation</title>\n'
            '  <link rel="stylesheet" type="text/css" href="style.css"/>\n'
            '</head>\n'
            '<body>\n'
            '  <nav epub:type="toc" id="toc">\n'
            f'    <h1>{toc_heading}</h1>\n'
            '    <ol>\n'
            f'      <li><a href="title.xhtml">{title_label}</a></li>\n'
            f'      <li><a href="start.xhtml">{start_label}</a></li>\n'
            f'{chapter_items}\n'
            '    </ol>\n'
            '  </nav>\n'
            '  <nav epub:type="landmarks" hidden="">\n'
            '    <h2>Landmarks</h2>\n'
            '    <ol>\n'
            '      <li><a epub:type="titlepage" href="title.xhtml">Title Page</a></li>\n'
            '      <li><a epub:type="bodymatter" href="start.xhtml">Start</a></li>\n'
            '    </ol>\n'
            '  </nav>\n'
            '</body>\n'
            '</html>'
        )

    def _generate_toc_ncx(self) -> str:
        safe_title = html.escape(self.story.title)
        safe_author = html.escape(self.story.author)
        title_label = "书名页" if self.is_cn else "Title Page"
        start_label = "开始阅读 / 视角选择" if self.is_cn else "Start Reading / Perspective"

        chapters_toc = [
            ("ch01_part1_stick", "第一章 歇洛克·福尔摩斯先生" if self.is_cn else "Chapter 1: Mr. Sherlock Holmes"),
            ("ch02_part1_legend", "第二章 巴斯克维尔的灾祸" if self.is_cn else "Chapter 2: The Curse of the Baskervilles"),
            ("ch03_problem", "第三章 疑案" if self.is_cn else "Chapter 3: The Problem"),
            ("ch04_part1_warning", "第四章 亨利·巴斯克维尔爵士" if self.is_cn else "Chapter 4: Sir Henry Baskerville"),
            ("ch05_threads", "第五章 三条断了的线索" if self.is_cn else "Chapter 5: Three Broken Threads"),
            ("ch06_part1_arrival", "第六章 巴斯克维尔庄园" if self.is_cn else "Chapter 6: Baskerville Hall"),
            ("ch07_part1_naturalist", "第七章 梅利琵宅邸的主人斯台普吞" if self.is_cn else "Chapter 7: The Stapletons of Merripit House"),
            ("ch08_watson_report", "第八章 华生医生的第一份报告" if self.is_cn else "Chapter 8: First Report of Dr. Watson"),
            ("ch09_part1_midnight_watch", "第九章 沼地上的烛光" if self.is_cn else "Chapter 9: The Light upon the Moor"),
            ("ch10_diary_and_laura", "第十章 华生医生日记摘录" if self.is_cn else "Chapter 10: Extract from the Diary of Dr. Watson"),
            ("ch11_part1_lyons", "第十一章 岩岗上的人" if self.is_cn else "Chapter 11: The Man on the Tor"),
            ("ch12_part1_revelations", "第十二章 沼地的惨剧" if self.is_cn else "Chapter 12: Death on the Moor"),
            ("ch13_portrait", "第十三章 设网" if self.is_cn else "Chapter 13: Fixing the Nets"),
            ("ch14_part1_fog_ambush", "第十四章 巴斯克维尔的猎犬" if self.is_cn else "Chapter 14: The Hound of the Baskervilles"),
            ("ch15_victory", "第十五章 回顾" if self.is_cn else "Chapter 15: A Retrospection"),
        ]

        play_order = 1
        nav_points = [
            f'    <navPoint id="np-title" playOrder="{play_order}">\n'
            f'      <navLabel><text>{title_label}</text></navLabel>\n'
            '      <content src="title.xhtml"/>\n'
            '    </navPoint>'
        ]
        play_order += 1
        nav_points.append(
            f'    <navPoint id="np-start" playOrder="{play_order}">\n'
            f'      <navLabel><text>{start_label}</text></navLabel>\n'
            '      <content src="start.xhtml"/>\n'
            '    </navPoint>'
        )

        for nid, label in chapters_toc:
            if nid in self.story.nodes:
                play_order += 1
                nav_points.append(
                    f'    <navPoint id="np-{nid}" playOrder="{play_order}">\n'
                    f'      <navLabel><text>{html.escape(label)}</text></navLabel>\n'
                    f'      <content src="passages/{nid}.xhtml"/>\n'
                    '    </navPoint>'
                )

        nav_points_xml = "\n".join(nav_points)

        return (
            '<?xml version="1.0" encoding="utf-8"?>\n'
            '<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">\n'
            '  <head>\n'
            f'    <meta name="dtb:uid" content="{self.book_id}"/>\n'
            '    <meta name="dtb:depth" content="2"/>\n'
            '    <meta name="dtb:totalPageCount" content="0"/>\n'
            '    <meta name="dtb:maxPageNumber" content="0"/>\n'
            '  </head>\n'
            f'  <docTitle><text>{safe_title}</text></docTitle>\n'
            f'  <docAuthor><text>{safe_author}</text></docAuthor>\n'
            '  <navMap>\n'
            f'{nav_points_xml}\n'
            '  </navMap>\n'
            '</ncx>'
        )

    def _generate_content_opf(self) -> str:
        safe_title = html.escape(self.story.title)
        safe_author = html.escape(self.story.author)
        safe_desc = html.escape(self.story.description)

        manifest_items = [
            '    <item id="style" href="style.css" media-type="text/css"/>',
            '    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
            '    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
            '    <item id="titlepage" href="title.xhtml" media-type="application/xhtml+xml"/>',
            '    <item id="startpage" href="start.xhtml" media-type="application/xhtml+xml"/>',
        ]

        spine_items = [
            '    <itemref idref="titlepage"/>',
            '    <itemref idref="startpage"/>',
        ]

        for node_id in self.story.nodes.keys():
            manifest_items.append(
                f'    <item id="passage_{node_id}" href="passages/{node_id}.xhtml" media-type="application/xhtml+xml"/>'
            )
            spine_items.append(f'    <itemref idref="passage_{node_id}"/>')

        manifest_xml = "\n".join(manifest_items)
        spine_xml = "\n".join(spine_items)

        return (
            '<?xml version="1.0" encoding="utf-8"?>\n'
            '<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookId" version="3.0">\n'
            '  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">\n'
            f'    <dc:identifier id="BookId">{self.book_id}</dc:identifier>\n'
            f'    <dc:title>{safe_title}</dc:title>\n'
            f'    <dc:creator>{safe_author}</dc:creator>\n'
            f'    <dc:language>{self.lang_code}</dc:language>\n'
            f'    <dc:description>{safe_desc}</dc:description>\n'
            f'    <meta property="dcterms:modified">{self.pub_date}</meta>\n'
            '  </metadata>\n'
            '  <manifest>\n'
            f'{manifest_xml}\n'
            '  </manifest>\n'
            '  <spine toc="ncx">\n'
            f'{spine_xml}\n'
            '  </spine>\n'
            '</package>'
        )
