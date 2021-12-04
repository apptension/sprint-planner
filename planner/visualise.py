def print_calendar(calendar_enties_list):
    for index, entry in enumerate(calendar_enties_list):
        blockTypeLabel = 'Busy' if entry.busy else 'Free'
        blockDurationLabel = '{} minutes'.format(entry.length)
        
        busyReasonLabel = '(working on {})'.format(entry.issue.name) if entry.issue else '(on meeting)'

        print('{} for {} {}'.format(blockTypeLabel, blockDurationLabel, busyReasonLabel if entry.busy else ''))
        
        if index < len(calendar_enties_list) - 1:
            print(' | ')
            print(' | ')
