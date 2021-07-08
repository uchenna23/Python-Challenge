#import csv and os
import csv
import os
#select csv file
budget_csv= os.path.join("Resources", "budget_data.csv")
#create lists
date = []
profit = []
monthly_change = []
#set variables = 0
count = 0
net_profit = 0
last_month_profit = 0
current_month_profit = 0
change_in_profit = 0
#read csv file
with open(budget_csv,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for line in csvreader:
        count = count + 1
        net_profit = int(line[1]) + net_profit
        date.append(line[0])
        current_month_profit= int(line[1])
        if count != 1:
            
            change_in_profit = current_month_profit - last_month_profit
            monthly_change.append(change_in_profit)
        last_month_profit = int(line[1])
    
avg_change = sum(monthly_change)/ len(monthly_change)

greatest_increase_profits = max(monthly_change)
greatest_decrease_profits = min(monthly_change)

increase_date = date[monthly_change.index(greatest_increase_profits)]
decrease_date = date[monthly_change.index(greatest_decrease_profits)]
#Clean up the data
print("Financial Analysis")
print("------------------------------------")
print("Total Months: " + str(count))
print("Total Profits: " + "$" + str(net_profit))
print("Average Change: " + "$" + str(int(avg_change)))
print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")

