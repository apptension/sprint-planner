import math

class GreedyNaive:
    schedule = None
    issues = None

    def __init__(self, schedule, issues):
        self.schedule = schedule
        self.issues = issues

    @property
    def expected_time_per_estimation_point(self):
        return math.ceil(self.schedule.total_free_time / self.issues.total_estimation)

    def run(self):
        print('Running "Greedy Naive"\n')

        print('Total issues estimation: ' + str(self.issues.total_estimation))
        print('Total calendar time: ' + str(self.schedule.total_time))
        print('Total calendar free time: ' + str(self.schedule.total_free_time))
        print('Total calendar busy time: ' + str(self.schedule.total_busy_time))
        print('Expected time per estimation point (minutes): ' + str(self.expected_time_per_estimation_point))

        return self.schedule