from model.calendar_entry import CalendarEntry
from model.calendar_schedule import CalendarSchedule
from model.issues_list import IssuesList
from planner.algorithm.calendar_planner_algorithm import CalendarPlannerAlgorithm

class GreedyNaive(CalendarPlannerAlgorithm):
    def __init__(self, schedule: CalendarSchedule, issues: IssuesList):
        super().__init__(name="Greedy Naive", schedule=schedule, issues=issues)
    
    def run(self):
        super().run()
        return self.schedule