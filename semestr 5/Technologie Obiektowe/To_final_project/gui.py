from tkinter import Tk, StringVar, END, Canvas
from tkinter import ttk
from budget_manager import BudgetManager
from transaction_factory import TransactionFactory
from observer import BudgetObserver
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import defaultdict


class BudgetApp:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title("Menadżer Budżetu Domowego")
        self.root.geometry("1300x900")
        self.root.configure(bg="#f4f4f9")

        # Style configuration
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=("Arial", 10), background="#4CAF50", foreground="white", borderwidth=2)
        style.map("TButton", background=[("active", "#45a049")])
        style.configure("TLabel", font=("Arial", 12), background="#f4f4f9", foreground="#333")
        style.configure("TFrame", background="#f4f4f9")
        style.configure("TEntry", font=("Arial", 10))
        style.configure("TOptionMenu", font=("Arial", 10))
        style.configure("TListbox", font=("Arial", 10), background="#ffffff", foreground="#333", borderwidth=1, relief="solid")

        # Budget manager and observer
        self.budget_manager = BudgetManager.get_instance()
        self.observer = BudgetObserver(self.update_transaction_list)
        self.budget_manager.attach(self.observer)

        # Transaction settings
        self.transaction_types = ["Wydatek", "Dochód", "Wydatek"]
        self.expensesCategories = ["Żywność", "Transport", "Rozrywka", "Zdrowie", "Inne"]
        self.incomesCategories = ["Wypłata", "Inwestycje", "Oszczędności", "Inne"]
        self.transaction_buttons = []

        # Main application frames
        self.main_frame = ttk.Frame(root, padding=10)
        self.main_frame.pack(side="left", fill="y", padx=10, pady=10)

        self.summary_frame = ttk.Frame(root, padding=10)
        self.summary_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Setup UI Panels
        self._setup_main_panel()
        self._setup_summary_panel()

    def _setup_main_panel(self):
    # Główna ramka z polami do wprowadzania danych
        input_frame = ttk.Frame(self.main_frame)
        input_frame.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="ew")

        self.transaction_type_var = StringVar(value=self.transaction_types[0])
        self.transaction_type_menu = ttk.OptionMenu(
            input_frame, self.transaction_type_var, *self.transaction_types, command=self.toggle_category_field
        )
        self.transaction_type_menu.grid(row=0, column=0, padx=10, pady=5)

        self.transaction_description = ttk.Entry(input_frame, width=30)
        self.transaction_description.insert(0, "Wpisz nazwę transakcji...")
        self.transaction_description.bind("<FocusIn>", lambda event: self.clear_placeholder(self.transaction_description, "Wpisz nazwę transakcji..."))
        self.transaction_description.grid(row=0, column=1, padx=10, pady=5)

        self.transaction_amount = ttk.Entry(input_frame, width=15)
        self.transaction_amount.insert(0, "Wpisz kwotę...")
        self.transaction_amount.bind("<FocusIn>", lambda event: self.clear_placeholder(self.transaction_amount, "Wpisz kwotę..."))
        self.transaction_amount.grid(row=0, column=2, padx=10, pady=5)

        self.selectedCategories = self.expensesCategories
        self.category_var = StringVar(value=self.selectedCategories[0])
        self.category_menu = ttk.OptionMenu(input_frame, self.category_var, *self.selectedCategories)
        self.category_menu.grid(row=0, column=3, padx=10, pady=5)

        self.add_button = ttk.Button(input_frame, text="Dodaj Transakcję", command=self.add_transaction)
        self.add_button.grid(row=0, column=4, padx=10, pady=5)

        # Sekcja przycisków do operacji na danych
        button_frame = ttk.Frame(self.main_frame)
        button_frame.grid(row=1, column=0, columnspan=2, pady=(10, 20), sticky="ew")

        self.save_button = ttk.Button(button_frame, text="Zapisz do pliku", command=self.save_to_file)
        self.save_button.grid(row=0, column=0, padx=10, pady=5)

        self.load_button = ttk.Button(button_frame, text="Wczytaj z pliku", command=self.load_from_file)
        self.load_button.grid(row=0, column=1, padx=10, pady=5)

        self.reset_button = ttk.Button(button_frame, text="Resetuj Budżet", command=self.reset_budget)
        self.reset_button.grid(row=0, column=2, padx=10, pady=5)

        # Sekcja transakcji (dynamiczna lista z przewijaniem)
        transaction_list_frame = ttk.LabelFrame(self.main_frame, text="Lista transakcji")
        transaction_list_frame.grid(row=2, column=0, columnspan=2, pady=10, sticky="nsew")

        # Tworzenie canvas z paskami przewijania
        canvas = Canvas(transaction_list_frame, bg="#f4f4f9", highlightthickness=0)  # Tło canvas na kolor tła interfejsu
        canvas.pack(side="left", fill="both", expand=True)

        # Dodanie scrollbara pionowego
        y_scrollbar = ttk.Scrollbar(transaction_list_frame, orient="vertical", command=canvas.yview)
        y_scrollbar.pack(side="right", fill="y")


        canvas.configure(yscrollcommand=y_scrollbar.set)

        # Ramka wewnątrz canvas do przechowywania transakcji
        self.transactions_frame = ttk.Frame(canvas, style="TFrame")  # Stylowana ramka z dopasowaniem do tła
        self.transactions_frame.bind(
            "<Configure>",
            lambda event: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=self.transactions_frame, anchor="nw")

        # Styl transakcji
        style = ttk.Style()
        style.configure("TFrame", background="#f4f4f9")

        # Konfiguracja dynamicznego układu w sekcji głównej
        self.main_frame.rowconfigure(2, weight=1)
        self.main_frame.columnconfigure(0, weight=1)


    def _setup_summary_panel(self):
        # Summary header
        ttk.Label(self.summary_frame, text="Podsumowanie", font=("Arial", 16, "bold")).pack(pady=10)

        # Total budget
        self.total_label = ttk.Label(self.summary_frame, text="Całkowity Budżet: 0.00 zł")
        self.total_label.pack(pady=5)

        # Expense chart
        ttk.Label(self.summary_frame, text="Wykres Wydatków", font=("Arial", 14)).pack(pady=5)

        self.expense_label = ttk.Label(self.summary_frame, text="Całkowite Wydatki: 0.00 zł")
        self.expense_label.pack(pady=5)

        self.expense_canvas = Canvas(self.summary_frame, width=400, height=300, bg="#f4f4f9", borderwidth=0)
        self.expense_canvas.pack(pady=10)

        # Income chart
        ttk.Label(self.summary_frame, text="Wykres Dochodów", font=("Arial", 14)).pack(pady=5)

        self.income_label = ttk.Label(self.summary_frame, text="Całkowite Wpływy: 0.00 zł")
        self.income_label.pack(pady=5)

        self.income_canvas = Canvas(self.summary_frame, width=400, height=300, bg="#f4f4f9", borderwidth=0)
        self.income_canvas.pack(pady=10)

    def toggle_category_field(self, selected_type):
        # Sprawdzamy, jaki typ transakcji jest wybrany
        if selected_type == "Dochód":
            self.selectedCategories = self.incomesCategories
        else:
            self.selectedCategories = self.expensesCategories

        # Ustawiamy wartość zmienną z wybraną kategorią, pierwszą z nowej listy
        self.category_var.set(self.selectedCategories[0])

        # Zmiana opcji w OptionMenu, żeby wyświetlało nowe kategorie
        self.category_menu['menu'].delete(0, 'end')  # Usuń stare opcje
        for category in self.selectedCategories:  # Dodaj nowe
            self.category_menu['menu'].add_command(label=category, command=lambda c=category: self.category_var.set(c))

        # Aktualizowanie interfejsu, po zmianie listy kategorii
        self.category_menu.grid(row=0, column=3, padx=10, pady=5)

    def clear_placeholder(self, entry, placeholder_text):
        if entry.get() == placeholder_text:
            entry.delete(0, END)

    def add_transaction(self):
        transaction_type = self.transaction_type_var.get()
        description = self.transaction_description.get().strip()
        amount_text = self.transaction_amount.get().strip()
        category = self.category_var.get()

        try:
            amount = float(amount_text)
            factory = TransactionFactory()
            transaction = factory.create_transaction(transaction_type, description, amount, category)
            self.budget_manager.add_transaction(transaction)
            self.transaction_description.delete(0, END)
            self.transaction_amount.delete(0, END)
            self.update_summary()
        except ValueError:
            print("Błędna wartość kwoty!")

    def update_transaction_list(self, transactions):
        for widget in self.transactions_frame.winfo_children():
            widget.destroy()
        print(self.transactions_frame.winfo_children())
        for i, transaction in enumerate(transactions):
            transaction_row = ttk.Frame(self.transactions_frame)
            transaction_row.pack(fill="x", pady=2)

            transaction_label = ttk.Label(transaction_row, text=str(transaction))
            transaction_label.pack(side="left")

            remove_button = ttk.Button(transaction_row, text="Usuń", command=lambda idx=i: self.remove_transaction(idx))
            remove_button.pack(side="right")

    def remove_transaction(self, index):
        self.budget_manager.transactions.pop(index)
        self.update_transaction_list(self.budget_manager.transactions)
        self.update_summary()

    def update_summary(self):
    # Obliczanie całkowitych wydatków i dochodów
        total_expenses = sum(t.amount for t in self.budget_manager.transactions if t.type == "Wydatek")
        total_income = sum(t.amount for t in self.budget_manager.transactions if t.type == "Dochód")

        # Uaktualnienie ogólnego budżetu na etykiecie
        self.total_label.config(text=f"Całkowity Budżet: {total_income - total_expenses:.2f} zł")
        self.income_label.config(text=f"Całkowite Wpływy: {total_income:.2f} zł")
        self.expense_label.config(text=f"Całkowite Wydatki: {total_expenses:.2f} zł")
        
        # Uaktualnienie wykresów dla wydatków i dochodów
        self.update_chart(self.expense_canvas, "Wydatek")
        self.update_chart(self.income_canvas, "Dochód")

    def update_chart(self, canvas, filter_type):
        # Usuń poprzednie wykresy
        for widget in canvas.winfo_children():
            widget.destroy()

        # Filtruj transakcje na podstawie typu
        filtered_transactions = [t for t in self.budget_manager.transactions if t.type == filter_type]

        if not filtered_transactions:
            return  # Brak danych do wyświetlenia, kończymy

        # Grupowanie transakcji według kategorii i sumowanie wartości
        category_totals = defaultdict(float)
        for transaction in filtered_transactions:
            category = transaction.category or "Bez kategorii"
            category_totals[category] += abs(transaction.amount)

        # Dane do wykresu
        labels = list(category_totals.keys())
        values = list(category_totals.values())

        # Tworzenie wykresu
        figure = Figure(figsize=(4, 3), dpi=100)
        subplot = figure.add_subplot(111)

        subplot.pie(values, labels=labels, autopct="%1.1f%%", startangle=140)

        # Przypnij wykres do widgetu Canvas
        chart = FigureCanvasTkAgg(figure, canvas)
        widget = chart.get_tk_widget()
        widget.pack(fill="both", expand=True)
        chart.draw()

    def save_to_file(self):
        self.budget_manager.save_to_file("budget.json")

    def load_from_file(self):
        self.budget_manager.load_from_file("budget.json")
        self.update_summary()
        
    def reset_budget(self):
        self.budget_manager.reset_budget()
        self.update_summary()

