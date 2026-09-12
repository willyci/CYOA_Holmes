# -*- coding: utf-8 -*-
"""Update generate_hound_stories.py to incorporate full 15-chapter Holmes and Stapleton tracks."""
import re
from pathlib import Path

ROOT = Path(r"c:\dev\CYOA_Holmes")

with open(ROOT / "generate_hound_stories.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update cross-POV targets in Watson nodes
replacements = [
    ('"target": "holmes_start"', '"target": "holmes_ch06_part2_hut_surveillance"'),
    ('"target": "stapleton_start"', '"target": "stapleton_ch06_part1_arrival_watch"'),
    ('"target": "holmes_ancestral_clue"', '"target": "holmes_ch13_portrait"'),
    ('"target": "holmes_moor_ambush"', '"target": "holmes_ch11_part2_stone_hut"'),
    ('"target": "stapleton_dinner_trap"', '"target": "stapleton_ch13_fatal_dinner"'),
    ('"holmes_ch1_baker_street"', '"holmes_ch01_part1_observation"'),
    ('"stapleton_ch1_london"', '"stapleton_ch01_part1_heritage"'),
]

for old, new in replacements:
    code = code.replace(old, new)

# 2. Replace lines from '# 2. HOLMES & STAPLETON NODES EXTRACTION' onward
new_tail = '''# 2. HOLMES & STAPLETON 15-CHAPTER TRACKS
from holmes_data import HOLMES_NODES
from stapleton_data import STAPLETON_NODES

def render_watson_nodes_code(lang):
    code_blocks = []
    for cfg in WATSON_NODES:
        content = get_watson_node_text(cfg, lang)
        node_type = f"NodeType.{cfg['type'].upper()}"
        anchor_str = f'"{cfg["anchor"]}"' if cfg["anchor"] else "None"
        clues_str = json.dumps(cfg["clues_en" if lang == "en" else "clues_cn"], ensure_ascii=False)
        pov_enum = f"POV.{cfg['pov'].upper()}"
        choices = cfg["choices_en" if lang == "en" else "choices_cn"]
        choices_code = []
        for c in choices:
            sw = f', pov_switch=POV.{c["pov_switch"].upper()}' if "pov_switch" in c else ""
            choices_code.append(
                f'            Choice(id="{c["id"]}", text={json.dumps(c["text"], ensure_ascii=False)}, target_node_id="{c["target"]}"{sw}),'
            )
        choices_block = "\\n".join(choices_code)
        if choices_block:
            choices_block = f"[\\n{choices_block}\\n        ]"
        else:
            choices_block = "[]"

        title_str = json.dumps(cfg["title_en" if lang == "en" else "title_cn"], ensure_ascii=False)
        code_block = f\'\'\'    nodes["{cfg['id']}"] = PassageNode(
        id="{cfg['id']}",
        title={title_str},
        pov={pov_enum},
        node_type={node_type},
        anchor_name={anchor_str},
        content={json.dumps(content, ensure_ascii=False)},
        choices={choices_block},
        clues_discovered={clues_str},
    )
\'\'\'
        code_blocks.append(code_block)
    return "".join(code_blocks)

def render_track_nodes_code(track_list, lang):
    code_blocks = []
    for cfg in track_list:
        content = cfg["content_en"] if lang == "en" else cfg["content_cn"]
        node_type = f"NodeType.{cfg['type'].upper()}"
        anchor_str = f'"{cfg["anchor"]}"' if cfg.get("anchor") else "None"
        clues_str = json.dumps(cfg["clues_en" if lang == "en" else "clues_cn"], ensure_ascii=False)
        pov_enum = f"POV.{cfg['pov'].upper()}"
        choices = cfg["choices_en" if lang == "en" else "choices_cn"]
        choices_code = []
        for c in choices:
            sw = f', pov_switch=POV.{c["pov_switch"].upper()}' if "pov_switch" in c else ""
            choices_code.append(
                f'            Choice(id="{c["id"]}", text={json.dumps(c["text"], ensure_ascii=False)}, target_node_id="{c["target"]}"{sw}),'
            )
        choices_block = "\\n".join(choices_code)
        if choices_block:
            choices_block = f"[\\n{choices_block}\\n        ]"
        else:
            choices_block = "[]"

        title_str = json.dumps(cfg["title_en" if lang == "en" else "title_cn"], ensure_ascii=False)
        code_block = f\'\'\'    nodes["{cfg['id']}"] = PassageNode(
        id="{cfg['id']}",
        title={title_str},
        pov={pov_enum},
        node_type={node_type},
        anchor_name={anchor_str},
        content={json.dumps(content, ensure_ascii=False)},
        choices={choices_block},
        clues_discovered={clues_str},
    )
\'\'\'
        code_blocks.append(code_block)
    return "".join(code_blocks)

print("Writing hound_story_en.py...")
en_code = f\'\'\'"""English narrative content adapting 'The Hound of the Baskervilles' by Sir Arthur Conan Doyle.
Multi-POV Canonical 15-Chapter Edition:
- Dr. John H. Watson: 15 Canonical Chapters with extensive authentic prose (book_en.txt)
- Sherlock Holmes: 15 Canonical Chapters with extensive first-person deductive prose
- Jack Stapleton: 15 Canonical Chapters with chilling antagonist first-person prose
"""

from src.models import Choice, NodeType, POV, PassageNode, StoryGraph


def build_story_en() -> StoryGraph:
    """Constructs the English StoryGraph with all three playable perspectives."""
    nodes: dict[str, PassageNode] = {{}}

    # =========================================================================
    # 1. WATSON CANONICAL TRACK (15 Chapters, extensive text)
    # =========================================================================
{render_watson_nodes_code("en")}

    # =========================================================================
    # 2. SHERLOCK HOLMES TRACK (15 Chapters, extensive text)
    # =========================================================================
{render_track_nodes_code(HOLMES_NODES, "en")}

    # =========================================================================
    # 3. JACK STAPLETON TRACK (15 Chapters, extensive text)
    # =========================================================================
{render_track_nodes_code(STAPLETON_NODES, "en")}

    return StoryGraph(
        language="en",
        title="The Hound of the Baskervilles: Multi-POV Interactive Edition",
        author="Sir Arthur Conan Doyle",
        description=(
            "Experience The Hound of the Baskervilles across three playable perspectives across all 15 canonical chapters: "
            "Dr. John H. Watson (authentic full-length investigation), Sherlock Holmes (covert moor surveillance and deduction), "
            "and Jack Stapleton (the antagonist mastermind of Grimpen Mire)."
        ),
        start_nodes={{
            POV.WATSON: "ch01_part1_stick",
            POV.HOLMES: "holmes_ch01_part1_observation",
            POV.STAPLETON: "stapleton_ch01_part1_heritage",
        }},
        nodes=nodes,
    )
\'\'\'

with open(ROOT / 'src/content/hound_story_en.py', 'w', encoding='utf-8') as f:
    f.write(en_code)
print(f"Generated hound_story_en.py ({len(en_code)} bytes)")

print("Writing hound_story_cn.py...")
cn_code = f\'\'\'"""中文原著互动版《巴斯克维尔的猎犬》（阿瑟·柯南·道尔著）。
多视角全十五章节原著典藏版：
- 约翰·H·华生医生：完整15章原著宏篇长篇纪实（book_cn.txt），保留原著详尽篇幅。
- 歇洛克·福尔摩斯：完整15章名侦探第一人称深度探案、荒原石屋隐蔽暗察与严密逻辑推理。
- 杰克·斯台普吞：完整15章幕后主使第一人称暗黑密谋、训育荧光猎犬夺取遗产的反派主线。
"""

from src.models import Choice, NodeType, POV, PassageNode, StoryGraph


def build_story_cn() -> StoryGraph:
    """构建涵盖三重视角与原著完整15章节的中文互动故事图谱。"""
    nodes: dict[str, PassageNode] = {{}}

    # =========================================================================
    # 1. 华生正典主线（全15章原著宏篇长文）
    # =========================================================================
{render_watson_nodes_code("cn")}

    # =========================================================================
    # 2. 福尔摩斯正典主线（全15章第一人称宏篇长文）
    # =========================================================================
{render_track_nodes_code(HOLMES_NODES, "cn")}

    # =========================================================================
    # 3. 斯台普吞正典主线（全15章第一人称宏篇长文）
    # =========================================================================
{render_track_nodes_code(STAPLETON_NODES, "cn")}

    return StoryGraph(
        language="cn",
        title="巴斯克维尔的猎犬：多视角原著互动典藏版",
        author="阿瑟·柯南·道尔",
        description=(
            "完整重现阿瑟·柯南·道尔原著十五个章节的宏篇巨著。三大人物视角全篇15章完整覆盖："
            "华生医生（全15章原汁原味长篇探案纪实）、福尔摩斯（全15章神探第一人称破案纪实）与斯台普吞（全15章反派罪枭第一人称沉浸密谋）。"
        ),
        start_nodes={{
            POV.WATSON: "ch01_part1_stick",
            POV.HOLMES: "holmes_ch01_part1_observation",
            POV.STAPLETON: "stapleton_ch01_part1_heritage",
        }},
        nodes=nodes,
    )
\'\'\'

with open(ROOT / 'src/content/hound_story_cn.py', 'w', encoding='utf-8') as f:
    f.write(cn_code)
print(f"Generated hound_story_cn.py ({len(cn_code)} bytes)")
'''

# Find cut point in generate_hound_stories.py
cut_marker = "# 2. HOLMES & STAPLETON NODES EXTRACTION"
idx = code.find(cut_marker)
if idx != -1:
    code = code[:idx] + new_tail
else:
    print("WARNING: cut marker not found!")

with open(ROOT / "generate_hound_stories.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Updated generate_hound_stories.py successfully!")
