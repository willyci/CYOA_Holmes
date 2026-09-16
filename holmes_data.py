"""Aggregator for Sherlock Holmes 15-chapter track.
Imports modular chapters 1-5, 6-10, and 11-14 from src.content.tracks.
"""
from src.content.tracks.holmes_part1 import HOLMES_NODES_PART1
from src.content.tracks.holmes_part2 import HOLMES_NODES_PART2
from src.content.tracks.holmes_part3 import HOLMES_NODES_PART3

HOLMES_NODES = HOLMES_NODES_PART1 + HOLMES_NODES_PART2 + HOLMES_NODES_PART3

if __name__ == "__main__":
    print(f"Loaded {len(HOLMES_NODES)} Holmes track nodes.")
    total_en = sum(len(n["content_en"].split()) for n in HOLMES_NODES)
    total_cn = sum(len(n["content_cn"]) for n in HOLMES_NODES)
    print(f"Total English words: {total_en}")
    print(f"Total Chinese characters: {total_cn}")
