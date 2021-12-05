# Sprint planner

Sprint planner is a Python script for planning your Jira tasks based on your calendar availability.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
python -m pip install -r requirements.txt
```
For Google Calendar integration:

1. Create Google Cloud Platform project with the Google Calendar API enabled. To create a project and enable an API, refer to [Create a project and enable the API](https://developers.google.com/workspace/guides/create-project)
2. Create authorization credentials for a desktop application. To learn how to create credentials for a desktop application, refer to [Create credentials](https://developers.google.com/workspace/guides/create-credentials).
3. Save file with credentials as `credentials.json` in main project folder.

For Jira integration:

Set `JIRA_TOKEN`, `JIRA_SERVER` , `JIRA_USER` with proper values. See `Environment variables` section for more details.

## Usage

### Plan sprint work based on JIRA tickets and available calendar time
It generates sprint plan based on your calendar and JIRA tickets.

```python
python3 plan_sprint.py $env_file
```
`$env_file` is optional parameter to be used if there is another path to env file than default `.env`

### Optimise focus time based on your calendar
It generates optimised list of workload you can do, without being distracted by any meeting during an issue work.

```python
python3 optimise_focus_time.py $env_file
```
`$env_file` is optional parameter to be used if there is another path to env file than default `.env`

## Known issues
- all Google Calendar events from user main calendar are being fetched, without checking if user is attending
- problems with GCal events which lasts more than one day
- problems might occurs if Google Calendar events starts before work hours or end after work hours

## Environment variables
### Jira
- `JIRA_TOKEN` - User authorization token, can be generated [here](https://id.atlassian.com/manage-profile/security/api-tokens).
- `JIRA_SERVER` - Your Jira server name i.e. https://organization.atlassian.net/.
- `JIRA_USER` - Your user email.
- `JIRA_PROJECT` - Project ID to fill default JQL query. Not required if you set `JIRA_ISSUES_JQL` variable.
- `JIRA_ESTIMATE_FIELD` - Name of the field with estimation points, default value: `timeoriginalestimate`.
- `JIRA_ISSUES_JQL` - Custom JQL query for fetching issues from Jira.
- `JIRA_PRIORITY_ORDER` - Set to DESC if your most important tasks has greater priority id than less important ones.

### Google
- `GOOGLE_CALENDAR_ID` - ID of Google Calendar you want to use, default set to `primary`

### Calendar parameters
- `WORKING_HOURS_FROM` - Your start work hour, default value `9`.
- `WORKING_HOURS_TO` - Your end work hour, default value `17`.
- `WORKING_DAYS_START_WEEKDAY` - First day of working week, default value `0` which means `Monday`.
- `WORKING_DAYS_END_WEEKDAY` - Last day of working week, default value `5` which means `Friday`.

### Algorithm parameters
- `TIME_PER_ESTIMATION_POINT` - How long it should take to do one estimation point. Default value `None` which means that value will be counted proportionally to free time.
- `ALGORITHM` - Possible values: `NAIVE_GREEDY`, `NAIVE_GREEDY_WITH_SPLIT`, Default value: `NAIVE_GREEDY_WITH_SPLIT` 

## License
[MIT](https://choosealicense.com/licenses/mit/)