from transaction import Income, Expense

class TransactionFactory:
    
    @staticmethod
    def create_transaction(type, description, amount, category):
        if type == "Dochód":
            return Income(description, amount, category)
        elif type == "Wydatek":
            return Expense(description, amount, category)
        else:
            raise ValueError(f"Nieznany typ transakcji: {type}")
