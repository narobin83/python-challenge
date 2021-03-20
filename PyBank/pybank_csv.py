import os
import csv

csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')
    

with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

   
output_path = os.path.join("..", "PyBank", "analysis.csv")

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['text'])
    
    csvwriter.writerow(['Financial_Analysis'])

print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Total Months:'])

    csvwriter.writerow(['Total:'])

    csvwriter.writerow(['Average Change:'])

    csvwriter.writerow(['Greates Increase in Profits:'])

     csvwriter.writerow(['Greatest Decrease in Profits:'])
