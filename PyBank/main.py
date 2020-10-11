# Import OS and CSV modules
import os
import csv
# define variables
old_month = 0
new_month = 0
month_count = 0
total_profit = 0
profit_change_current_month = 0
profit_change_prior_month = 0
profit_change_running_total = 0
profit_change_average = 0
profit_total_aggregate = 0
profit_change_highest = 0
profit_change_highest_month = 0
profit_change_lowest = 0
profit_change_lowest_month = 0
# set filepath to data file and start looping through rows to do awesome stuff
budgetdatapath = "PyBank/Resources/BudgetData.csv" # point to budget data csv file
with open(budgetdatapath) as csvfile:
    budgetdata = csv.reader(csvfile, delimiter=",")
    budgetdataheader = next(budgetdata) #skip header row
    # loop through rows in budget data csv file, and perform iterative steps on each row
    for row in budgetdata:
        month_count = month_count + 1
        total_profit += int(row[1])
        if month_count == 1: #for first month: +1 to running month count, and set profit total aggregate equal to current month profit 
            print(f"month count ",month_count)
            new_month = int(row[1])
            print(f"new month ",new_month)
            profit_change_current_month = new_month - old_month
            profit_total_aggregate = new_month = int(row[1])
            print(f"profit total aggregate", profit_total_aggregate)
            print("------------------------------")
        elif month_count != 1: #for months 2+, : +1 to running month count, and do some other stuff
            print(f"month count ",month_count)
            old_month = new_month
            print(f"old month", old_month)
            new_month = int(row[1])
            print(f"new month ",new_month)
            if month_count == 2: # ignore month 2 for average profit change
                profit_change_prior_month = 0
                print(f"profit change prior month ",profit_change_prior_month)
            else: 
                profit_change_prior_month = profit_change_current_month
                print(f"profit change prior month ",profit_change_prior_month)
            profit_change_current_month = new_month - old_month
            print(f"profit change current month", profit_change_current_month)
            if profit_change_current_month > profit_change_highest: # find month with largest month-over-month profit increase
                profit_change_highest = profit_change_current_month
                profit_change_highest_month = str(row[0])
            else: profit_change_highest = profit_change_highest
            if profit_change_current_month < profit_change_lowest: # find month with largest month-over-month profit decrease
                profit_change_lowest = profit_change_current_month
                profit_change_lowest_month = str(row[0])
            else: profit_change_lowest = profit_change_lowest
            print(f"profit change highest", profit_change_highest_month, profit_change_highest)
            profit_change_running_total = profit_change_running_total + profit_change_current_month
            print(f"profit change running total",profit_change_lowest_month, profit_change_running_total)
            profit_change_average = profit_change_running_total / (month_count - 1)
            print(f"profit change average ",profit_change_average)
            profit_total_aggregate = profit_total_aggregate + new_month
            print(f"profit total aggregate", profit_total_aggregate)
            print("------------------------------")
        else:
            print("error")
# Print table summary
print("------------------------------")
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: ", month_count)
print("Total Profit/Loss: $", profit_total_aggregate)
print("Average Change: $",profit_change_average)
print("Greatest Increase in profits: ",profit_change_highest_month, "($", profit_change_highest, ")")
print("Greatest Decrease in Profits: ",profit_change_lowest_month, "($", profit_change_lowest, ")")
print("------------------------------")