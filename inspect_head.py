import subprocess, re

out = subprocess.check_output(['git', 'show', '7b5b9e5:src/content/hound_story_en.py'], text=True, encoding='utf-8')
matches = re.findall(r'nodes\["([^"]+)"\] = PassageNode\(\s*id="[^"]+",\s*title="([^"]+)",\s*pov=POV\.([A-Z]+)', out)
print(f"Total nodes in 7b5b9e5: {len(matches)}")
pov_counts = {}
for nid, title, pov in matches:
    pov_counts[pov] = pov_counts.get(pov, 0) + 1
print("POV counts in 7b5b9e5:", pov_counts)

print("\nSample nodes for each POV:")
for nid, title, pov in matches:
    if nid.startswith('holmes') or nid.startswith('stapleton'):
        print(f"[{pov}] {nid}: {title}")
