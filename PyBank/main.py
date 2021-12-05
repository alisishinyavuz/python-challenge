#import modules
import os
import csv
import statistics as st

csvpath = os.path.join("Resources","budget_data.csv")
#Lists to store the data
profit = []
months = []
profit_changes = []


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")  

    #Skip the header row  from csv file
    csv_header = next(csvreader) 


    for row in csvreader:

        #Add date
        months.append(row[0])

        #Add Profit/Loss
        profit.append(int(row[1]))


total_profit = 0
for i in profit:
    total_profit += i 



profit_changes = [profit[i+1]- profit[i] for i in range(len(profit)-1)]

#Calculate the greatest increase in profits 
max_profit = max(profit_changes)

#Calculate the greatest decrease in loss 
min_profit = min(profit_changes)

#Calculate the total months included in the data set
total_months = len(months)

#Calculate the net amount of Profit/Losses over the period of time
net_amount = sum(profit)

#Calculate the average change per month
average_change = sum(profit_changes) / len(months)



#Using the index of the greatest increase to find the date
index_max = profit_changes.index(max_profit)
max_month = months[index_max]


#Using the index of the greatest decrease to find the date
index_min = profit_changes.index(min_profit)
min_month = months[index_min]

greatest_increase_profits = max(profit_changes)
greatest_decrease_profits = min(profit_changes)

increase_month = months[profit_changes.index(greatest_increase_profits)]
decrease_month = months[profit_changes.index(greatest_decrease_profits)]

#print the analysis to the terminal and export a text file with the results

analysis =[]
analysis.append("----------------------------------------------------------")
analysis.append(f"Total Months:{total_months}")
analysis.append(f"Total:${total_profit}")
analysis.append(f"Average Change: ${round((average_change),2)}")
analysis.append(f"Greatest Increase in Profits:{increase_month}(${greatest_increase_profits})")
analysis.append(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease_profits})")


file_name = "Analysis.txt"

with open(file_name, "w") as file:
    for item in analysis:
        print(item)
        file.write(item + "\n")


    

