# Import OS and CSV modules
import os
import csv
# read in budgetdata.csv
budgetdatapath = "PyBank/Resources/BudgetData.csv"
with open(budgetdatapath) as csvfile:
    budgetdata = csv.reader(csvfile, delimiter=",")
    for row in budgetdata:
        print(row[1])