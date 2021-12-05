import settings
from dataclasses import dataclass, replace
from llist import sllist

from model.calendar_entry import CalendarEntry


class CalendarSchedule:
    schedule = None

    def __init__(self, entries):
        self.schedule = sllist(entries)

    @property
    def total_time(self):
        return sum(entry.length for entry in self.schedule)

    @property
    def total_free_time(self):
        entry_free_time = lambda entry: 0 if entry.busy else entry.length
        return sum(entry_free_time(entry) for entry in self.schedule)

    @property
    def total_time_spent_on_issues(self):
        entry_issue_time = lambda entry: entry.length if entry.busy_on_issue else 0
        return sum(entry_issue_time(entry) for entry in self.schedule)

    @property
    def total_time_spent_on_meetings(self):
        entry_meeting_time = lambda entry: entry.length if entry.busy_on_meeting else 0
        return sum(entry_meeting_time(entry) for entry in self.schedule)

    @property
    def total_busy_time(self):
        return self.total_time - self.total_free_time

    @property
    def entries(self):
        return self.schedule

    def get_entry_node_at_index(self, index):
        return self.entries.nodeat(index)

    # finds available schedule entry with at least <min_length> length between given offsets
    # returns available entry node with position
    def find_free_slot_between(self, min_length, start_offset, end_offset):
        length_position = 0
        node_index = None
        for index, entry in enumerate(self.schedule):
            length_position += entry.length
            if end_offset >= length_position >= start_offset and length_position - start_offset >= min_length:
                if entry.length >= min_length and not entry.busy:
                    node_index = index
                    break
        return (self.get_entry_node_at_index(node_index), length_position) if node_index else (None, None)

    # finds available schedule entry with at least <min_length> length
    # returns available entry node
    def find_free_slot(self, min_length):
        node_index = next(
            (index for index, entry in enumerate(self.schedule) if entry.length >= min_length and not entry.busy),
            None,
        )
        return self.get_entry_node_at_index(node_index) if node_index != None else None

    # finds consecutive available slots (allowing to be interrupted by meetings)
    # returns available slots nodes
    def find_free_multi_slot(self, min_length):
        slots = []
        time_to_distribute = min_length

        for index, entry in enumerate(self.schedule):
            if entry.busy_on_issue:
                slots = []
                time_to_distribute = min_length
            elif not entry.busy_on_meeting and not entry.too_short:
                slots.append(self.get_entry_node_at_index(index))
                time_to_distribute -= entry.length

                if time_to_distribute <= 0:
                    return slots

        # no matching multi-slot found
        return None

    def spread_entry_over(self, target_nodes, new_entry):
        remaining_entry = replace(new_entry)

        for target_node in target_nodes:
            target_node_length = target_node.value.length
            if target_node_length >= remaining_entry.length:
                # whole remaining entry can fit into the slot
                return self.add_entry_within(target_node, remaining_entry)
            else:
                # requires splitting
                entry_to_add = replace(remaining_entry, length=target_node_length)
                remaining_entry = replace(remaining_entry, length=remaining_entry.length - target_node_length)
                self.add_entry_within(target_node, entry_to_add)

    def add_entry_within(self, target_node, new_entry):
        target_entry = target_node.value
        inserted_node = self.schedule.insertbefore(new_entry, target_node)
        shortened_target_entry = replace(target_entry, length=target_entry.length - new_entry.length)
        self.schedule.remove(target_node)
        if shortened_target_entry.length > 0:
            shortened_node = self.schedule.insertafter(shortened_target_entry, inserted_node)
            return inserted_node, shortened_node
        return (inserted_node,)

    def add_entry_inside(self, target_node, new_entry, offset):
        inserted_node, shortened_node = self.add_entry_within(
            target_node,
            CalendarEntry(target_node.value.on_meeting, target_node.value.issue, offset)
        )
        self.add_entry_within(shortened_node, new_entry)
