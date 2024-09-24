from html.parser import incomplete


class Income:
    def __init__(self):
        self.budget = 0
        self.list_income_amounts = []


    def __str__(self):
        return f"Income is {self.budget}"


    def add_income(self, amount):
        self.budget += amount
        self.list_income_amounts.append(amount)
        Income.display_budget(self)
        #print(self.budget)
        return self.budget


    def display_all_entries(self):
        for entry in self.list_income_amounts:
            print(entry)


    def display_budget(self):
        print(f"Your budget is {self.budget}")


    def remaining_budget(self, expenses):

        self.budget -= expenses
        print(f"Your remaining budget = {self.budget}")
        return self.budget