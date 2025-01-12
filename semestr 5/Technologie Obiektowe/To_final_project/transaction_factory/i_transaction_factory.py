from abc import abstractmethod

class ITransactionFactory:
    @abstractmethod
    def create_transaction(type, description, amount, category):
        pass