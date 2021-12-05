def print_calendar(calendar_schedule):
    calendar_enties_list = calendar_schedule.entries

    for index, entry in enumerate(calendar_enties_list):
        print(str(entry))

        if index < len(calendar_enties_list) - 1:
            print(" | ")


def print_issues(issues, time_per_estimation_point=None):
    for issue in issues:
        expected_time = (
            "| estimated time (minutes) {}".format(
                issue.estimation * time_per_estimation_point
            )
            if time_per_estimation_point != None
            else ""
        )
        print("{} {}".format(str(issue), expected_time))
