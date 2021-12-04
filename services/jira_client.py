import settings

from typing import Union
from jira import JIRA
from jira.resources import Issue as JiraIssue, Sprint
from model.issue import Issue
from model.issues_list import IssuesList


class JiraClient:
    jira = None

    def __init__(self):
        self.jira = JIRA(server=settings.JIRA_SERVER, basic_auth=(settings.JIRA_USER, settings.JIRA_TOKEN))

    @staticmethod
    def _create_issue_from_jira_issue(jira_issue: JiraIssue) -> Union[Issue, None]:
        if hasattr(jira_issue.fields, settings.JIRA_ESTIMATE_FIELD) and getattr(jira_issue.fields, settings.JIRA_ESTIMATE_FIELD):
            return Issue(
                jira_issue.key,
                jira_issue.fields.summary,
                int(getattr(jira_issue.fields, settings.JIRA_ESTIMATE_FIELD)),
                int(jira_issue.fields.priority.id)
            )
        return None

    def get_issues_list(self):
        jira_issues = self.jira.search_issues(settings.JIRA_ISSUES_JQL)
        issues = []
        for jira_issue in jira_issues:
            issues += filter(None, [self._create_issue_from_jira_issue(jira_issue)])
        return IssuesList(issues)

    def get_current_sprint(self) -> Sprint:
        return self.jira.sprints(self.jira.boards(projectKeyOrID=settings.JIRA_PROJECT)[0].id, state="active")[0]
