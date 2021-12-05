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

    def __str__(self):
        blockTypeLabel = "Busy" if self.busy else "Free"
        blockDurationLabel = "{} minutes".format(self.length)

        busyReasonLabel = "(working on {})".format(self.issue.name) if self.issue else "(on meeting)"

        return "{} for {} {}".format(blockTypeLabel, blockDurationLabel, busyReasonLabel if self.busy else "")
