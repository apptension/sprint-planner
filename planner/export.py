import csv

from model.calendar_schedule import CalendarSchedule
from planner.algorithm.calendar_planner_algorithm import CalendarPlannerAlgorithm

workday_minutes = 480

def split_into_days(schedule):
    days = []
    current_day = []
    current_day_load = 0
    for entry in schedule:
        current_day.append(entry)
        current_day_load += entry.length
        if (current_day_load == workday_minutes):
            days.append(current_day)
            current_day = []
            current_day_load = 0
    
    max_day_entries = len(max(days, key=lambda day : len(day)))
    return (days, len(days), max_day_entries)
        

def export_plan_to_csv(plan: CalendarPlannerAlgorithm, filename):
    file = open(filename, "w")
    writer = csv.writer(file)

    (schedule_days, days_count, max_day_entries) = split_into_days(plan.schedule)
    
    writer.writerow('Day {}'.format(index + 1) for index, entry in enumerate(schedule_days))

    for day_entry_index in range(max_day_entries):
        writer.writerow(str(day[day_entry_index]) if day_entry_index < len(day) else '' for day in schedule_days)

    print('\n')
    print('Saved plan to {}'.format(filename))