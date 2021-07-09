#import csv and os
import csv
import os
#select csvfile
vote_csv = os.path.join("Resources", "election_data.csv")
#create dictionary for candidates and votes
elections = {}
#set variables = 0
total_votes = 0
#create lists
candidates = []
vote_count = []
winners_list = []    
vote_percentage = []
#read csvfile
with open(vote_csv,'r') as csvfile:
    csvreader= csv.reader(csvfile)
    csv_header=next(csvreader)
    for line in csvreader:
        total_votes = total_votes + 1
        if line[2] in elections.keys():
            elections[line[2]] = elections[line[2]] + 1
        else:
            elections[line[2]] = 1
#put dictionary items into lists
for key, value in elections.items():
    candidates.append(key)
    vote_count.append(value)
for x in vote_count:
    vote_percentage.append(round(x/total_votes*100, 1))
#clean the data
new_data = list(zip(candidates, vote_count, vote_percentage))
#place winners in winners list
for name in new_data:
    if max(vote_count) == name[1]:
        winners_list.append(name[0])

winner = winners_list[0]

if len(winners_list) > 1:
    for w in range(1, len(winners_list)):
        winner = winner + ", " + winners_list[w]

output_file = os.path.join('election_results.txt')
with open(output_file, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in new_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

with open(output_file, 'r') as readfile:
    print(readfile.read())