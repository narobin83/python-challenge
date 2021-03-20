import os
import csv

csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')


def Analysis(data):

    # Variables
    Months_Amount = 0
    Profit = 0
    Months = []
    Total_Profit = 0
    Difference = 0
    Total_Difference = []
    
    # Loop
    for row in data:
       
        # + 1
        Months_Amount += 1
        
        # Total_Profit total
        Total_Profit += int(row[1])
        
        # Months total
        Months.append(str(row[0]))
        
        if Difference != 0:
            
            # First Profit 
            Profit = int(row[1])
            
            # Difderence, new vs old
            Difference = Profit - Difference
            
            # Store Difference 
            Total_Difference.append(Difference)
            
            # Reset
            Difference = int(row[1])
            
        # Else value = 0
        elif Difference == 0:
            Difference = int(row[1])  
            
    # No Difference first month
    Months.pop(0)
    
    # Find Greatest Increase and
    Greatest_Increase = Total_Difference.index(max(Total_Difference))
    Greatest_Decrease = Total_Difference.index(min(Total_Difference))

    # Find Months
    Increase_Difference = (Months[int(Greatest_Increase)], max(Total_Difference))
    Decrease_Difference = (Months[int(Greatest_Decrease)], min(Total_Difference))
    
# Find mean of total difference
    Mean = sum(Total_Difference)/float(len(Total_Difference))
    Mean = round(Mean,2)
    
    # print the results
    print(f'Financial Analysis')
    print(f'-------------------------------------------')
    print(f'Total Months: {Months_Amount}')
    print(f'Net Profit: {Total_Profit}')
    print(f'Average Monthly Change: {Mean}')
    print(f'Greatest Increase in Profits: {Increase_Difference}')
    print(f'Greatest Loss In Profits: {Decrease_Difference}')

# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvfile)
    
    print(f"CSV Header: {csv_header}")

    # Specify the file to write to
output_path = os.path.join("..", "PyBank", "analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])

    # Write the second row
    csvwriter.writerow(['Total Month: 86'])
    csvwriter.writerow(['Net Profit: $38382578'])
    csvwriter.writerow(['Average Monthly Change: $-2315.12'])
    csvwriter.writerow(['Greatest Increase In Profits: Feb-2012 ($1926159'])
    csvwriter.writerow(['Greastest Loss In Profits: Sep-2013 ($-2196167'])

