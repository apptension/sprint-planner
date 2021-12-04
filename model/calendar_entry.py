from dataclasses import dataclass
from model.issue import Issue

@dataclass(frozen=True)
class CalendarEntry:
    busy: bool
    issue: Issue
    length: int = 15