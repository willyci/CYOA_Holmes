"""Data models for the Multi-POV Choose Your Own Adventure (CYOA) engine."""

from enum import Enum
from typing import Any, Optional
from pydantic import BaseModel, Field


class POV(str, Enum):
    """Playable Points of View."""
    WATSON = "watson"
    HOLMES = "holmes"
    STAPLETON = "stapleton"

    def display_name(self, lang: str = "en") -> str:
        if lang in ("cn", "zh"):
            names = {
                POV.WATSON: "约翰·H·华生医生",
                POV.HOLMES: "歇洛克·福尔摩斯",
                POV.STAPLETON: "杰克·斯台普吞",
            }
            return names.get(self, self.value)
        names = {
            POV.WATSON: "Dr. John H. Watson",
            POV.HOLMES: "Sherlock Holmes",
            POV.STAPLETON: "Jack Stapleton",
        }
        return names.get(self, self.value.title())

    def role_description(self, lang: str = "en") -> str:
        if lang in ("cn", "zh"):
            roles = {
                POV.WATSON: "实地观察、社交探访，在巴斯克维尔庄园护卫亨利爵士。",
                POV.HOLMES: "在荒原史前石屋隐蔽监视、化学痕迹分析与缜密司法推导。",
                POV.STAPLETON: "穿行大格林盆泥潭密径、伪装昆虫学家，训育荧光猎犬夺取遗产。",
            }
            return roles.get(self, "")
        roles = {
            POV.WATSON: "Field observation, social interviews, and protective vigilance at Baskerville Hall.",
            POV.HOLMES: "Covert surveillance from the moor stone hut, chemical analysis, and deduction.",
            POV.STAPLETON: "Mire navigation, deception, and managing hound preparations without raising suspicion.",
        }
        return roles.get(self, "")


class NodeType(str, Enum):
    """Types of narrative passage nodes in the Web-and-Anchor model."""
    ANCHOR = "anchor"   # Shared canon event where multiple POVs converge
    BRANCH = "branch"   # Character-specific choice point and investigation
    CLIMAX = "climax"   # Critical confrontational chapter
    ENDING = "ending"   # Terminal outcome (victory, tragedy, escape, arrest)


class Choice(BaseModel):
    """A decision option presented to the reader at a passage."""
    id: str
    text: str
    target_node_id: str
    condition: Optional[str] = None
    pov_switch: Optional[POV] = None
    clue_hint: Optional[str] = None


class PassageNode(BaseModel):
    """An individual scene / chapter in the interactive story graph."""
    id: str
    title: str
    pov: POV
    node_type: NodeType
    content: str
    anchor_name: Optional[str] = None
    choices: list[Choice] = Field(default_factory=list)
    clues_discovered: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)

    @property
    def is_ending(self) -> bool:
        return self.node_type == NodeType.ENDING or len(self.choices) == 0


class StoryGraph(BaseModel):
    """Top-level container for the complete multi-POV interactive story."""
    language: str = "en"
    title: str = "The Hound of the Baskervilles: Multi-POV Interactive Edition"
    author: str = "Sir Arthur Conan Doyle (Adapted)"
    description: str = "A Choose Your Own Adventure adaptation experienced through Watson, Holmes, and Stapleton."
    start_nodes: dict[POV, str] = Field(
        description="Maps each playable POV to its opening passage node ID."
    )
    nodes: dict[str, PassageNode] = Field(
        description="All passage nodes indexed by unique node ID."
    )

    def get_node(self, node_id: str) -> Optional[PassageNode]:
        return self.nodes.get(node_id)
