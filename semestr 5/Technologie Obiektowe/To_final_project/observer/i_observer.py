from abc import abstractmethod

class IObservable:
    @abstractmethod
    def attach(self, observer: 'IObserver') -> None:
        pass

    @abstractmethod
    def detach(self, observer: 'IObserver') -> None:
        pass

    @abstractmethod
    def notify_observers(self, data) -> None:
        pass

class IObserver:
    @abstractmethod
    def update(self, data) -> None:
        pass
