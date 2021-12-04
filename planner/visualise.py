def print_calendar(calendar_schedule):
    calendar_enties_list = calendar_schedule.entries
    
    for index, entry in enumerate(calendar_enties_list):
        blockTypeLabel = 'Busy' if entry.busy else 'Free'
        blockDurationLabel = '{} minutes'.format(entry.length)
        
        busyReasonLabel = '(working on {})'.format(entry.issue.name) if entry.issue else '(on meeting)'

        print('{} for {} {}'.format(blockTypeLabel, blockDurationLabel, busyReasonLabel if entry.busy else ''))
        
        if index < len(calendar_enties_list) - 1:
            print(' | ')


def print_issues(issues, time_per_estimation_point = None):
    for issue in issues:
        expected_time = '| estimated time (minutes) {}'.format(issue.estimation * time_per_estimation_point) if time_per_estimation_point != None else ''
        print('{} | priority: {} | estimation: {} {}'.format(issue.name, issue.priority, issue.estimation, expected_time))