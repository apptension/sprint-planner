from llist import sllist

class CalendarSchedule:
    schedule = None

    def __init__(self, entries):
        self.schedule = sllist(entries)

    @property
    def total_time(self):
        return sum(entry.length for entry in self.schedule)

    @property
    def total_free_time(self):
        entry_free_time = lambda entry : 0 if entry.busy else entry.length
        return sum(entry_free_time(entry) for entry in self.schedule)

    @property
    def total_busy_time(self):
        return self.total_time - self.total_free_time

    @property
    def entries(self):
        return self.schedule