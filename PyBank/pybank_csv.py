import os
import csv

csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')
    

with open('budget_data.csv', 'r') as csvfile:
    csv_reader = csv.Dictreader(csvfile, delimiter=',') 
    total = []
    for row_count, row in enumerate(csvreader, start=1)
        value = int(row['Profit/Losses'])
        totals.append(value)    

print("Financial Analysis")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print("Total Months: {}".format(row_count))
print("Total: {}".format(sum(totals)))
print("Average Change: ")
print("Greatest Increase in Profits: ")
print("Greatest Decrease in Profits: ")
        

output_path = os.path.join("Analysis.txt")    

with open(output_file, 'w', newline='') as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
    text_file.write("Total Months: {}\n".format(row_count))
    text_file.write("Average: {}\n")
    text_file.write("Greatest Increase in Profits: {}\n")
    text_file.write("Greastest Decrease in Profits: {}\n")

  
