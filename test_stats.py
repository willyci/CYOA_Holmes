from src.content.hound_story import create_hound_story
from src.graph import StoryGraphManager

for lang in ['en', 'cn']:
    story = create_hound_story(lang)
    manager = StoryGraphManager(story)
    stats = manager.validate_graph()
    print(f"[{lang}] Total: {stats['total_nodes']}, Reachable: {stats['reachable_nodes']}, Endings: {stats['endings_count']}")
    print(f"[{lang}] POV breakdown: {stats['pov_breakdown']}")
    for pov, start_id in story.start_nodes.items():
        paths = manager.get_paths_to_endings(start_id)
        start_node = story.get_node(start_id)
        print(f"  {pov.value} (start: {start_id}, pov: {start_node.pov.value}) -> {len(paths)} paths to endings")
