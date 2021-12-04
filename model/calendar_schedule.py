from dataclasses import replace
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

    def get_entry_node_at_index(self, index):
        return self.entries.nodeat(index)

    def find_free_slot(self, min_length):
        node_index = next((index for index, entry in enumerate(self.schedule) if entry.length >= min_length and not entry.busy), None)
        return self.get_entry_node_at_index(node_index) if node_index != None else None

    def add_entry_within(self, target_node, new_entry):
        target_entry = target_node.value
        inserted_node = self.schedule.insertbefore(new_entry, target_node)
        shortened_target_entry = replace(target_entry, length=target_entry.length - new_entry.length)
        self.schedule.remove(target_node)
        if shortened_target_entry.length > 0:
            self.schedule.insertafter(shortened_target_entry, inserted_node)
            return 2
        return 1
