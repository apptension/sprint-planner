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


## License
[MIT](https://choosealicense.com/licenses/mit/)