import math
from model.calendar_schedule import CalendarSchedule
from model.issues_list import IssuesList
from planner.visualise import print_issues

class CalendarPlannerAlgorithm:
    def __init__(self, name: str, schedule: CalendarSchedule, issues: IssuesList, time_per_estimation_point: int):
        self.name = name
        self.schedule = schedule
        self.issues = issues
        self.expected_time_per_estimation_point = time_per_estimation_point or math.floor(self.schedule.total_free_time / self.issues.total_estimation)

    def is_issue_scheduled(self, issue):
        return next((entry for entry in self.schedule.schedule if entry.issue and entry.issue.id == issue.id), None) != None

    @property
    def scheduled_issues(self):
        return filter(lambda issue : self.is_issue_scheduled(issue), self.issues.issues)

    @property
    def expected_time_to_finish_scheduled_issues(self):
        return sum(entry.estimation * self.expected_time_per_estimation_point for entry in self.scheduled_issues)

    @property
    def not_scheduled_issues(self):
        return filter(lambda issue : not self.is_issue_scheduled(issue), self.issues.issues)

    @property
    def expected_time_to_finish_not_scheduled_issues(self):
        return sum(entry.estimation * self.expected_time_per_estimation_point for entry in self.not_scheduled_issues)

    @property
    def scheduled_sprint_coverage(self):
        return self.expected_time_to_finish_scheduled_issues / (self.issues.total_estimation * self.expected_time_per_estimation_point)

    @property
    def stats(self):
        print('\n\n')
        print('Stats:')
        
        print('Total issues estimation: {} SP / {} minutes'.format(
            self.issues.total_estimation,
            self.issues.total_estimation * self.expected_time_per_estimation_point
        ))
        print('Total calendar time: {} minutes'.format(self.schedule.total_time))
        print('Scheduled calendar time: {} minutes / {}%'.format(
            self.schedule.total_busy_time,
            round(100 * self.schedule.total_busy_time / self.schedule.total_time)
        ))
        print('Remaining calendar time: {} minutes / {}%'.format(
            self.schedule.total_free_time,
            round(100 * self.schedule.total_free_time / self.schedule.total_time)
        ))
        print('Expected time per estimation point: {} minutes'.format(self.expected_time_per_estimation_point))
        print('Expected time to finish not planned issues: {} minutes'.format(
            self.expected_time_to_finish_not_scheduled_issues
        ))
        print('Scheduled sprint story points coverage: {}%'.format(round(self.scheduled_sprint_coverage * 100)))
        print('Total time scheduled on issues: {} minutes / {}%'.format(
            self.schedule.total_time_spent_on_issues,
            round(100 * self.schedule.total_time_spent_on_issues / self.schedule.total_time)
        ))
        print('Total time scheduled on meetings: {} minutes / {}%'.format(
            self.schedule.total_time_spent_on_meetings,
            round(100 * self.schedule.total_time_spent_on_meetings / self.schedule.total_time)
        ))
        
        print('\n\n')
        print('Expected issues (Prioritised):\n')
        print_issues(self.issues.in_prioritised_order, time_per_estimation_point=self.expected_time_per_estimation_point)

        print('\n\n')
        print('Not scheduled issues:\n')
        print_issues(self.not_scheduled_issues, time_per_estimation_point=self.expected_time_per_estimation_point)

        return None

    def run(self):
        print('Running "{}"\n'.format(self.name))

        print('\n\n')
        print('Available Issues (Prioritised):\n')
        print_issues(self.issues.in_prioritised_order, time_per_estimation_point=self.expected_time_per_estimation_point)

        print('\n\n')

        print('Total issues estimation: {} SP / {} minutes'.format(
            self.issues.total_estimation,
            self.issues.total_estimation * self.expected_time_per_estimation_point
        ))
        print('Total calendar time: {} minutes'.format(self.schedule.total_time))
        print('Total calendar free time: {} minutes'.format(self.schedule.total_free_time))
        print('Total calendar busy time: {} minutes'.format(self.schedule.total_busy_time))
        print('Expected time per estimation point: {} minutes'.format(self.expected_time_per_estimation_point))