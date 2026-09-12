"""Script to extract and map Holmes and Stapleton nodes from 7b5b9e5 into our 15-chapter architecture.
"""
import subprocess, re, sys, json
sys.stdout.reconfigure(encoding='utf-8')

en_src = subprocess.check_output(['git', 'show', '7b5b9e5:src/content/hound_story_en.py'], text=True, encoding='utf-8')
cn_src = subprocess.check_output(['git', 'show', '7b5b9e5:src/content/hound_story_cn.py'], text=True, encoding='utf-8')

# Target mappings to align with 15-chapter node IDs
TARGET_MAP = {
    "climax_fog_advance": "ch14_part1_fog_ambush",
    "watson_hut_reunion": "ch11_part2_stone_hut",
    "watson_climax_vigil": "ch14_part1_fog_ambush",
    "ending_canon": "ch15_victory",
    "ending_watson_heroic": "ch15_watson",
    "ending_holmes_master_deduction": "ch15_holmes",
    "ending_stapleton_triumph": "ch15_tragedy",
    "ending_stapleton_tragedy": "ch15_mire",
    "ending_stapleton_arrest": "ch15_arrest",
}

def extract_pov_nodes(src):
    pattern = re.compile(
        r'nodes\["((?:holmes|stapleton)_[^"]+)"\] = PassageNode\((.*?)\n    \)',
        re.DOTALL
    )
    nodes = {}
    for m in pattern.finditer(src):
        nid = m.group(1)
        body = m.group(2)
        # replace targets in body
        for old_t, new_t in TARGET_MAP.items():
            body = body.replace(f'target_node_id="{old_t}"', f'target_node_id="{new_t}"')
        nodes[nid] = body
    return nodes

en_pov_nodes = extract_pov_nodes(en_src)
cn_pov_nodes = extract_pov_nodes(cn_src)

# Connect holmes_moor_ambush from holmes_hut_interior so Holmes POV can reach it
en_extra_choice = '''            Choice(
                id="h_hut_to_ambush",
                text="Slip outside quietly to intercept any watcher from the blind side of the stones.",
                target_node_id="holmes_moor_ambush",
            ),
'''
cn_extra_choice = '''            Choice(
                id="h_hut_to_ambush",
                text="轻步潜行至石屋外，借巨石盲区反向拦截查探的暗哨。",
                target_node_id="holmes_moor_ambush",
            ),
'''

if "holmes_hut_interior" in en_pov_nodes:
    en_pov_nodes["holmes_hut_interior"] = en_pov_nodes["holmes_hut_interior"].replace(
        'choices=[\n',
        f'choices=[\n{en_extra_choice}'
    )
if "holmes_hut_interior" in cn_pov_nodes:
    cn_pov_nodes["holmes_hut_interior"] = cn_pov_nodes["holmes_hut_interior"].replace(
        'choices=[\n',
        f'choices=[\n{cn_extra_choice}'
    )

print(f"Extracted {len(en_pov_nodes)} EN POV nodes, {len(cn_pov_nodes)} CN POV nodes")
assert set(en_pov_nodes.keys()) == set(cn_pov_nodes.keys()), "Node IDs mismatch between EN and CN!"
print("All node IDs match 100% between EN and CN!")
