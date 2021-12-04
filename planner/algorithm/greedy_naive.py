class GreedyNaive:
    calendar = None
    issues = None

    def __init__(self, calendar, issues):
        self.calendar = calendar
        self.issues = issues


    @property
    def total_time(self):
        return sum(entry.length for entry in self.calendar)

    @property
    def total_free_time(self):
        entry_free_time = lambda entry : 0 if entry.busy else entry.length
        return sum(entry_free_time(entry) for entry in self.calendar)

    @property
    def total_busy_time(self):
        return self.total_time - self.total_free_time

    @property
    def total_estimation(self):
        return sum(issue.estimation for issue in self.issues)

    @property
    def expected_time_per_estimation_point(self):
        return self.total_free_time / self.total_estimation

    def run(self):
        print('Running "Greedy Naive"\n')

        print('Total issues estimation: ' + str(self.total_estimation))
        print('Total calendar time: ' + str(self.total_time))
        print('Total calendar free time: ' + str(self.total_free_time))
        print('Total calendar busy time: ' + str(self.total_busy_time))
        print('Expected time per estimation point (minutes): ' + str(self.expected_time_per_estimation_point))
        return self.calendar