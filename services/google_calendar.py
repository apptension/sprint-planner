from __future__ import print_function
from datetime import date, timedelta, datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from model.calendar_schedule import CalendarSchedule
from model.calendar_entry import CalendarEntry


class GoogleCalendarEventsClient:
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    creds = None
    start_date = None
    end_date = None

    def __init__(self, start_date=None, end_date=None):
        if not start_date:
            self.start_date = datetime.utcnow()
        if not end_date:
            self.end_date = (datetime.utcnow() + timedelta(days=14))
        self.authenticate()

    def _get_calendar_service(self):
        return build('calendar', 'v3', credentials=self.creds)

    def authenticate(self):
        if os.path.exists('token.json'):
            self.creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(self.creds.to_json())

    @staticmethod
    def _get_event_duration_minutes(start, end):
        return int((end - start).seconds / 60)

    def get_events(self):
        service = self._get_calendar_service()
        events_result = service.events().list(calendarId='primary',
                                              timeMin=self.start_date.isoformat() + 'Z',
                                              timeMax=self.end_date.isoformat() + 'Z',
                                              singleEvents=True,
                                              orderBy='startTime'
                                              ).execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
        result = []
        for event in events:
            start = event['start'].get('dateTime', None)
            end = event['end'].get('dateTime', None)
            if start and end:
                datetime_format = '%Y-%m-%dT%H:%M:%S%z'
                start = datetime.strptime(start, datetime_format)
                end = datetime.strptime(end, datetime_format)
                duration = self._get_event_duration_minutes(start, end)
                result.append({"start": start, "end": end, "duration": duration})
        return result

    def get_calendar_list(self, working_hours_from=9, working_hours_to=17, working_days_from=0, working_days_to=4):
        def daterange(start_date, end_date):
            for n in range(int((end_date - start_date).days)):
                yield start_date + timedelta(n)

        start_date = self.start_date
        end_date = self.end_date
        calendar_entries = []
        dates = []
        for single_date in daterange(start_date, end_date):
            weekday = single_date.weekday()
            if working_days_from <= weekday <= working_days_to:
                dates.append(single_date)
                calendar_entries.append(CalendarEntry(False, None, ((working_hours_to - working_hours_from) * 60)))

        events = self.get_events()
        return CalendarSchedule(calendar_entries)
