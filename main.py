from llist import sllist

from model.calendar_entry import CalendarEntry
from model.issue import Issue
from planner.visualise import print_calendar

mockIssues = [
    Issue('1', 'issue_1', 5, 1),
    Issue('2', 'issue_1', 5, 3),
    Issue('3', 'issue_1', 5, 8),
    Issue('4', 'issue_1', 5, 3),
]

mockCalendar = sllist([
    CalendarEntry(False, None, 60),
    CalendarEntry(True, None, 120),
    CalendarEntry(False, None, 60),
    CalendarEntry(True, None, 60),
    CalendarEntry(False, None, 180),
])

print_calendar(mockCalendar)