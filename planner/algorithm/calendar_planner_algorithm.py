import math
from model.calendar_schedule import CalendarSchedule
from model.issues_list import IssuesList

class CalendarPlannerAlgorithm:
    def __init__(self, name: str, schedule: CalendarSchedule, issues: IssuesList):
        self.name = name
        self.schedule = schedule
        self.issues = issues

    @property
    def expected_time_per_estimation_point(self):
        return math.ceil(self.schedule.total_free_time / self.issues.total_estimation)

    def run(self):
        print('Running "{}"\n'.format(self.name))

        print('Total issues estimation: ' + str(self.issues.total_estimation))
        print('Total calendar time: ' + str(self.schedule.total_time))
        print('Total calendar free time: ' + str(self.schedule.total_free_time))
        print('Total calendar busy time: ' + str(self.schedule.total_busy_time))
        print('Expected time per estimation point (minutes): ' + str(self.expected_time_per_estimation_point))