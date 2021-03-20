import os
import csv

csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')
    

with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

   
output_path = os.path.join(",", "output", "budget_data.csv")

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['text'])
    print(writerow)

    csvwriter.writerow(['Financial_Analysis'])
    print(writerow)

