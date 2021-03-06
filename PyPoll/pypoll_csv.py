import os
import csv

csvpath = os.path.join("../PyBank/election_data.csv")

poll = {}

total_votes = 0

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        print(csvreader)

    # Read the header row first (skip this step if there is now header)
        csv_header = next(csvfile)
    
        print(f"CSV Header: {csv_header}")

        for row in csvreader:
         total_votes +=1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1

candidates =[]
num_votes = []

for key, value in poll.items():
        candidates.append(key)
        num_votes.append(value)

vote_percent = []
for n in num_votes:
        vote_percent.append(round(n/total_votes*100, 3))

clean_data = list(zip(candidates, num_votes, vote_percent))

winner_list =[]

for name in clean_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

winner = winner_list[0]

if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]

# Specify the file to write to
        output_path = os.path.join("..", "PyPoll", "election.txt")   

    # Open the file using "write" mode. Specify the variable to hold the contents
        with open(output_path, 'w', newline='') as txtfile:
         txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in clean_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')
  
    with open(output_path, 'r') as readfile:
            print(readfile.read()) 