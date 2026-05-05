from utils import add_expense
from utils import view_expense
from utils import total_expense
from utils import category_insights
import matplotlib.pyplot as plt


def main():
    print("---EXPENSE TRACKER---")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Total Expense")
    print("4. Category Insights")
    print("5. View Charts")
    print("0. Exit")
    choice = int(input("Enter Preffered Choice: "))

    if choice == 1:
        try:
            amount = float(input("Enter Amount:$ "))
            category = input("Enter Category: ")
            date = input("Enter Date (DD-MM-YYYY): ")

            add_expense(amount,category,date)
            print("Expense added successfully!")
        except(ValueError):
            print("Invalid input. Amount must be a number!")
    elif choice == 2:
        output = view_expense()
        for row in output:
            amt,cat,_date = row
            print(f" AMOUNT : ${float(amt):<12,.2f}CATEGORY : {cat:<12}DATE : {_date}")
    elif choice == 3:
        total = total_expense()
        print(f"TOTAL: ${total:,.2f}")
    elif choice == 4:
        insights = category_insights()
        print("---Category Insights---")

        for cat, total in insights.items():
            print(f"Category : {cat:<12} Total : {float(total):,.2f}")
    elif choice == 5:
        insights = category_insights()

        category = list(insights.keys())
        values = list(insights.values())

        plt.bar(category, values)
        plt.title("Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.show()
    
    else:
        exit

if __name__ == "__main__":
    main()
