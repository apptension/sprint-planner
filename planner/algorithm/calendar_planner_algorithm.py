import math
from model.calendar_schedule import CalendarSchedule
from model.issues_list import IssuesList
from planner.visualise import print_issues

class CalendarPlannerAlgorithm:
    def __init__(self, name: str, schedule: CalendarSchedule, issues: IssuesList):
        self.name = name
        self.schedule = schedule
        self.issues = issues
        self.expected_time_per_estimation_point = math.ceil(self.schedule.total_free_time / self.issues.total_estimation)

    def run(self):
        print('Running "{}"\n'.format(self.name))

        print('\n\n')
        print('Available Issues (Prioritised):\n')
        print_issues(self.issues.in_prioritised_order, time_per_estimation_point=self.expected_time_per_estimation_point)

        print('\n\n')

        print('Total issues estimation: ' + str(self.issues.total_estimation))
        print('Total calendar time: ' + str(self.schedule.total_time))
        print('Total calendar free time: ' + str(self.schedule.total_free_time))
        print('Total calendar busy time: ' + str(self.schedule.total_busy_time))
        print('Expected time per estimation point (minutes): ' + str(self.expected_time_per_estimation_point))