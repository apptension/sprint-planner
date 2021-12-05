import settings
from dataclasses import dataclass
from model.issue import Issue


@dataclass(frozen=True)
class CalendarEntry:
    on_meeting: bool
    issue: Issue
    length: int = 15

    @property
    def too_short(self):
        return self.length < int(settings.MIN_CONSIDERABLE_SLOT_TIME)

    @property
    def busy(self) -> bool:
        return self.on_meeting or self.issue or self.too_short

    @property
    def busy_on_meeting(self) -> bool:
        return self.on_meeting

    @property
    def busy_on_issue(self) -> bool:
        return self.issue is not None

    def __str__(self):
        if self.too_short and not self.on_meeting:
            return "Skipped {} minutes, slot is to short".format(self.length)

        blockTypeLabel = "Busy" if self.busy else "Free"
        blockDurationLabel = "{} minutes".format(self.length)

        busyReasonLabel = "(working on {})".format(self.issue.name) if self.issue else "(on meeting)"

        return "{} for {} {}".format(blockTypeLabel, blockDurationLabel, busyReasonLabel if self.busy else "")
