from model.calendar_entry import CalendarEntry
from model.calendar_schedule import CalendarSchedule
from model.issues_list import IssuesList
from planner.algorithm.calendar_planner_algorithm import CalendarPlannerAlgorithm
from llist import sllist

from planner.visualise import print_calendar

class GreedyNaive(CalendarPlannerAlgorithm):
    def __init__(self, schedule: CalendarSchedule, issues: IssuesList, time_per_estimation_point = None):
        super().__init__(name="Greedy Naive", schedule=schedule, issues=issues, time_per_estimation_point=time_per_estimation_point)
        self.issues_queue = sllist(self.issues.in_prioritised_order)
    
    def pop_next_issue(self):
        return self.issues_queue.popleft()

    def run(self):
        super().run()
        step = 0

        while self.issues_queue.size > 0:
            issue = self.pop_next_issue()
            required_issue_time = issue.estimation * self.expected_time_per_estimation_point
            matching_slot = self.schedule.find_free_slot(required_issue_time)
            issue_calendar_entry = CalendarEntry(on_meeting=False, issue=issue, length=required_issue_time)
            
            if (matching_slot):
                self.schedule.add_entry_within(matching_slot, issue_calendar_entry)

            step+=1

        return self