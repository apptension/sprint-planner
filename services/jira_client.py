from typing import Union
from jira import JIRA
from jira.resources import Issue as JiraIssue
import os
from dotenv import load_dotenv
from model.issue import Issue
from model.issues_list import IssuesList

load_dotenv()

JIRA_SERVER = os.getenv('JIRA_SERVER')
JIRA_USER = os.getenv('JIRA_USER')
JIRA_TOKEN = os.getenv('JIRA_TOKEN')
JIRA_PROJECT = os.getenv('JIRA_PROJECT')
JIRA_ESTIMATE_FIELD = "customfield_10115"  # for time estimate use: timeoriginalestimate
JIRA_ISSUES_JQL = 'project=' + JIRA_PROJECT


class JiraClient:
    jira = None

    def __init__(self):
        self.jira = JIRA(server=JIRA_SERVER, basic_auth=(JIRA_USER, JIRA_TOKEN))

    @staticmethod
    def _create_issue_from_jira_issue(jira_issue: JiraIssue) -> Union[Issue, None]:
        if hasattr(jira_issue.fields, JIRA_ESTIMATE_FIELD) and getattr(jira_issue.fields, JIRA_ESTIMATE_FIELD):
            return Issue(
                jira_issue.key,
                jira_issue.fields.summary,
                int(getattr(jira_issue.fields, JIRA_ESTIMATE_FIELD)),
                int(jira_issue.fields.priority.id)
            )
        return None

    def get_issues_list(self):
        jira_issues = self.jira.search_issues(JIRA_ISSUES_JQL)
        issues = []
        for jira_issue in jira_issues:
            issues += filter(None, [self._create_issue_from_jira_issue(jira_issue)])
        return IssuesList(issues)
