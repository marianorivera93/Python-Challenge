#import budget data
import os
import csv

#List variables
candidates = []
votes={}

#Count Votes
total_votes=0

election_csv= os.path.join('Resources', 'election_data.csv')
with open(election_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter= ',')
    next (csvreader, None)
    for row in csvreader:
        candidate = row[2]
        if candidate not in votes:
            votes[candidate]=1
        else:
            votes[candidate]+=1
        total_votes+=1

results= []
results.append("Election Results\n-------------------")
results.append(f"Total Votes: {total_votes}\n------------")

#Print 
print (f"Election Results")
print (f"---------------------------")
print (f"Total Votes: {total_votes}")
print (f"---------------------------")
for key, value in votes.items():
    print(f"{key}: {value/total_votes: 0.3%} ({value})")
print (f"---------------------------")
print (f"Winner: {max(votes, key=votes.get)}")
print (f"---------------------------")

#.txtFile
output_path= election_csv

write_electionCSV = f"{output_path}resultstext"

filewriter = open(write_electionCSV, mode = 'w')

filewriter.write("Election Results\n")
filewriter.write("-----------------------\n")
filewriter.write(f"Total Votes: {total_votes}\n")
for key, value in votes.items():
    filewriter.write(f"{key}: {value/total_votes: 0.3%} ({value})\n")
filewriter.write("-----------------------\n")
filewriter.write(f"Winner: {max(votes, key=votes.get)}\n")
filewriter.write("-----------------------\n")

filewriter.close()
