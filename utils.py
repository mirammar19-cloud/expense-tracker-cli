import csv

file_path = "data/expenses.csv"

def add_expense(amount,category,date):
    with open(file_path,"a",newline= "") as file:
        writer = csv.writer(file)
        writer.writerow([amount,category,date])