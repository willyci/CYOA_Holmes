"""Kindle Web Browser Exporter (Bilingual: English & Chinese).

Generates an interactive, zero-dependency web reader specifically engineered for
the Amazon Kindle e-ink web browser (and modern browsers):
- Language picker at start (English / 中文)
- Instant language toggle mid-story (preserves current scene and clues)
- High-contrast monochrome typography (Bookerly / CJK Serif stack)
- Zero animations / zero motion blur to eliminate e-ink ghosting
- Large, tactile tap targets (>50px) with instant inverted tap feedback
- In-page navigation history ('Return to previous scene')
- Font sizing controls (A- / A+) and High-Contrast E-Ink mode
- Direct download buttons for both English and Chinese offline EPUBs
- Embedded complete English and Chinese story graphs in JSON for 100% offline client-side execution
"""

import html
import json
import shutil
from pathlib import Path

from src.models import StoryGraph


class KindleWebExporter:
    """Exports English and Chinese StoryGraphs into a unified Kindle-optimized web reader."""

    def __init__(self, story_en: StoryGraph, story_cn: StoryGraph):
        self.story_en = story_en
        self.story_cn = story_cn

    def export(
        self,
        output_dir: str | Path,
        epub_en_path: str | Path | None = None,
        epub_cn_path: str | Path | None = None,
        azw3_en_path: str | Path | None = None,
        azw3_cn_path: str | Path | None = None,
        mobi_en_path: str | Path | None = None,
        mobi_cn_path: str | Path | None = None,
    ) -> Path:
        """Generates the static web bundle in output_dir.

        Copies EPUB, AZW3, and MOBI files into the output directory so they are directly downloadable.
        """
        out_dir = Path(output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)

        # Copy ebook files if available
        files_to_copy = [
            (epub_en_path, "hound_of_the_baskervilles_en.epub"),
            (epub_cn_path, "hound_of_the_baskervilles_cn.epub"),
            (azw3_en_path, "hound_of_the_baskervilles_en.azw3"),
            (azw3_cn_path, "hound_of_the_baskervilles_cn.azw3"),
            (mobi_en_path, "hound_of_the_baskervilles_en.mobi"),
            (mobi_cn_path, "hound_of_the_baskervilles_cn.mobi"),
        ]
        for src_path, target_name in files_to_copy:
            if src_path and Path(src_path).exists():
                shutil.copy2(src_path, out_dir / target_name)

        # Generate HTML
        index_html_content = self._generate_html()
        index_file = out_dir / "index.html"
        index_file.write_text(index_html_content, encoding="utf-8")

        return index_file

    def _story_to_dict(self, story: StoryGraph) -> dict:
        lang = story.language
        return {
            "title": story.title,
            "author": story.author,
            "description": story.description,
            "start_nodes": {pov.value: node_id for pov, node_id in story.start_nodes.items()},
            "pov_roles": {
                pov.value: {
                    "name": pov.display_name(lang),
                    "description": pov.role_description(lang),
                }
                for pov in story.start_nodes.keys()
            },
            "nodes": {
                node_id: {
                    "id": node.id,
                    "title": node.title,
                    "pov": node.pov.value,
                    "pov_name": node.pov.display_name(lang),
                    "node_type": node.node_type.value,
                    "anchor_name": node.anchor_name,
                    "content": node.content,
                    "is_ending": node.is_ending,
                    "clues": node.clues_discovered,
                    "choices": [
                        {
                            "id": c.id,
                            "text": c.text,
                            "target": c.target_node_id,
                            "pov_switch": c.pov_switch.value if c.pov_switch else None,
                            "pov_switch_name": c.pov_switch.display_name(lang) if c.pov_switch else None,
                        }
                        for c in node.choices
                    ],
                }
                for node_id, node in story.nodes.items()
            },
        }

    def _generate_html(self) -> str:
        bilingual_data = {
            "en": self._story_to_dict(self.story_en),
            "cn": self._story_to_dict(self.story_cn),
        }
        story_json = json.dumps(bilingual_data, ensure_ascii=False)

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Hound of the Baskervilles / 巴斯克维尔的猎犬 - CYOA</title>
  <style>
    /* =========================================================================
       KINDLE E-INK OPTIMIZED STYLESHEET
       Strict high contrast, no transitions/animations, book serif typography
       ========================================================================= */
    * {{
      box-sizing: border-box;
      -webkit-tap-highlight-color: transparent;
      transition: none !important;
      animation: none !important;
    }}

    :root {{
      --bg: #ffffff;
      --text: #000000;
      --card-bg: #f7f7f7;
      --card-border: #000000;
      --secondary-text: #333333;
      --font-scale: 1.0;
    }}

    body.dark-mode {{
      --bg: #000000;
      --text: #ffffff;
      --card-bg: #1a1a1a;
      --card-border: #ffffff;
      --secondary-text: #cccccc;
    }}

    body {{
      font-family: "Bookerly", "PingFang SC", "Hiragino Sans GB", "Source Han Serif SC", "Songti SC", "SimSun", "Caecilia", "Georgia", serif;
      font-size: calc(18px * var(--font-scale));
      line-height: 1.65;
      background-color: var(--bg);
      color: var(--text);
      margin: 0;
      padding: 0;
    }}

    .container {{
      max-width: 740px;
      margin: 0 auto;
      padding: 10px 16px 60px 16px;
    }}

    /* Header Bar */
    header {{
      border-bottom: 2px solid var(--text);
      padding: 8px 0;
      margin-bottom: 16px;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 8px;
    }}

    .header-title {{
      font-size: calc(14px * var(--font-scale));
      font-weight: bold;
      letter-spacing: 0.5px;
    }}

    .header-controls {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      align-items: center;
    }}

    /* Buttons */
    button, .btn {{
      font-family: inherit;
      font-size: calc(14px * var(--font-scale));
      font-weight: bold;
      color: var(--text);
      background-color: var(--bg);
      border: 2px solid var(--text);
      padding: 6px 10px;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      user-select: none;
      min-height: 38px;
    }}

    button:active, .btn:active, button.selected {{
      background-color: var(--text);
      color: var(--bg);
    }}

    .btn-download {{
      border: 2px solid var(--text);
      background-color: var(--card-bg);
      font-size: calc(13px * var(--font-scale));
      padding: 6px 8px;
    }}

    /* Language Selection Banner */
    .lang-banner {{
      border: 2px solid var(--text);
      background-color: var(--card-bg);
      padding: 14px;
      margin-bottom: 20px;
      text-align: center;
    }}

    .lang-btn-group {{
      display: flex;
      gap: 12px;
      justify-content: center;
      margin-top: 10px;
    }}

    .lang-btn-group button {{
      min-width: 140px;
      padding: 10px 16px;
      font-size: calc(16px * var(--font-scale));
    }}

    /* POV Indicator */
    .pov-indicator {{
      border: 1px solid var(--text);
      padding: 6px 10px;
      margin-bottom: 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background-color: var(--card-bg);
      font-size: calc(14px * var(--font-scale));
      letter-spacing: 0.5px;
    }}

    .anchor-tag {{
      border: 1px solid var(--text);
      padding: 2px 6px;
      font-size: 0.8em;
      font-weight: bold;
    }}

    /* Prose */
    h1.story-title {{
      font-size: calc(24px * var(--font-scale));
      text-align: center;
      margin: 16px 0 6px 0;
      line-height: 1.25;
    }}

    .story-subtitle {{
      text-align: center;
      font-style: italic;
      color: var(--secondary-text);
      margin-bottom: 20px;
      font-size: calc(15px * var(--font-scale));
    }}

    h2.scene-title {{
      font-size: calc(22px * var(--font-scale));
      margin: 12px 0 16px 0;
      line-height: 1.3;
      border-bottom: 1px solid var(--text);
      padding-bottom: 6px;
    }}

    .prose p {{
      text-indent: 2em;
      margin: 0 0 14px 0;
      text-align: justify;
    }}

    /* Clues Box (Collapsible) */
    .clues-panel {{
      border: 2px dashed var(--text);
      margin: 20px 0;
      background-color: var(--card-bg);
      font-size: calc(14px * var(--font-scale));
    }}

    .clues-toggle-btn {{
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: transparent;
      border: none;
      color: var(--text);
      font-family: inherit;
      font-size: calc(14px * var(--font-scale));
      padding: 10px 14px;
      cursor: pointer;
      text-align: left;
      min-height: 48px;
    }}

    .clues-toggle-btn:hover,
    .clues-toggle-btn:focus {{
      background-color: var(--card-bg);
      outline: 1px dotted var(--text);
    }}

    .clues-title {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .clues-icon {{
      font-size: 1.1em;
      display: inline-block;
      width: 1.2em;
    }}

    .clues-hint {{
      font-size: 0.85em;
      opacity: 0.8;
      font-style: italic;
    }}

    .clues-content {{
      padding: 4px 14px 12px 14px;
      border-top: 1px dashed var(--text);
    }}

    .clues-content ul {{
      margin: 6px 0 0 18px;
      padding: 0;
    }}

    .clues-content li {{
      margin-bottom: 6px;
      line-height: 1.5;
    }}

    /* Choices */
    .choices-section {{
      margin-top: 24px;
      border-top: 2px solid var(--text);
      padding-top: 14px;
    }}

    .choices-header {{
      font-weight: bold;
      letter-spacing: 0.5px;
      margin-bottom: 12px;
      font-size: calc(15px * var(--font-scale));
    }}

    .choice-card {{
      display: block;
      width: 100%;
      text-align: left;
      margin-bottom: 14px;
      padding: 14px 16px;
      border: 2px solid var(--card-border);
      background-color: var(--card-bg);
      color: var(--text);
      font-size: calc(17px * var(--font-scale));
      line-height: 1.45;
      cursor: pointer;
      min-height: 52px;
    }}

    .choice-card:active {{
      background-color: var(--text);
      color: var(--bg);
    }}

    .pov-switch-notice {{
      display: inline-block;
      font-size: 0.85em;
      font-style: italic;
      margin-top: 4px;
      border-top: 1px dashed var(--secondary-text);
      padding-top: 4px;
      width: 100%;
    }}

    /* Ending */
    .ending-card {{
      border: 3px double var(--text);
      padding: 20px;
      margin: 24px 0;
      background-color: var(--card-bg);
      text-align: center;
    }}

    .ending-card h3 {{
      margin-top: 0;
      font-size: calc(22px * var(--font-scale));
    }}

    /* POV Cards */
    .pov-picker {{
      display: flex;
      flex-direction: column;
      gap: 16px;
      margin-top: 20px;
    }}

    .pov-card {{
      border: 2px solid var(--text);
      padding: 16px;
      background-color: var(--card-bg);
      cursor: pointer;
      text-align: left;
    }}

    .pov-card:active {{
      background-color: var(--text);
      color: var(--bg);
    }}

    .pov-card h3 {{
      margin: 0 0 6px 0;
      font-size: calc(19px * var(--font-scale));
    }}

    .pov-card p {{
      margin: 0;
      font-size: calc(15px * var(--font-scale));
      color: var(--secondary-text);
    }}

    .bottom-nav {{
      margin-top: 30px;
      padding-top: 12px;
      border-top: 1px solid var(--secondary-text);
      display: flex;
      justify-content: space-between;
      gap: 10px;
      font-size: calc(14px * var(--font-scale));
    }}

    /* Download Section */
    .download-section {{
      margin-top: 28px;
      border: 2px solid var(--text);
      padding: 16px;
      background-color: var(--card-bg);
    }}

    .download-section h3 {{
      margin-top: 0;
      margin-bottom: 12px;
      font-size: calc(18px * var(--font-scale));
      border-bottom: 1px solid var(--text);
      padding-bottom: 6px;
    }}

    .download-grid {{
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}

    .download-card {{
      border: 1px solid var(--text);
      padding: 12px;
      background-color: var(--bg);
    }}

    .format-badge {{
      display: inline-block;
      font-weight: bold;
      font-size: calc(12px * var(--font-scale));
      border: 1px solid var(--text);
      padding: 2px 6px;
      margin-bottom: 6px;
      background-color: var(--text);
      color: var(--bg);
    }}

    .download-card p {{
      margin: 4px 0 8px 0;
      font-size: calc(14px * var(--font-scale));
      color: var(--secondary-text);
    }}

    .btn-group {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }}
  </style>
</head>
<body>

  <div class="container">
    <!-- Top Header -->
    <header>
      <div class="header-title" id="app-heading">Baskerville CYOA</div>
      <div class="header-controls">
        <button id="btn-lang" title="Toggle Language (English / 中文)">中 / EN</button>
        <button id="btn-font-down" title="Decrease font" aria-label="Decrease font">A-</button>
        <button id="btn-font-up" title="Increase font" aria-label="Increase font">A+</button>
        <button id="btn-contrast" title="Toggle High Contrast / Dark mode">Contrast</button>
        <a id="link-azw3" href="hound_of_the_baskervilles_en.azw3" class="btn btn-download" download title="Download AZW3 for Kindle (USB Sideload)">
          &#8595; AZW3
        </a>
        <a id="link-epub" href="hound_of_the_baskervilles_en.epub" class="btn btn-download" download title="Download EPUB (Send to Kindle / Kobo)">
          &#8595; EPUB
        </a>
        <a id="link-mobi" href="hound_of_the_baskervilles_en.mobi" class="btn btn-download" download title="Download MOBI (Legacy Kindle)">
          &#8595; MOBI
        </a>
      </div>
    </header>

    <!-- Main View -->
    <main id="app-root">
      <!-- Dynamic rendering via JS -->
    </main>
  </div>

  <script>
    // Embedded Bilingual Story Graphs
    const STORY_DATA = {story_json};

    // State
    const state = {{
      lang: "en",               // "en" or "cn"
      currentView: "home",      // "home" or "scene"
      currentNodeId: null,
      currentPOV: null,
      history: [],
      cluesDiscovered: new Set(),
      fontScale: 1.0,
      isDark: false
    }};

    // DOM Elements
    const root = document.getElementById("app-root");
    const heading = document.getElementById("app-heading");
    const langBtn = document.getElementById("btn-lang");

    function getStory() {{
      return STORY_DATA[state.lang];
    }}

    function setLanguage(newLang) {{
      state.lang = newLang;
      langBtn.textContent = state.lang === "en" ? "中文版" : "English";

      // Update header download links to current language
      const azw3Link = document.getElementById("link-azw3");
      const epubLink = document.getElementById("link-epub");
      const mobiLink = document.getElementById("link-mobi");
      if (azw3Link) azw3Link.href = `hound_of_the_baskervilles_${{state.lang}}.azw3`;
      if (epubLink) epubLink.href = `hound_of_the_baskervilles_${{state.lang}}.epub`;
      if (mobiLink) mobiLink.href = `hound_of_the_baskervilles_${{state.lang}}.mobi`;

      if (state.currentView === "home") {{
        renderHome();
      }} else if (state.currentView === "scene" && state.currentNodeId) {{
        const node = getStory().nodes[state.currentNodeId];
        if (node) {{
          renderScene(node);
        }} else {{
          renderHome();
        }}
      }}
    }}

    // Header Event Listeners
    langBtn.addEventListener("click", () => {{
      setLanguage(state.lang === "en" ? "cn" : "en");
    }});

    document.getElementById("btn-font-up").addEventListener("click", () => {{
      if (state.fontScale < 1.6) {{
        state.fontScale += 0.15;
        document.documentElement.style.setProperty("--font-scale", state.fontScale.toFixed(2));
      }}
    }});

    document.getElementById("btn-font-down").addEventListener("click", () => {{
      if (state.fontScale > 0.75) {{
        state.fontScale -= 0.15;
        document.documentElement.style.setProperty("--font-scale", state.fontScale.toFixed(2));
      }}
    }});

    document.getElementById("btn-contrast").addEventListener("click", () => {{
      state.isDark = !state.isDark;
      document.body.classList.toggle("dark-mode", state.isDark);
    }});

    // Rendering
    function renderHome() {{
      state.currentView = "home";
      const story = getStory();
      const isCn = state.lang === "cn";

      heading.textContent = isCn ? "巴斯克维尔的猎犬" : "Baskerville CYOA";

      const langBannerHtml = `
        <div class="lang-banner">
          <strong>Language / 语言选择:</strong>
          <div class="lang-btn-group">
            <button class="${{state.lang === 'en' ? 'selected' : ''}}" onclick="setLanguage('en')">English</button>
            <button class="${{state.lang === 'cn' ? 'selected' : ''}}" onclick="setLanguage('cn')">中文版</button>
          </div>
        </div>
      `;

      const startBtnHtml = `
        <div style="text-align: center; margin: 20px 0 24px 0;">
          <button class="choice-card" onclick="startStory('watson')" style="font-size: 1.15em; font-weight: bold; padding: 16px; border: 2px solid var(--text); background: var(--text); color: var(--bg); cursor: pointer; display: block; width: 100%;">
            ${{isCn ? "▶ 立即开始阅读第一章 (Chapter 1)" : "▶ Start Reading from Chapter 1"}}
          </button>
        </div>
      `;

      const einkNoteHtml = isCn
        ? `
          <div style="border: 2px solid var(--text); padding: 12px; margin-bottom: 20px; background-color: var(--card-bg);">
            <strong>Kindle 墨水屏阅读模式已就绪：</strong>
            <p style="margin: 6px 0 0 0; font-size: 0.9em;">
              专为 Kindle 原生浏览器调优：高对比度黑白排版、零延迟无动画渲染、超大触控按键。
              涵盖原著全15章经典宏篇，每章保留数千字详尽内容，您可在线沉浸阅读或下载离线电子书。
            </p>
          </div>
          ${{startBtnHtml}}
          <h2 style="text-align: center; margin-top: 10px;">选择探索视角（全15章）</h2>
        `
        : `
          <div style="border: 2px solid var(--text); padding: 12px; margin-bottom: 20px; background-color: var(--card-bg);">
            <strong>Kindle E-Reader Mode Active:</strong>
            <p style="margin: 6px 0 0 0; font-size: 0.9em;">
              Optimized for e-ink web browsers with zero motion lag, large tap targets, and high contrast.
              Featuring all 15 canonical chapters with extensive authentic prose. Read online or download offline e-books.
            </p>
          </div>
          ${{startBtnHtml}}
          <h2 style="text-align: center; margin-top: 10px;">Select Perspective (15 Chapters)</h2>
        `;

      const povRoles = story.pov_roles;
      const povCardsHtml = `
        <div class="pov-picker">
          <div class="pov-card" onclick="startStory('watson')">
            <h3>${{escapeHtml(povRoles.watson.name)}}</h3>
            <p>${{escapeHtml(povRoles.watson.description)}}</p>
          </div>
          <div class="pov-card" onclick="startStory('holmes')">
            <h3>${{escapeHtml(povRoles.holmes.name)}}</h3>
            <p>${{escapeHtml(povRoles.holmes.description)}}</p>
          </div>
          <div class="pov-card" onclick="startStory('stapleton')">
            <h3>${{escapeHtml(povRoles.stapleton.name)}}</h3>
            <p>${{escapeHtml(povRoles.stapleton.description)}}</p>
          </div>
        </div>
      `;

      const downloadsHtml = isCn
        ? `
          <div class="download-section">
            <h3>离线电子书文件下载（三种格式）：</h3>
            <div class="download-grid">
              <div class="download-card">
                <span class="format-badge">AZW3 (KF8)</span>
                <strong>现代 Kindle USB 数据线直传（最推荐）</strong>
                <p>支持现代衬线字体、宋体/黑体排版与无缝超链接选择跳转。连接电脑后直接拷贝至 Kindle 的 <code>documents</code> 文件夹即可阅读。</p>
                <div class="btn-group">
                  <a href="hound_of_the_baskervilles_cn.azw3" class="btn" download>&#8595; 下载中文版 AZW3</a>
                  <a href="hound_of_the_baskervilles_en.azw3" class="btn" download>&#8595; Download English AZW3</a>
                </div>
              </div>
              <div class="download-card">
                <span class="format-badge">EPUB 3</span>
                <strong>Send-to-Kindle 邮件与网页推送（官方推荐）</strong>
                <p>亚马逊官方无线推送标准格式。通过 amazon.com/sendtokindle 上传或直接发送邮件至 @kindle.com，亚马逊将自动同步至设备。同时兼容 Apple Books、Kobo 等。</p>
                <div class="btn-group">
                  <a href="hound_of_the_baskervilles_cn.epub" class="btn" download>&#8595; 下载中文版 EPUB</a>
                  <a href="hound_of_the_baskervilles_en.epub" class="btn" download>&#8595; Download English EPUB</a>
                </div>
              </div>
              <div class="download-card">
                <span class="format-badge">MOBI</span>
                <strong>早期旧款 Kindle 专用格式</strong>
                <p>针对 Kindle 1-3 代、Kindle Keyboard、Kindle DX 等老旧机型兼容设计，可通过 USB 导入。</p>
                <div class="btn-group">
                  <a href="hound_of_the_baskervilles_cn.mobi" class="btn" download>&#8595; 下载中文版 MOBI</a>
                  <a href="hound_of_the_baskervilles_en.mobi" class="btn" download>&#8595; Download English MOBI</a>
                </div>
              </div>
            </div>
          </div>
        `
        : `
          <div class="download-section">
            <h3>Offline E-Book Downloads (Three Formats Available):</h3>
            <div class="download-grid">
              <div class="download-card">
                <span class="format-badge">AZW3 (KF8)</span>
                <strong>Best for Modern Kindle USB Sideload (Recommended)</strong>
                <p>Modern Kindle Format 8 with high-resolution typography, Bookerly serif font, and interactive choice links. Copy directly to your Kindle's <code>documents</code> folder via USB.</p>
                <div class="btn-group">
                  <a href="hound_of_the_baskervilles_en.azw3" class="btn" download>&#8595; Download English AZW3</a>
                  <a href="hound_of_the_baskervilles_cn.azw3" class="btn" download>&#8595; 下载中文版 AZW3</a>
                </div>
              </div>
              <div class="download-card">
                <span class="format-badge">EPUB 3</span>
                <strong>Best for Send-to-Kindle (Wireless / Email)</strong>
                <p>Amazon's official format for wireless sync. Upload via amazon.com/sendtokindle or email to your @kindle.com address. Also compatible with Apple Books and Kobo.</p>
                <div class="btn-group">
                  <a href="hound_of_the_baskervilles_en.epub" class="btn" download>&#8595; Download English EPUB</a>
                  <a href="hound_of_the_baskervilles_cn.epub" class="btn" download>&#8595; 下载中文版 EPUB</a>
                </div>
              </div>
              <div class="download-card">
                <span class="format-badge">MOBI</span>
                <strong>For Legacy Older Kindle Models</strong>
                <p>Compatible with vintage Kindle models (Kindle 1-3, Keyboard, DX) using direct USB file transfer.</p>
                <div class="btn-group">
                  <a href="hound_of_the_baskervilles_en.mobi" class="btn" download>&#8595; Download English MOBI</a>
                  <a href="hound_of_the_baskervilles_cn.mobi" class="btn" download>&#8595; 下载中文版 MOBI</a>
                </div>
              </div>
            </div>
          </div>
        `;

      root.innerHTML = `
        ${{langBannerHtml}}
        <h1 class="story-title">${{escapeHtml(story.title)}}</h1>
        <p class="story-subtitle">${{escapeHtml(story.author)}}</p>
        <p style="text-align: center; margin-bottom: 24px;">${{escapeHtml(story.description)}}</p>
        ${{einkNoteHtml}}
        ${{povCardsHtml}}
        ${{downloadsHtml}}
      `;
      window.scrollTo(0, 0);
    }}

    function startStory(pov) {{
      state.currentPOV = pov;
      state.history = [];
      state.cluesDiscovered.clear();
      const startNodeId = getStory().start_nodes[pov];
      goToNode(startNodeId);
    }}

    function goToNode(nodeId, isBack = false) {{
      const story = getStory();
      const node = story.nodes[nodeId];
      if (!node) {{
        console.error("Node not found:", nodeId);
        return;
      }}

      if (!isBack && state.currentNodeId) {{
        state.history.push(state.currentNodeId);
      }}

      state.currentNodeId = nodeId;
      state.currentPOV = node.pov;
      state.currentView = "scene";

      if (node.clues && node.clues.length > 0) {{
        node.clues.forEach(c => state.cluesDiscovered.add(c));
      }}

      renderScene(node);
      window.scrollTo(0, 0);
    }}

    function goBack() {{
      if (state.history.length > 0) {{
        const prevId = state.history.pop();
        goToNode(prevId, true);
      }} else {{
        renderHome();
      }}
    }}

    function toggleClues() {{
      const content = document.getElementById("clues-content");
      const icon = document.getElementById("clues-icon");
      const hint = document.getElementById("clues-hint");
      const btn = document.getElementById("clues-toggle-btn");
      if (!content) return;

      const isHidden = content.style.display === "none";
      if (isHidden) {{
        content.style.display = "block";
        if (icon) icon.innerHTML = "&#9662;";
        if (hint) hint.textContent = state.lang === "cn" ? "（点击收起）" : "(click to collapse)";
        if (btn) btn.setAttribute("aria-expanded", "true");
      }} else {{
        content.style.display = "none";
        if (icon) icon.innerHTML = "&#9656;";
        if (hint) hint.textContent = state.lang === "cn" ? "（点击展开）" : "(click to expand)";
        if (btn) btn.setAttribute("aria-expanded", "false");
      }}
    }}

    function renderScene(node) {{
      const isCn = state.lang === "cn";
      heading.textContent = isCn ? `当前视角：${{node.pov_name}}` : `POV: ${{node.pov_name}}`;

      const paragraphs = node.content.split("\\n\\n")
        .map(p => `<p>${{escapeHtml(p.trim())}}</p>`)
        .join("");

      let cluesHtml = "";
      if (state.cluesDiscovered.size > 0) {{
        const cluesList = Array.from(state.cluesDiscovered)
          .map(c => `<li>${{escapeHtml(c)}}</li>`)
          .join("");
        const cluesTitle = isCn
          ? `案件侦查线索 (${{state.cluesDiscovered.size}})`
          : `Case Notes &amp; Clues Discovered (${{state.cluesDiscovered.size}})`;
        const hintText = isCn ? "（点击展开）" : "(click to expand)";
        cluesHtml = `
          <div class="clues-panel" id="clues-panel">
            <button type="button" class="clues-toggle-btn" id="clues-toggle-btn" onclick="toggleClues()" aria-expanded="false">
              <span class="clues-title">
                <span class="clues-icon" id="clues-icon">&#9656;</span>
                <strong>${{cluesTitle}}</strong>
              </span>
              <span class="clues-hint" id="clues-hint">${{hintText}}</span>
            </button>
            <div class="clues-content" id="clues-content" style="display: none;">
              <ul>${{cluesList}}</ul>
            </div>
          </div>
        `;
      }}

      let choicesHtml = "";
      if (node.is_ending) {{
        const endingTitle = isCn ? "~ 案情终局 ~" : "~ Chronicle Concluded ~";
        const endingDesc = isCn
          ? "你已在当前线索分支中达成了案情结局。"
          : "You have reached a resolution in this investigation.";
        const replayText = isCn ? "&larr; 换一个视角重新探索" : "&larr; Choose Another Perspective / Replay";
        choicesHtml = `
          <div class="ending-card">
            <h3>${{endingTitle}}</h3>
            <p style="margin-bottom: 18px;">${{endingDesc}}</p>
            <button class="choice-card" onclick="renderHome()" style="text-align: center; font-weight: bold;">
              ${{replayText}}
            </button>
          </div>
        `;
      }} else {{
        const choiceCards = node.choices.map((c, index) => {{
          let switchTag = "";
          if (c.pov_switch_name) {{
            switchTag = isCn
              ? `<div class="pov-switch-notice">&xrarr; 视角即将切换至：${{escapeHtml(c.pov_switch_name)}}</div>`
              : `<div class="pov-switch-notice">&xrarr; Perspective shifts to ${{escapeHtml(c.pov_switch_name)}}</div>`;
          }}
          return `
            <button class="choice-card" onclick="goToNode('${{c.target}}')">
              <strong>${{index + 1}}.</strong> ${{escapeHtml(c.text)}}
              ${{switchTag}}
            </button>
          `;
        }}).join("");

        const choiceHeader = isCn ? "决定你的下一步行动：" : "Decide Your Next Action:";
        choicesHtml = `
          <div class="choices-section">
            <div class="choices-header">${{choiceHeader}}</div>
            ${{choiceCards}}
          </div>
        `;
      }}

      const anchorText = isCn ? "正典主线关键节点" : "Canon Milestone";
      const anchorBadge = node.anchor_name
        ? `<span class="anchor-tag">${{anchorText}}</span>`
        : "";

      const povLabel = isCn ? "视角" : "Perspective";
      const backText = isCn ? "&larr; 返回上一节" : "&larr; Previous Scene";
      const tocText = isCn ? "返回主目录" : "Table of Contents";

      root.innerHTML = `
        <div class="pov-indicator">
          <span><strong>${{povLabel}}:</strong> ${{escapeHtml(node.pov_name)}}</span>
          ${{anchorBadge}}
        </div>

        <h2 class="scene-title">${{escapeHtml(node.title)}}</h2>

        <div class="prose">
          ${{paragraphs}}
        </div>

        ${{cluesHtml}}
        ${{choicesHtml}}

        <div class="bottom-nav">
          <button onclick="goBack()">${{backText}}</button>
          <button onclick="renderHome()">${{tocText}}</button>
        </div>
      `;
    }}

    function escapeHtml(str) {{
      if (!str) return "";
      return str
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
    }}

    // Initialize in English by default
    renderHome();
  </script>
</body>
</html>
"""
