from abc import ABC, abstractmethod

class ITransaction(ABC):
    @abstractmethod
    def to_dict(self):
        pass
    @abstractmethod
    def from_dict(self):
        pass
    @abstractmethod
    def transaction_type(self) -> str:
        pass
