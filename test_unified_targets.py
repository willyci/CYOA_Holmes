"""Validate unified multi-POV graph generation with 15-chapter Watson track + Holmes track + Stapleton track.
"""
import subprocess, re, sys, json
sys.stdout.reconfigure(encoding='utf-8')

from unify_all_povs import en_pov_nodes, cn_pov_nodes, TARGET_MAP

print(f"Loaded {len(en_pov_nodes)} Holmes/Stapleton nodes.")

# Let's inspect targets from holmes and stapleton nodes
all_targets = set()
for nid, body in en_pov_nodes.items():
    targets = re.findall(r'target_node_id="([^"]+)"', body)
    all_targets.update(targets)

print("Targets in Holmes & Stapleton nodes:", sorted(list(all_targets)))
