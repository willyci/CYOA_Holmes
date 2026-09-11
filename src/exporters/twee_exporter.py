"""Standard Twee 3 (.twee) exporter for Twine 2 and Tweego compilers."""

from pathlib import Path
from src.models import StoryGraph, PassageNode, POV


class TweeExporter:
    """Exports StoryGraph into standard Twee 3 format."""

    def __init__(self, story: StoryGraph):
        self.story = story
        self.is_cn = story.language.lower() in ("cn", "zh")

    def export(self, output_path: str | Path) -> Path:
        out_file = Path(output_path)
        out_file.parent.mkdir(parents=True, exist_ok=True)

        lines: list[str] = []

        # StoryData and StoryTitle
        lines.append(f":: StoryTitle\n{self.story.title}\n")
        lines.append(
            ":: StoryData\n"
            "{\n"
            '  "ifid": "C7D3882B-B1C8-42FE-9332-86BDEE76A7FC",\n'
            '  "format": "SugarCube",\n'
            '  "format-version": "2.36.1",\n'
            '  "start": "Start"\n'
            "}\n"
        )

        # Start Passage (POV selection)
        lines.append(":: Start [start]\n")
        lines.append(f"''{self.story.title}''\n")
        lines.append(f"//Adapted from {self.story.author}//\n\n")
        lines.append(f"{self.story.description}\n\n")

        pov_prompt = "请选择你的探案视角：\n" if self.is_cn else "Select your perspective:\n"
        lines.append(pov_prompt)
        lines.append(f"* [[{POV.WATSON.display_name(self.story.language)}|{self.story.start_nodes[POV.WATSON]}]]\n")
        lines.append(f"* [[{POV.HOLMES.display_name(self.story.language)}|{self.story.start_nodes[POV.HOLMES]}]]\n")
        lines.append(f"* [[{POV.STAPLETON.display_name(self.story.language)}|{self.story.start_nodes[POV.STAPLETON]}]]\n\n")

        # Passages
        clues_label = "线索：" if self.is_cn else "Clues:"
        choices_label = "选项：" if self.is_cn else "Choices:"
        ending_label = "''~ 终局 ~''\n\n" if self.is_cn else "''~ The End ~''\n\n"
        return_label = "[[返回开始|Start]]\n\n" if self.is_cn else "[[Return to Start|Start]]\n\n"

        for node_id, node in self.story.nodes.items():
            tags = [node.pov.value, node.node_type.value]
            if node.anchor_name:
                tags.append(node.anchor_name)
            tag_str = f" [{ ' '.join(tags) }]"

            pov_display = node.pov.display_name(self.story.language)
            lines.append(f":: {node_id}{tag_str}\n")
            lines.append(f"''{node.title}'' (POV: {pov_display})\n\n")
            lines.append(f"{node.content}\n\n")

            if node.clues_discovered:
                lines.append(f"''{clues_label}'' {', '.join(node.clues_discovered)}\n\n")

            if node.is_ending:
                lines.append(ending_label)
                lines.append(return_label)
            else:
                lines.append(f"''{choices_label}''\n")
                for c in node.choices:
                    lines.append(f"* [[{c.text}|{c.target_node_id}]]\n")
                lines.append("\n")

        out_file.write_text("".join(lines), encoding="utf-8")
        return out_file
