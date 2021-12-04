from model.calendar_entry import CalendarEntry
from model.issue import Issue
from planner.visualise import print_calendar, print_issues
from planner.propose_schedule import propose_schedule
from model.issues_list import IssuesList
from model.calendar_schedule import CalendarSchedule

mock_issues = IssuesList([
    Issue('1', 'issue_1', 2, 1),
    Issue('2', 'issue_2', 5, 3),
    Issue('3', 'issue_3', 4, 8),
    Issue('4', 'issue_4', 3, 3),
])

mock_calendar = CalendarSchedule([
    CalendarEntry(False, None, 60),
    CalendarEntry(True, None, 120),
    CalendarEntry(False, None, 60),
    CalendarEntry(True, None, 60),
    CalendarEntry(False, None, 180),
])

print('Available calendar:\n')
print_calendar(mock_calendar)

print('\n\n')
print('Available Issues:\n')
print_issues(mock_issues.issues)

print('\n\n')

proposed_schedule = propose_schedule(mock_calendar, mock_issues, time_per_estimation_point=30)

print('\n\n')

print('Output:\n')
print_calendar(proposed_schedule)

