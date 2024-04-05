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
previous_row = 0
total_list = []

# open and read csv
with open(budget_file_path) as budget_file:
    csv_file = csv.reader(budget_file)
    header = next(csv_file)

# calculate total months, calculate total profit/loss, & create a profit/loss list
    for row in csv_file:
        total_months = total_months +1
        month_date = row [0]
        profit_loss = row [1]
        sum_profit_loss= int(profit_loss)+ sum_profit_loss
        profit_loss_list.append(int(row[1]))

# using profit/loss list, create a list of changes month to month 
for row in profit_loss_list:
    row = row
    monthly_change = row - previous_row
    changes.append(monthly_change)
    previous_row = row

    # calculate greatest increase
    if greatest_increase < monthly_change:
        greatest_increase = monthly_change

    # calculate greatest decrease
    if greatest_decrease > monthly_change:
        greatest_decrease = monthly_change

new_changes = changes.pop(0) # removed the first value in list as there was no previous row to subtract from

# calculate the total of changes list
for row in changes:
    row = row
    sum_monthly_change = sum_monthly_change + row

# calculate number of rows in changes list
row_number = 0
for row in changes:
    row = row
    row_number = row_number +1

# calculate average change
average_change = round(sum_monthly_change/row_number,2)










#greatest_decrease = min(changes)
#print(greatest_decrease)
#greatest_increase = max(changes)
#print(greatest_increase)

        

# create output file path



# create output file

print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total Months:', total_months)
print(f'Total:', '$', sum_profit_loss)
print(f'Average Change:', '$', average_change)
print(f'Greatest Increase in Profits:', '($',greatest_increase, ')')
print(f'Greatest Decrease in Profits:', '($',greatest_decrease, ')')



#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)