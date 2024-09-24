from income import Income
#from budget_tracker import BudgetTracker

class Expenses:
    def __init__(self):
        self.total_expenses = 0
        self.list_of_expenses = []


    def add_expenses(self, amount):
        income = Income()
        self.total_expenses += amount
        print("Expenses were added to your BudgetTracker")
        income.remaining_budget(self.total_expenses)
        return self.total_expenses


    def delete_expenses(self):
        if expenses in self.total_expenses:
            self.total_expenses.remove(expenses)
            print(f"{expenses} were removed")
            return self.total_expenses


    def display_expenses(self):
        pass

