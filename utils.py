import csv

file_path = "data/expenses.csv"

def add_expense(amount,category,date):
    with open(file_path,"a",newline= "") as file:
        writer = csv.writer(file)
        writer.writerow([amount,category,date])


def view_expense():
    with open(file_path,"r") as file:
        reader = csv.reader(file)
        rows = []
        for row in reader:
            rows.append(row)
        return rows
    
def total_expense():
    with open(file_path,"r") as file:
        reader = csv.reader(file)
        total = 0
        for row in reader:
            total += float(row[0])
        return total
