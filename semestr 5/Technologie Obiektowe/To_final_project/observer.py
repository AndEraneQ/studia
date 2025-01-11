class Observable:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify_observers(self, data):
        for observer in self.observers:
            observer.update(data)


class BudgetObserver:
    def __init__(self, update_callback):
        self.update_callback = update_callback

    def update(self, data):
        self.update_callback(data)
