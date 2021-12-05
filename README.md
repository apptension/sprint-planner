# Sprint planner

Sprint planner is a Python script for planning your Jira tasks based on your calendar availability.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
python3 -m venv .venv
python3 -m pip install -r requirements.txt
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
- `JIRA_PROJECT` - Project ID to fill default JQL query and to get start/end dates from current sprint.
- `JIRA_ESTIMATE_FIELD` - Name of the field with estimation points, default value: `timeoriginalestimate`.
- `JIRA_ISSUES_JQL` - Custom JQL query for fetching issues from Jira.
- `JIRA_PRIORITY_ORDER` - Set to DESC if your most important tasks has greater priority id than less important ones.

### Google
- `GOOGLE_CALENDAR_ID` - ID of Google Calendar you want to use, default set to `primary`
- `GOOGLE_ATTENDEE_EMAIL` - Email address of user to check if event is accepted for them. Default value `None` which means that all events will be loaded.

### Calendar parameters
- `WORKING_HOURS_FROM` - Your start work hour, default value `9`.
- `WORKING_HOURS_TO` - Your end work hour, default value `17`.
- `WORKING_DAYS_START_WEEKDAY` - First day of working week, default value `0` which means `Monday`.
- `WORKING_DAYS_END_WEEKDAY` - Last day of working week, default value `5` which means `Friday`.
- `WITH_BREAK` - Include break timeslot each day. Default value `True`
- `BREAK_TIME` - Length of break in minutes. Default value `30`
- `BREAK_AFTER` - Minimum hour in day for the break. Default value `13`

### Algorithm parameters
- `TIME_PER_ESTIMATION_POINT` - How long it should take to do one estimation point. Default value `None` which means that value will be counted proportionally to free time.
- `ALGORITHM` - Possible values: `NAIVE_GREEDY`, `NAIVE_GREEDY_WITH_SPLIT`, Default value: `NAIVE_GREEDY_WITH_SPLIT` 
- `MIN_CONSIDERABLE_SLOT_TIME` - Dont plan work for slots less than `MIN_CONSIDERABLE_SLOT_TIME` minutes. Defaults to 0

### Focus optimisation parameters
- `FOCUS_TIME_CALENDAR_START` - Start date for focus optimisation in `%Y-%m-%dT%H:%M:%S.%fZ` format (i.e. 2021-12-10T00:00:00.000Z)
- `FOCUS_TIME_CALENDAR_END` - End date for focus optimisation in `%Y-%m-%dT%H:%M:%S.%fZ` format (i.e. 2021-12-10T00:00:00.000Z)
- `FOCUS_TIME_STORY_POINTS_CAPACITY` - Total Story Points to use in `<FOCUS_TIME_CALENDAR_START, FOCUS_TIME_CALENDAR_END>` range

## Future improvements
- [ ] Introduce more complex algorithms to plan the sprint
- [ ] Support for planning multiple developers (whole team) at once
- [ ] Consider time cost for regaining focus after each meeting

## License
[MIT](https://choosealicense.com/licenses/mit/)