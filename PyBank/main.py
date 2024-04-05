import csv

# set filepath
budget_file_path = "PyBank/Resources/budget_data.csv"

# set variables
total_months = 0
sum_profit_loss = 0
profit_loss_list = []
changes = []
greatest_increase = 0
greatest_decrease = 0
monthly_change = 0
sum_monthly_change = 0
change = 0

# open and read csv
with open(budget_file_path) as budget_file:
    csv_file = csv.reader(budget_file)
    header = next(csv_file)

    for row in csv_file:
        total_months = total_months +1
        month_date = row [0]
        profit_loss = row [1]
        sum_profit_loss= int(profit_loss)+ sum_profit_loss
        profit_loss_list.append(int(row[1]))

previous_row = 0
for row in profit_loss_list:
    row = row
    monthly_change = row - previous_row
    changes.append(monthly_change)
    previous_row = row
new_changes = changes.pop(0)

for row in changes:
    row = row
    sum_monthly_change = sum_monthly_change + row

row_number = 0
for row in changes:
    row = row
    row_number = row_number +1

average_change = round(sum_monthly_change/row_number,2)
print(average_change)




        



#print(f'Financial Analysis')
#print(f'----------------------------')
#print(f'Total Months:',total_months)
#print(f'Total:', $ sum_profit_loss)
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