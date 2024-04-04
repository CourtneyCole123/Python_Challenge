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
profit_loss_dict = {}
offset_list = []
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
print(changes)







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