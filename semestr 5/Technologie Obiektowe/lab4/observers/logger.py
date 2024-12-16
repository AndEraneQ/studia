from .i_logger import ILogger

class Logger(ILogger):
    def __init__(self, fire_stations):
        self.fire_stations = fire_stations
        self.logged_events = []
        self.register_vehicles()

    def register_vehicles(self):
        for station in self.fire_stations:
            for vehicle in station.vehicles:
                vehicle.add_observer(self)

    def log_event(self, event):
        print(f"\nIncident: {event.event_type} at {event.event_location}!")

        for station in self.fire_stations:
            print(f"Unit: {station.station_name}")
            for vehicle in station.vehicles:
                if vehicle.is_available():
                    print(f"  {vehicle} is available")
                else:
                    print(f"  {vehicle} is occupied, assigned to: {vehicle.current_event}")
        print("\n")

    def update(self, event):
        pass
