import os
import csv

budget_data_csv = os.path.join('budget_data.csv')
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0

with open(budget_data_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
    first_row = next(csvreader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in csvreader:
        # Track the total months
        total_months += 1
        total_net += int(row[1])
        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]

#Average change
monthly_average = sum(net_change_list) / len(net_change_list)

#Greatest increase in Profits
greatest_increase = max(net_change_list)

#Greatest Descrease in Profits
greatest_decrease = min(net_change_list)

print("Financial Analysis")
print("-----------------------------------")
print("Total Months:", total_months)
print("Total:", total_net)
print("Average Change:", monthly_average)
print("Greatest Increase in Profits:", greatest_increase)
print("Greatest Decrease in Profits:", greatest_decrease)
