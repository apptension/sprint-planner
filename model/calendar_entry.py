from dataclasses import dataclass
from model.issue import Issue

@dataclass(frozen=True)
class CalendarEntry:
    on_meeting: bool
    issue: Issue
    length: int = 15

    @property
    def busy(self) -> bool:
        return self.on_meeting or self.issue