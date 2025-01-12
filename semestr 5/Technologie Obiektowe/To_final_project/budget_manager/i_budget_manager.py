from abc import abstractmethod

class IBudgetManager:
    @abstractmethod
    def add_transaction(self, transaction):
        pass

    @abstractmethod
    def save_to_file(self, filename: str):
        pass

    @abstractmethod
    def load_from_file(self, filename: str):
        pass

    @abstractmethod
    def reset_budget(self):
        pass
