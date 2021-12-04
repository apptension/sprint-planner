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

    @property
    def busy_on_meeting(self) -> bool:
        return self.on_meeting

    @property
    def busy_on_issue(self) -> bool:
        return self.issue is not None