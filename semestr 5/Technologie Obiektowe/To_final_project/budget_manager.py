import json
from observer import Observable
from transaction import TransactionBase

class BudgetManager(Observable):
    _instance = None

    @staticmethod
    def get_instance():
        if BudgetManager._instance is None:
            BudgetManager._instance = BudgetManager()
        return BudgetManager._instance

    def __init__(self):
        if BudgetManager._instance is not None:
            raise Exception("Singleton already instantiated!")
        super().__init__()
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.notify_observers(self.transactions)

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            data = [transaction.to_dict() for transaction in self.transactions]
            json.dump(data, file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.transactions = [TransactionBase.from_dict(t) for t in data]
            self.notify_observers(self.transactions)

    def reset_budget(self):
        self.transactions = []
        self.notify_observers(self.transactions)

