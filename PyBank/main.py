# import modules
import os
import csv

#define variables
months = 0
net_profit_loss = 0
change_profit_loss = 0
total_change_profit_loss = 0
average_change_profits_loss = 0.00
greatest_increase_profits = 0
greatest_decrease_profits = 0
current_profits_loss = 0
previous_profits_loss = 0
date_greatest_increase = 0
date_gratest_decrease = 0

#open csv file
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:

    #read csv file to perform functions
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header row
    csv_header = next(csvreader)

    for row in csvreader:
        #count the number of rows in the file (which equals number of months)
        months += 1

        #calculate total profits and losses over period
        net_profit_loss += int(row[1])

        #compare the profit/loss to the previous row to calculate change
        #set current_profits_loss equal to value in first row (after header)
        current_profits_loss = int(row[1])

        #add conditional to correctly add or subtract the values to find the total amount of change
        if current_profits_loss > previous_profits_loss:
            change_profit_loss = abs(current_profits_loss - previous_profits_loss)
        elif current_profits_loss < previous_profits_loss:
            change_profit_loss = -abs(current_profits_loss - previous_profits_loss)

        #add conditional statement to account for first row being none
        if previous_profits_loss != 0:

        #add this row's change in profit/loss to the total change of profit/loss 
            total_change_profit_loss += change_profit_loss

        #reset the previous profits/loss value to be the current row for the next iteration
        previous_profits_loss = current_profits_loss

        #create conditional to find the greated increase and derease 
        #in change profits/loss
        if change_profit_loss > 0 and change_profit_loss > greatest_increase_profits:
            greatest_increase_profits = change_profit_loss
            date_greatest_increase = str(row[0])
        elif change_profit_loss < 0 and change_profit_loss < greatest_decrease_profits:
            greatest_decrease_profits = change_profit_loss
            date_gratest_decrease = str(row[0])

    #calculate average change in profits/loss, subtract one from months to account
    #for no change on the first month
    average_change_profits_loss = total_change_profit_loss / (months-1)

    #round average change in profits/loss to 2 decimal points
    average_change_profits_loss = round(average_change_profits_loss, 2)
    

#print correct output for assignment
print("Financial Analysis")
print("--------------------")
print(f"Total Months: {months}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${average_change_profits_loss}")
print(f"Greatest Increase in Profits: {date_greatest_increase} (${greatest_increase_profits})")
print(f"Greatest Decrease in Profts: {date_gratest_decrease} (${greatest_decrease_profits})")

#print output to text file
output_path = os.path.join("Analysis", "PyBank_Financial_Analysis.txt")
with open(output_path, 'w') as textfile:
    textfile.write("Financial Analysis\n"
                   "--------------------\n"
                   f"Total Months: {months}\n"
                   f"Total: ${net_profit_loss}\n"
                   f"Average Change: ${average_change_profits_loss}\n"
                   f"Greatest Increase in Profits: {date_greatest_increase} (${greatest_increase_profits})\n"
                   f"Greatest Decrease in Profts: {date_gratest_decrease} (${greatest_decrease_profits})\n")