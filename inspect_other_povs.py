import subprocess, re

out = subprocess.check_output(['git', 'show', '7b5b9e5:src/content/hound_story_en.py'], text=True, encoding='utf-8')

# Find all holmes and stapleton nodes
pattern = re.compile(
    r'nodes\["((?:holmes|stapleton)_[^"]+)"\] = PassageNode\((.*?)\n    \)',
    re.DOTALL
)

for m in pattern.finditer(out):
    nid = m.group(1)
    body = m.group(2)
    title_m = re.search(r'title="([^"]+)"', body)
    title = title_m.group(1) if title_m else ""
    content_m = re.search(r'content=\((.*?)\),\s*choices', body, re.DOTALL)
    content = content_m.group(1) if content_m else ""
    print(f"=== {nid} ({title}) ===")
    print(content[:150].strip() + "...\n")
