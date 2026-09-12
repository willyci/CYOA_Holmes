import subprocess, re, json, sys
sys.stdout.reconfigure(encoding='utf-8')

en_src = subprocess.check_output(['git', 'show', '7b5b9e5:src/content/hound_story_en.py'], text=True, encoding='utf-8')
cn_src = subprocess.check_output(['git', 'show', '7b5b9e5:src/content/hound_story_cn.py'], text=True, encoding='utf-8')

# Extract nodes from en_src and cn_src
def extract_nodes(src):
    node_pattern = re.compile(
        r'nodes\["([^"]+)"\] = PassageNode\((.*?)\n    \)',
        re.DOTALL
    )
    nodes = {}
    for m in node_pattern.finditer(src):
        nid = m.group(1)
        body = m.group(2)
        nodes[nid] = body
    return nodes

en_nodes = extract_nodes(en_src)
cn_nodes = extract_nodes(cn_src)

print(f"Old EN nodes: {len(en_nodes)}, Old CN nodes: {len(cn_nodes)}")
holmes_nodes = [nid for nid in en_nodes if nid.startswith('holmes_')]
stapleton_nodes = [nid for nid in en_nodes if nid.startswith('stapleton_')]
print(f"Holmes nodes: {len(holmes_nodes)}")
print(f"Stapleton nodes: {len(stapleton_nodes)}")

with open('old_holmes_stapleton_nodes.json', 'w', encoding='utf-8') as f:
    json.dump({
        'holmes': holmes_nodes,
        'stapleton': stapleton_nodes,
    }, f, indent=2)
print("Dumped node IDs successfully.")
