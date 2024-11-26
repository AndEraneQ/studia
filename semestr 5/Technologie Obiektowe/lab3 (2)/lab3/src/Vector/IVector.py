from abc import ABC, abstractmethod

class IVector(ABC):
    @abstractmethod
    def abs(self) -> float:
        pass
    
    @abstractmethod
    def cdot(self, other) -> float:
        pass
    
    @abstractmethod
    def getComponents(self) -> list[float]:
        pass
    