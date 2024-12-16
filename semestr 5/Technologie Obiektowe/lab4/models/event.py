import random
from states.i_states import AvailableState

class Event:
    def __init__(self):
        self.event_type = None
        self.event_location = None
        self.is_complete = False
        self.duration = 0
        self.time_elapsed = 0
        self.assigned_vehicles = []

    def mark_complete(self):
        self.is_complete = True

        for vehicle in self.assigned_vehicles:
            if vehicle.current_event == self:
                vehicle.current_state = AvailableState()
                vehicle.current_event = None
                vehicle.notify_observers()

    def generate_random_event(self):
        self.event_type = random.choices(["PZ", "MZ", "AF"], [0.3, 0.7, 0.05])[0]
        
        lat = random.uniform(49.95855025648944, 50.154564013341734)
        lon = random.uniform(19.688292482742394, 20.02470275868903)
        self.event_location = (lat, lon)

        if self.event_type == "AF":
            self.duration = random.randint(1, 3)
        else:
            self.duration = random.randint(5, 25)

    def update(self):
        self.time_elapsed += 1
        if self.time_elapsed >= self.duration:
            self.mark_complete()

    def __str__(self):
        return f"Event {self.event_type} in {self.event_location}"