from planner.export import export_plan_to_csv
from planner.visualise import print_calendar, print_issues
from planner.propose_schedule import Algorithm, propose_schedule
from services.google_calendar import GoogleCalendarEventsClient
from services.jira_client import JiraClient

jira_client = JiraClient()
issues = jira_client.get_issues_list()
current_sprint = jira_client.get_current_sprint()

google_event_client = GoogleCalendarEventsClient(start_date=current_sprint.startDate, end_date=current_sprint.endDate)
calendar = google_event_client.get_calendar_list()

print('Available calendar:\n')
print_calendar(calendar)

print('\n\n')
print('Available Issues:\n')
print_issues(issues.issues)

print('\n\n')

(proposed_schedule, stats) = propose_schedule(
    calendar,
    issues,
    # time_per_estimation_point=60,
    algorithm=Algorithm.NAIVE_GREEDY_WITH_SPLIT
    )

print('\n\n')

print('Output:\n')
print_calendar(proposed_schedule)

export_plan_to_csv(proposed_schedule, filename='sprint_plan.csv')
