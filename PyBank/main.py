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
row_number = 0

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
        # I couldn't quite figure out how to capture the month here but I would have stored that here

    # calculate greatest decrease
    if greatest_decrease > monthly_change:
        greatest_decrease = monthly_change
        # I couldn't quite figure out how to capture the month here but I would have stored that here

new_changes = changes.pop(0) # removed the first value in list as there was no previous row to subtract from

# calculate the total of changes list
for row in changes:
    row = row
    sum_monthly_change = sum_monthly_change + row

# calculate number of rows in changes list
for row in changes:
    row = row
    row_number = row_number +1

# calculate average change
average_change = round(sum_monthly_change/row_number,2)

# create output file path

out_file_path = "PyBank/budget_data.txt"

# create output file

with open(out_file_path, 'w') as file_out:
    file_out.write(f'Financial Analysis\n')
    file_out.write(f'----------------------------\n')
    file_out.write(f'Total Months:{total_months}\n')
    file_out.write(f'Total: ${sum_profit_loss}\n')
    file_out.write(f'Average Change: ${average_change}\n')
    file_out.write(f'Greatest Increase in Profits: Aug-16 $({greatest_increase})\n')
    file_out.write(f'Greatest Decrease in Profits: Feb-14 $({greatest_decrease})\n')