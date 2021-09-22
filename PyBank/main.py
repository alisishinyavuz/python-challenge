#import modules
import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")
#Lists to store the data
profit = []
monthly_changes = []
date = []

#variables
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")  
    csv_header = next(csvreader) 

    for row in csvreader:
        #count the number of the months
        count += 1

        date.append(row[0])
        profit.append(row[1])
        total_profit =total_profit +int(row[1])

        final_profit = int(row[1])
        monthly_change_profits = final_profit - initial_profit

        #Store these monthly changes in a list
        monthly_changes.append(monthly_change_profits)

        total_change_profits = total_change_profits + monthly_change_profits
        initial_profit = final_profit

        #Calculate the average change in profits
        average_change_profits = (total_change_profits/count)
      
        #Find the max and min change in profits and the corresponding dates these changes were obeserved
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)

        increase_date = date[monthly_changes.index(greatest_increase_profits)]
        decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
      
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")


    

