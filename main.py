from BudgetTracker.income import Income
from BudgetTracker.expenses import Expenses



def main():
    income = Income()
    expenses = Expenses()

    while True:
        print("BudgetTracker Menu:")
        print("1. Display Budget")
        print("2. Add income")
        print("3. Add expense")
        print("4. exit")
        choice = input("Please choose from the Menu (1-4): ")
        if choice == "1":
            income.display_budget()
        elif choice == "2":
            user_income = int(input("What income would you like to add? "))
            income.add_income(user_income)
            #income.display_budget()
        elif choice == "3":
            user_expenses = int(input("What expenses would you like to add? "))
            expenses.add_expenses(user_expenses)
        elif choice == "4":
            print("Bye bye")
            break
        else:
            print("Wrong answer!!")



if __name__ == "__main__":
    main()