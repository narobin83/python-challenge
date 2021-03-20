import os
import csv

csvpath = os.path.join('..', 'PyBank', 'election_data.csv')

# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

# Function
def Poll(data):

    # Variables
    TotalVotes = 0
    Votes = []
    Candidates = []
    Unique_Candidates = []
    Total_Percent = []
     
    # Loop
    for row in data:

        # Sum Votes
        TotalVotes += 1

        # Append Candidates
        if row[2] not in Unique_Candidates:
            Unique_Candidates.append(row[2])

        # New List
        Votes.append(row[2])

    # Loop
    for candidate in Unique_Candidates:
        Candidates.append(Votes.count(candidate))
        Total_Percent.append(round(Votes.count(candidate)/TotalVotes*100,3))

    # Most Votes
    Winner = Unique_Candidates[Candidates.index(max(Candidates))]
    
    # Print
    print('Election Results')
    print('--------------------------------')
    print(f'Total Votes: {TotalVotes}')
    print('--------------------------------')
    for p in range(len(Unique_Candidates)):
        print(f'{Unique_Candidates[p]}: {Total_Percent[p]}% {Candidates[p]}')
    print('--------------------------------')
    print(f'Winner: {Winner}')
    print('--------------------------------')

    with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        print(csvreader)

    # Read the header row first (skip this step if there is now header)
        csv_header = next(csvfile)
    
        print(f"CSV Header: {csv_header}")

    # Specify the file to write to
        output_path = os.path.join("..", "PyPoll", "election.csv")   

    # Open the file using "write" mode. Specify the variable to hold the contents
        with open(output_path, 'w', newline='') as csvfile:

            # Initialize csv.writer
            csvwriter = csv.writer(csvfile, delimiter=',')

            # Write the first row (column headers)
            csvwriter.writerow(['Election Results'])

            # Write the second row
            csvwriter.writerow(['_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ -'])
            csvwriter.writerow(['Total Votes: 3521001'])
            csvwriter.writerow(['_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ '])
            csvwriter.writerow(['Khan: 63.000% (2218231)'])
            csvwriter.writerow(['Correy: 20.000% (704200)'])
            csvwriter.writerow(['Li: 14.000% (492940)']) 
            csvwriter.writerow(['O Tooley: 3.000% (105630)'])
            csvwriter.writerow(['_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ '])
            csvwriter.writerow(['Winner: Khan'])
            csvwriter.writerow(['_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ '])