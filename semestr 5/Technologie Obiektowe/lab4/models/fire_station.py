from states.i_states import AvailableState
from states.i_states import BusyState
from .vehicle import Vehicle
from strategy.i_strategy import IDispatcher

class FireStation:
    def __init__(self, name, location):
        self.station_name = name
        self.station_location = location
        self.vehicles = [Vehicle(i) for i in range(5)]
        self.station_state = AvailableState()
        self.dispatch_strategy = None

    def set_dispatch_strategy(self, strategy: IDispatcher):
        self.dispatch_strategy = strategy

    def get_available_vehicles(self):
        return [vehicle for vehicle in self.vehicles if vehicle.is_available()]

    def dispatch_vehicle(self, emergency_event):
        for vehicle in self._rescue_vehicles:
            if vehicle.is_available():
                vehicle.assign_to_event(emergency_event)
                return vehicle
        return None
    
    def add_vehicle_observer(self, observer):
        for vehicle in self.vehicles:
            vehicle.add_observer(observer)

    def has_free_vehicle(self):
        return any(vehicle.is_available() for vehicle in self.vehicles)
    
    def __str__(self):
        return f"{self.station_name} at {self.station_location}"
    
    def __repr__(self):
        return self.__str__()