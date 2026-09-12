"""NetworkX graph construction, traversal, and structural safety validation."""

from typing import Any, Dict, List, Optional, Set, Tuple
import networkx as nx

from src.models import StoryGraph, PassageNode, NodeType, POV


class GraphValidationError(Exception):
    """Raised when story graph fails structural safety checks."""
    pass


class StoryGraphManager:
    """Wraps StoryGraph with NetworkX analysis, cycle safety, and reachability validation."""

    def __init__(self, story: StoryGraph):
        self.story = story
        self.nx_graph = self._build_nx_graph()

    def _build_nx_graph(self) -> nx.DiGraph:
        """Constructs a directed graph representing the narrative structure."""
        g = nx.DiGraph()
        for node_id, node in self.story.nodes.items():
            g.add_node(
                node_id,
                title=node.title,
                pov=node.pov.value,
                node_type=node.node_type.value,
                anchor_name=node.anchor_name,
                is_ending=node.is_ending
            )

        for node_id, node in self.story.nodes.items():
            for choice in node.choices:
                g.add_edge(
                    node_id,
                    choice.target_node_id,
                    choice_id=choice.id,
                    text=choice.text,
                    pov_switch=choice.pov_switch.value if choice.pov_switch else None
                )
        return g

    def validate_graph(self) -> dict[str, Any]:
        """Runs comprehensive NetworkX validation checks.

        Returns:
            Dict of diagnostic results and statistics.
        Raises:
            GraphValidationError if critical integrity issues exist.
        """
        errors: List[str] = []
        warnings: List[str] = []

        # 1. Check start nodes exist
        for pov, start_id in self.story.start_nodes.items():
            if start_id not in self.story.nodes:
                errors.append(f"Start node '{start_id}' for POV '{pov.value}' does not exist.")

        # 2. Check for dangling target links
        dangling_links: List[Tuple[str, str, str]] = []
        for node_id, node in self.story.nodes.items():
            for choice in node.choices:
                if choice.target_node_id not in self.story.nodes:
                    dangling_links.append((node_id, choice.id, choice.target_node_id))
                    errors.append(
                        f"Dangling link in node '{node_id}' (Choice '{choice.text}'): "
                        f"target '{choice.target_node_id}' does not exist."
                    )

        # 3. Check reachability from start nodes
        all_reachable_nodes: Set[str] = set()
        for pov, start_id in self.story.start_nodes.items():
            if start_id in self.nx_graph:
                reachable = set(nx.descendants(self.nx_graph, start_id))
                reachable.add(start_id)
                all_reachable_nodes.update(reachable)

        all_node_ids = set(self.story.nodes.keys())
        unreachable = all_node_ids - all_reachable_nodes
        if unreachable:
            warnings.append(f"Unreachable / orphan nodes detected: {sorted(list(unreachable))}")

        # 4. Check terminal states (endings should have no outgoing choices, non-endings must have choices)
        dead_ends_without_ending_type: List[str] = []
        for node_id, node in self.story.nodes.items():
            if len(node.choices) == 0 and node.node_type != NodeType.ENDING:
                dead_ends_without_ending_type.append(node_id)
                errors.append(
                    f"Node '{node_id}' has no outgoing choices but is not marked as NodeType.ENDING."
                )

        # 5. Check anchor point convergence
        anchor_nodes = [
            n for n in self.story.nodes.values()
            if n.node_type == NodeType.ANCHOR or n.anchor_name
        ]
        anchor_names = {n.anchor_name for n in anchor_nodes if n.anchor_name}

        if errors:
            raise GraphValidationError(f"Graph validation failed with {len(errors)} error(s):\n" + "\n".join(errors))

        stats = {
            "total_nodes": len(self.story.nodes),
            "total_edges": self.nx_graph.number_of_edges(),
            "reachable_nodes": len(all_reachable_nodes),
            "orphan_nodes": list(unreachable),
            "endings_count": len([n for n in self.story.nodes.values() if n.is_ending]),
            "anchor_count": len(anchor_names),
            "anchors": sorted(list(anchor_names)),
            "warnings": warnings,
            "pov_breakdown": {
                pov.value: len([n for n in self.story.nodes.values() if n.pov == pov])
                for pov in POV
            }
        }
        return stats

    def get_paths_to_endings(self, start_id: str, max_paths: Optional[int] = None) -> List[List[str]]:
        """Finds simple paths from a start node to all reachable ending nodes with optional path limit."""
        endings = [
            node_id for node_id, node in self.story.nodes.items()
            if node.is_ending
        ]
        all_paths = []
        for ending in endings:
            if nx.has_path(self.nx_graph, start_id, ending):
                if max_paths is not None:
                    count = 0
                    for path in nx.all_simple_paths(self.nx_graph, source=start_id, target=ending, cutoff=35):
                        all_paths.append(path)
                        count += 1
                        if count >= max_paths:
                            break
                else:
                    paths = list(nx.all_simple_paths(self.nx_graph, source=start_id, target=ending, cutoff=35))
                    all_paths.extend(paths)
        return all_paths
