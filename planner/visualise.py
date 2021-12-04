def print_calendar(calendar_schedule):
    calendar_enties_list = calendar_schedule.entries
    
    for index, entry in enumerate(calendar_enties_list):
        blockTypeLabel = 'Busy' if entry.busy else 'Free'
        blockDurationLabel = '{} minutes'.format(entry.length)
        
        busyReasonLabel = '(working on {})'.format(entry.issue.name) if entry.issue else '(on meeting)'

        print('{} for {} {}'.format(blockTypeLabel, blockDurationLabel, busyReasonLabel if entry.busy else ''))
        
        if index < len(calendar_enties_list) - 1:
            print(' | ')


def print_issues(issues):
    for issue in issues:
        print('{} | priority: {} | estimation: {}'.format(issue.name, issue.priority, issue.estimation))