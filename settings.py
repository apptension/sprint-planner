import os
import sys
from dotenv import load_dotenv

env_file = ".env" if len(sys.argv) == 1 else sys.argv[1]
load_dotenv(env_file)

# JIRA
JIRA_SERVER = os.getenv("JIRA_SERVER")
JIRA_USER = os.getenv("JIRA_USER")
JIRA_TOKEN = os.getenv("JIRA_TOKEN")
JIRA_PROJECT = os.getenv("JIRA_PROJECT")
JIRA_ESTIMATE_FIELD = os.getenv("JIRA_ESTIMATE_FIELD", "timeoriginalestimate")
JIRA_ISSUES_JQL = os.getenv(
    "JIRA_ISSUES_JQL",
    "project=" + JIRA_PROJECT + " and sprint in openSprints() AND assignee = currentUser()",
)
JIRA_PRIORITY_ORDER = os.getenv("JIRA_PRIORITY_ORDER", "ASC")

# GOOGLE
GOOGLE_CALENDAR_ID = os.getenv("GOOGLE_CALENDAR_ID", "primary")

# CALENDAR PARAMETERS
WORKING_HOURS_FROM = os.getenv("WORKING_HOURS_FROM", 9)
WORKING_HOURS_TO = os.getenv("WORKING_HOURS_FROM", 17)

WORKING_DAYS_START_WEEKDAY = os.getenv("WORKING_DAYS_START_WEEKDAY", 0)
WORKING_DAYS_END_WEEKDAY = os.getenv("WORKING_DAYS_START_WEEKDAY", 4)

# ALGORITHM PARAMETERS
TIME_PER_ESTIMATION_POINT = os.getenv("TIME_PER_ESTIMATION_POINT", None)
ALGORITHM = os.getenv("ALGORITHM", "NAIVE_GREEDY_WITH_SPLIT")  # NAIVE_GREEDY, NAIVE_GREEDY_WITH_SPLIT
