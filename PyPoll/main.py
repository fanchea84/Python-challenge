#Modules
import os
import csv

#Set path to BudgetData.csv
csvpath = os.path.join("PyBank", "Resources", "BudgetData.csv")

#Open BudgetData.csv
with open(csvpath) as csvfile:
    BudgetData = csv.reader(csvfile, delimiter=',')
    csv_header = next(BudgetData)

    for row in BudgetData:
        print(row[0])
        