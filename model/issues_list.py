from typing import Text


class IssuesList:
    issues = None

    def __init__(self, issues):
        self.issues = issues

    @property
    def total_estimation(self):
        return sum(issue.estimation for issue in self.issues)

    @property
    def in_prioritised_order(self):
        return sorted(self.issues, key=lambda issue : (-issue.priority, issue.estimation))