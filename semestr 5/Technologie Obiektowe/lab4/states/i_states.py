from abc import ABC, abstractmethod

class IStates(ABC):
    @abstractmethod
    def get_state(self, vehicle):
        pass

class BusyState(IStates):
    def get_state(self, vehicle):
        vehicle.state = BusyState()

class AvailableState(IStates):
    def get_state(self, vehicle):
        vehicle.state = AvailableState()