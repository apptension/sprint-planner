import settings
import math
from datetime import datetime
from planner.export import CsvExport
from planner.visualise import print_calendar, print_issues
from planner.propose_schedule import Algorithm, propose_schedule
from services.google_calendar import GoogleCalendarEventsClient
from services.jira_client import JiraClient

allowed_storypoints = [0, 1, 2, 3, 5, 8, 13, 21]


def round_to_allowed_storypoints(estimate):
    return next(sp for sp in allowed_storypoints[::-1] if sp <= estimate)


def main():
    sized_issues_counts = [0 for _ in allowed_storypoints]
    google_event_client = GoogleCalendarEventsClient(
        start_date=settings.FOCUS_TIME_CALENDAR_START, end_date=settings.FOCUS_TIME_CALENDAR_END
    )
    schedule = google_event_client.get_calendar_list()
    expected_time_per_storypoint = math.floor(schedule.total_free_time / int(settings.FOCUS_TIME_STORY_POINTS_CAPACITY))

    def time_to_storypoints(time):
        return round_to_allowed_storypoints(time / expected_time_per_storypoint)

    print("Available calendar:\n")
    print_calendar(schedule)

    print("\n\n")
    print("Planned calendar:\n")

    for entry in schedule.schedule:
        if entry.on_meeting:
            print(entry)
        else:
            possible_storypoints_done = time_to_storypoints(entry.length)
            sp_value_index = allowed_storypoints.index(possible_storypoints_done)
            sized_issues_counts[sp_value_index] += 1

            if possible_storypoints_done > 0:
                print(
                    "{} -- time for {} SP issue (~{} minutes)".format(
                        entry,
                        possible_storypoints_done,
                        possible_storypoints_done * expected_time_per_storypoint,
                    )
                )
            else:
                print(entry)
        print(" | ")

    print("\n\n")
    print("Summary:")
    print("\n")
    print("Time slots without issue (< 1 SP time slot): {}".format(sized_issues_counts[0]))
    for sp_value in allowed_storypoints[1:]:
        sp_value_index = allowed_storypoints.index(sp_value)
        print("Possible {} SP issues: {}".format(sp_value, sized_issues_counts[sp_value_index]))


if __name__ == "__main__":
    main()
