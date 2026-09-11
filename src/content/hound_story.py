"""Multi-POV narrative content router for 'The Hound of the Baskervilles'.

Supports both English and Chinese (《巴斯克维尔的猎犬》) starting from Chapter 1 at 221B Baker Street:
- en: src.content.hound_story_en
- cn: src.content.hound_story_cn

Based directly on canonical texts:
- book_en.txt: Arthur Conan Doyle original English text
- book_cn.txt: Classic Chinese translation
"""

from src.content.hound_story_cn import build_story_cn
from src.content.hound_story_en import build_story_en
from src.models import StoryGraph


def create_hound_story(lang: str = "en") -> StoryGraph:
    """Builds and returns the StoryGraph for The Hound of the Baskervilles in specified language."""
    if lang.lower() in ("cn", "zh"):
        return build_story_cn()
    return build_story_en()
