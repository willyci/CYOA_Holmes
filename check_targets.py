import subprocess, re, sys
sys.stdout.reconfigure(encoding='utf-8')

en_src = subprocess.check_output(['git', 'show', '7b5b9e5:src/content/hound_story_en.py'], text=True, encoding='utf-8')

node_pattern = re.compile(
    r'nodes\["((?:holmes|stapleton)_[^"]+)"\] = PassageNode\(.*?\n        choices=\[(.*?)\n        \],',
    re.DOTALL
)

for m in node_pattern.finditer(en_src):
    nid = m.group(1)
    choices_str = m.group(2)
    targets = re.findall(r'target_node_id="([^"]+)"', choices_str)
    print(f"{nid:30} -> {targets}")
