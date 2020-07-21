# main.py for PyBank

# Import the os module

import os

# Import the module for reading CSV files

import csv

# Set csvpath

csvpath = os.path.join('Resources', 'budget_data.csv')

# Read using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    # Set month counter and variables
    period_count = 0
    total_profit = 0
    total_profit_change = 0
    last_month_profit = 0
    greatest_pos_change = 0
    greatest_neg_change = 0


    # Read each row of data after the header
    for row in csvreader:
        total_profit = total_profit + int(row[1])
        period_count += 1

        if int(row[1]) - last_month_profit > greatest_pos_change:
            greatest_pos_change = int(row[1]) - last_month_profit
            greatest_pos_month = str(row[0])

        if int(row[1]) - last_month_profit < greatest_neg_change:
            greatest_neg_change = int(row[1]) - last_month_profit
            greatest_neg_month = str(row[0])

        if period_count >= 2:
            total_profit_change = total_profit_change + int(row[1]) - last_month_profit

        last_month_profit = int(row[1])

    average_profit_change = total_profit_change/(period_count - 1)


    # Print Summary Report

    print("Financial Analysis")
    print("-----------------------------------")

    print(f"Total Months: {period_count}")

    print(f"Total: ${total_profit:,}")

    print(f"Average Change: ${round(average_profit_change,2)}")

    print(f"Greatest Increase in Profits: {greatest_pos_month} (${greatest_pos_change:,})")

    print(f"Greatest Decrease in Profits: {greatest_neg_month} (${greatest_neg_change:,})")

