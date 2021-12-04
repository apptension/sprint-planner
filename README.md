# Sprint planner

Sprint planner is a Python script for planning your Jira tasks based on your calendar availability.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
python -m pip install -r requirements.txt
```
For Google Calendar integration:

1. Create Google Cloud Platform project with the Google Calendar API enabled. To create a project and enable an API, refer to [Create a project and enable the API](https://developers.google.com/workspace/guides/create-project)
2. Create authorization credentials for a desktop application. To learn how to create credentials for a desktop application, refer to [Create credentials](https://developers.google.com/workspace/guides/create-credentials).
3. Save file with credentials as `credentials.json` in main project folder.

## Usage

```python
python3 planner.py
```

## Known issues
- all Google Calendar events from user main calendar are being fetched, without checking if user is attending
- problems with GCal events which lasts more than one day

## Environment variables
### Jira
- `JIRA_TOKEN` - User authorization token, can be generated [here](https://id.atlassian.com/manage-profile/security/api-tokens).

- `JIRA_SERVER` - Your Jira server name i.e. https://organization.atlassian.net/.

- `JIRA_USER` - Your user email.

- `JIRA_PROJECT` - Project ID to fill default JQL query. Not required if you set `JIRA_ISSUES_JQL` variable.  

- `JIRA_ESTIMATE_FIELD` - Name of the field with estimation points, default value: `timeoriginalestimate`.

- `JIRA_ISSUES_JQL` - Custom JQL query for fetching issues from Jira.

- `JIRA_PRIORITY_ORDER` - Set to DESC if your most important tasks has greater priority id than less important ones.

## License
[MIT](https://choosealicense.com/licenses/mit/)