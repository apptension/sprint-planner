from dataclasses import dataclass

@dataclass(frozen=True)
class Issue:
    id: str
    name: str
    story_points: int = 1
    priority: int = 0