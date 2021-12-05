import csv
from datetime import datetime

from model.calendar_schedule import CalendarSchedule
from planner.algorithm.calendar_planner_algorithm import CalendarPlannerAlgorithm

workday_minutes = 480

class CsvExport:
    def __init__(self, filename: str, plan: CalendarPlannerAlgorithm):
        timestamp = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
        self.filename = '{}_{}.csv'.format(filename, timestamp)
        
        file = open(self.filename, "w")
        self.writer = csv.writer(file)
        self.plan = plan

    def split_plan_into_days(self):
        days = []
        current_day = []
        current_day_load = 0
        for entry in self.plan.schedule.schedule:
            current_day.append(entry)
            current_day_load += entry.length
            if (current_day_load == workday_minutes):
                days.append(current_day)
                current_day = []
                current_day_load = 0
        
        max_day_entries = len(max(days, key=lambda day : len(day)))
        return (days, len(days), max_day_entries)
            
    def export_schedule(self):
        (schedule_days, days_count, max_day_entries) = self.split_plan_into_days()

        self.writer.writerow('Day {}'.format(index + 1) for index, entry in enumerate(schedule_days))

        for day_entry_index in range(max_day_entries):
            self.writer.writerow(str(day[day_entry_index]) if day_entry_index < len(day) else ''for day in schedule_days)


    def export_stats(self):
        self.writer.writerow([
            'Total issues estimation [SP]',
            self.plan.issues.total_estimation,
        ])

        self.writer.writerow([
            'Total issues estimation [minutes]',
            self.plan.issues.total_estimation * self.plan.expected_time_per_estimation_point,
        ])

        self.writer.writerow([
            'Total calendar time [minutes]',
            self.plan.schedule.total_time,
        ])

        self.writer.writerow([
            'Scheduled calendar time [minutes]',
            self.plan.schedule.total_busy_time,
        ])

        self.writer.writerow([
            'Scheduled calendar time [%]',
            round(100 * self.plan.schedule.total_busy_time / self.plan.schedule.total_time),
        ])

        self.writer.writerow([
            'Remaining calendar time [minutes]',
            self.plan.schedule.total_free_time
        ])

        self.writer.writerow([
            'Remaining calendar time [%]',
            round(100 * self.plan.schedule.total_free_time / self.plan.schedule.total_time)
        ])

        self.writer.writerow([
            'Expected time per estimation point [minutes]',
            self.plan.expected_time_per_estimation_point
        ])
        
        self.writer.writerow([
            'Expected time to finish not planned issues',
            self.plan.expected_time_to_finish_not_scheduled_issues
        ])

        self.writer.writerow([
            'Scheduled sprint story points coverage [%]',
            round(self.plan.scheduled_sprint_coverage * 100)
        ])

        self.writer.writerow([
            'Total time scheduled on issues [minutes]',
            self.plan.schedule.total_time_spent_on_issues
        ])

        self.writer.writerow([
            'Total time scheduled on issues [%]',
            round(100 * self.plan.schedule.total_time_spent_on_issues / self.plan.schedule.total_time)
        ])

        self.writer.writerow([
            'Total time scheduled on meetings [minutes]',
            self.plan.schedule.total_time_spent_on_meetings
        ])

        self.writer.writerow([
            'Total time scheduled on meetings [%]',
            round(100 * self.plan.schedule.total_time_spent_on_meetings / self.plan.schedule.total_time)
        ])


    def export_issues(self, issues):
        self.writer.writerow(['issue', 'priority', 'estimation [SP]', 'expected time spent [minutes]'])

        for issue in issues:
            self.writer.writerow([issue.name, issue.priority, issue.estimation, issue.estimation * self.plan.expected_time_per_estimation_point])


    def export_empty_rows(self, number = 5):
        for empty_line in range(number):
                self.writer.writerow('')


    def export_all(self):
        self.export_schedule()
        
        self.export_empty_rows()
        
        self.export_stats()

        self.export_empty_rows()

        self.writer.writerow(['Expected issues (Prioritised)'])
        self.export_issues(self.plan.issues.in_prioritised_order)

        self.export_empty_rows()

        self.writer.writerow(['Not scheduled issues'])
        self.export_issues(self.plan.not_scheduled_issues)

        print('\n')
        print('Saved plan to {}'.format(self.filename))