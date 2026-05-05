from utils import add_expense
from utils import view_expense
from utils import total_expense

def main():
    print("---EXPENSE TRACKER---")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Total Expense")
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
            print(f" AMOUNT : ${amt:<12}CATEGORY : {cat:<12}DATE : {_date}")
    elif choice == 3:
        total = total_expense()
        print(f"TOTAL: ${total:,.2f}")
    else:
        exit

if __name__ == "__main__":
    main()
