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


def category_insights():
    cat_totals = {}

    with open(file_path,"r") as file:
        reader = csv.reader(file)

        for row in reader:
            amount = float(row[0])
            category = row[1]

            if category in cat_totals:
                cat_totals[category] += amount
            else:
                cat_totals[category] = amount
        
    return cat_totals

    