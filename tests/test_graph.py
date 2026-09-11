"""Unit tests for story graph structure and NetworkX validation (Bilingual EN & CN)."""

import pytest
from src.content.hound_story import create_hound_story
from src.graph import StoryGraphManager, GraphValidationError
from src.models import POV, NodeType


@pytest.mark.parametrize("lang", ["en", "cn"])
def test_story_graph_integrity(lang):
    story = create_hound_story(lang)
    manager = StoryGraphManager(story)
    stats = manager.validate_graph()

    # All nodes reachable
    assert stats["total_nodes"] == 54
    assert stats["reachable_nodes"] == 54
    assert len(stats["orphan_nodes"]) == 0

    # Anchors present
    assert "anchor_chapter1" in stats["anchors"]
    assert "anchor_london_mission" in stats["anchors"]
    assert "anchor_arrival" in stats["anchors"]
    assert "anchor_convict" in stats["anchors"]
    assert "anchor_climax" in stats["anchors"]

    # All 3 POVs represented
    assert stats["pov_breakdown"]["watson"] == 19
    assert stats["pov_breakdown"]["holmes"] == 17
    assert stats["pov_breakdown"]["stapleton"] == 18

    # Multiple endings exist
    assert stats["endings_count"] == 6


@pytest.mark.parametrize("lang", ["en", "cn"])
def test_no_dangling_links(lang):
    story = create_hound_story(lang)
    node_ids = set(story.nodes.keys())

    for node_id, node in story.nodes.items():
        for choice in node.choices:
            assert choice.target_node_id in node_ids, (
                f"[{lang}] Node '{node_id}' has dangling target '{choice.target_node_id}'"
            )


@pytest.mark.parametrize("lang", ["en", "cn"])
def test_paths_to_endings(lang):
    story = create_hound_story(lang)
    manager = StoryGraphManager(story)

    for pov, start_id in story.start_nodes.items():
        paths = manager.get_paths_to_endings(start_id)
        assert len(paths) > 0, f"[{lang}] POV {pov.value} has no valid paths leading to an ending!"
