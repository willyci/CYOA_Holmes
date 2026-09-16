"""Aggregator for Jack Stapleton 15-chapter track.
Imports modular chapters 1-5, 6-10, and 11-14 from src.content.tracks.
"""
from src.content.tracks.stapleton_part1 import STAPLETON_NODES_PART1
from src.content.tracks.stapleton_part2 import STAPLETON_NODES_PART2
from src.content.tracks.stapleton_part3 import STAPLETON_NODES_PART3

STAPLETON_NODES = STAPLETON_NODES_PART1 + STAPLETON_NODES_PART2 + STAPLETON_NODES_PART3

if __name__ == "__main__":
    print(f"Loaded {len(STAPLETON_NODES)} Stapleton track nodes.")
    total_en = sum(len(n["content_en"].split()) for n in STAPLETON_NODES)
    total_cn = sum(len(n["content_cn"]) for n in STAPLETON_NODES)
    print(f"Total English words: {total_en}")
    print(f"Total Chinese characters: {total_cn}")
