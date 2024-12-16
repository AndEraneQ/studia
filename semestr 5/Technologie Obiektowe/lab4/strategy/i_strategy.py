from abc import ABC, abstractmethod

class IDispatcher(ABC):
    @abstractmethod
    def assign_vehicles_to_event(self, event, stations):
        pass
    