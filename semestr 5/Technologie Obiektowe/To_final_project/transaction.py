from abc import ABC, abstractmethod

class TransactionBase(ABC):

    def __init__(self, description: str, amount: float, category: str, type: str):
        self.description = description
        self.amount = float(amount)
        self.category = category
        self.type = type

    def to_dict(self) -> dict:
        return {
            "description": self.description,
            "amount": self.amount,
            "category": self.category,
            "type": self.transaction_type()
        }

    @classmethod
    def from_dict(cls, data: dict):

        if not isinstance(data, dict):
            raise ValueError("Input data must be a dictionary.")

        required_keys = {"description", "amount", "category", "type"}
        if not required_keys.issubset(data):
            raise KeyError(f"Dictionary must contain keys: {', '.join(required_keys)}")
        
        if data["type"] == "Dochód":
            return Income(data["description"], data["amount"], data["category"])
        elif data["type"] == "Wydatek":
            return Expense(data["description"], data["amount"], data["category"])
        else:
            raise ValueError(f"Unknown transaction type: {data['type']}")

    @abstractmethod
    def transaction_type(self) -> str:
        pass

    def __str__(self) -> str:
        return f"{self.transaction_type()} - {self.description}: {self.amount:.2f} zł ({self.category})"


class Income(TransactionBase):
    
    def __init__(self, description: str, amount: float, category: str):
        super().__init__(description, amount, category, type="Dochód")

    def transaction_type(self) -> str:
        return "Dochód"


class Expense(TransactionBase):
    
    def __init__(self, description: str, amount: float, category: str):
        super().__init__(description, amount, category, type="Wydatek")

    def transaction_type(self) -> str:
        return "Wydatek"
