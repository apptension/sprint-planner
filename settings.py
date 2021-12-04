import os
from dotenv import load_dotenv

load_dotenv()

# JIRA
JIRA_SERVER = os.getenv('JIRA_SERVER')
JIRA_USER = os.getenv('JIRA_USER')
JIRA_TOKEN = os.getenv('JIRA_TOKEN')
JIRA_PROJECT = os.getenv('JIRA_PROJECT')
JIRA_ESTIMATE_FIELD = os.getenv("JIRA_ESTIMATE_FIELD", "timeoriginalestimate")
JIRA_ISSUES_JQL = os.getenv("JIRA_ISSUES_JQL", 'project=' + JIRA_PROJECT)
JIRA_PRIORITY_ORDER = os.getenv("JIRA_PRIORITY_ORDER", "ASC")
