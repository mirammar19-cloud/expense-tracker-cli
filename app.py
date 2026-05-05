from utils import add_expense

def main():
    print("---EXPENSE TRACKER---")
    choice = input("Would you like to proceed?(y/n): ")

    if choice == "y":
        try:
            amount = float(input("Enter Amount:$ "))
            category = input("Enter Category: ")
            date = input("Enter Date (DD-MM-YYYY): ")

            add_expense(amount,category,date)
            print("Expense added successfully!")
        except(ValueError):
            print("Invalid input. Amount must be a number!")
    else:
        exit

if __name__ == "__main__":
    main()
