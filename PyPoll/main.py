# import modules
import os
import csv

#define variables
total_votes = 0
winner = 0
candidates_dict = {}
popular_vote = 0

#open csv file
csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile: 

    #read csv file to perform functions
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header row
    csv_header = next(csvreader)

    #loop through csv file
    for row in csvreader:

        #count the total number of votes (which equals number of rows exluding header)
        total_votes += 1

        #find the different candidates and add them to the candidates dictionary
        candidate = str(row[2])

        #check if candidate in dict. If not, add to dict and add first vote to value
        if candidate not in candidates_dict:
            candidates_dict[candidate] = 0
            candidates_dict[candidate] += 1
        
        #if candidate is already in dictionary, add one to vote count
        else:
            candidates_dict[candidate] += 1

#print results. Loop through dictionary to print according to directions. 
print("Election Results")
print("-----------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------")
for candidate, votes in candidates_dict.items():
    print(f"{candidate}: {round((votes/total_votes)*100, 3)}% ({votes})")
print("-----------------------")
for candidate, votes in candidates_dict.items():
    if votes > 0 and votes > popular_vote:
        popular_vote = votes
        winner = candidate
print(f"Winner: {winner}")
print("-----------------------")

#print to text file
output_path = os.path.join("Analysis", "PyPoll_Financial_Analysis.txt")
with open(output_path, 'w') as textfile:
    textfile.write((f"Election Results\n"
                    "-----------------------\n"
                    f"Total Votes: {total_votes}\n"
                    "-----------------------\n"))
    for candidate, votes in candidates_dict.items():
        textfile.write(f"{candidate}: {round((votes/total_votes)*100, 3)}% ({votes})\n")
    textfile.write("-----------------------\n")
    for candidate, votes in candidates_dict.items():
        if votes > 0 and votes > popular_vote:
            popular_vote = votes
            winner = candidate
    textfile.write(f"Winner: {winner}\n")
    textfile.write("-----------------------\n")