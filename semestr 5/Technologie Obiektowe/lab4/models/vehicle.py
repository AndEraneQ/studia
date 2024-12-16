from states.i_states import BusyState
from states.i_states import AvailableState

class Vehicle:
    def __init__(self, identifier):
        self.current_state = AvailableState()
        self.current_event = None
        self.observers = []
        self.identifier = identifier

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

    def is_available(self):
        return isinstance(self.current_state, AvailableState)

    def assign_to_event(self, event):
        self.current_state = BusyState()
        self.current_event = event
        event.assigned_vehicles.append(self)
        self.notify_observers()

    def complete_assigned_task(self):
        if self.current_event:
            self.current_event.mark_complete()
        self.current_state = AvailableState()
        self.current_event = None
        self.notify_observers()

    def update_vehicle_state(self):
        self.current_state.get_state(self)

    def __str__(self):
        return f"{self.identifier}"

