import subprocess, re

out = subprocess.check_output(['git', 'show', '7b5b9e5:src/content/hound_story_en.py'], text=True, encoding='utf-8')

pattern = re.compile(
    r'nodes\["([^"]+)"\] = PassageNode\(\s*id="[^"]+",\s*title="([^"]+)",\s*pov=POV\.([A-Z]+).*?content=\((.*?)\),\s*choices=\[(.*?)\]',
    re.DOTALL
)

print("Nodes in 7b5b9e5:")
for m in pattern.finditer(out):
    nid = m.group(1)
    title = m.group(2)
    pov = m.group(3)
    choices = re.findall(r'target_node_id="([^"]+)"', m.group(5))
    print(f"[{pov:9}] {nid:32} | {title} | -> {choices}")
