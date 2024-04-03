import csv

# set filepath
budget_file_path = "PyBank/Resources/budget_data.csv"

#set variables
total_months = 0

# open and read csv
with open(budget_file_path) as budget_file:
    csv_file = csv.reader(budget_file)
    next(csv_file)

    for row in csv_file:
        total_months = total_months +1




#print(f'Financial Analysis')
#print(f'----------------------------')
print(f'Total Months:', total_months)
#print(f'Total:')
#print(f'Average Change:')
#print(f'Greatest Increase in Profits:')
#print(f'Greatest Decrease in Profits:')



#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)