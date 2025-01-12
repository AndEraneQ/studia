from abc import abstractmethod

class IBudgetApp:
    @abstractmethod
    def __init__(self, root):
        pass

    @abstractmethod
    def _setup_main_panel(self):
        pass

    @abstractmethod
    def _setup_summary_panel(self):
        pass

    @abstractmethod
    def toggle_category_field(self, selected_type):
        pass

    @abstractmethod
    def clear_placeholder(self, entry, placeholder_text):
        pass

    @abstractmethod
    def add_transaction(self):
        pass

    @abstractmethod
    def update_transaction_list(self, transactions):
        pass

    @abstractmethod
    def remove_transaction(self, index):
        pass

    @abstractmethod
    def update_summary(self):
        pass

    @abstractmethod
    def update_chart(self, canvas, filter_type):
        pass

    @abstractmethod
    def save_to_file(self):
        pass

    @abstractmethod
    def load_from_file(self):
        pass

    @abstractmethod
    def reset_budget(self):
        pass
