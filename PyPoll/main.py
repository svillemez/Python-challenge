# main.py for PyPoll

# Import the os module

import os

# Import the module for reading CSV files and Set CSV path

import csv

csvpath = os.path.join('Resources','election_data.csv')

# Create a dictionary to store totals

candidate_data = {
"Correy":0,
"Khan":0,
"Li":0,
"O'Tooley":0
}

# Read CSV using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    # Set month counter and winner vote count
    total_votes = 0
    greatest_vote_total = 0

# Set Path for Text File
    file_name = os.path.join("Analysis","PyPoll.txt")

# Open Text File
    f = open(file_name,'w', encoding="utf8")


# Read each row of data from CSV file and tally votes
    for row in csvreader:
        total_votes += 1
        candidate_choice = str(row[2])
        candidate_data[candidate_choice] = candidate_data[candidate_choice] + 1

# Sort Dictionary by Decending Vote Count
sorted_candidate_data = dict(sorted(candidate_data.items(), key=lambda x: (x[1]), reverse=True))
           
# Print Report Header and Total Votes to Terminal

print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {total_votes:,}")
print("-----------------------------------")

# Write Report Header and Total Votes to Text File

f.write("Election Results")
f.write("\n")
f.write("-----------------------------------")
f.write("\n")
f.write(f"Total Votes: {total_votes:,}")
f.write("\n")
f.write("-----------------------------------")
f.write("\n")

# Print Election Results to Terminal and Write Election Results to Text File

for x in sorted_candidate_data:
    name = str(x)
    votes = int(sorted_candidate_data[x])
    percent_votes = round((votes/total_votes)*100)
    print(f"{name}: {percent_votes}.000% ({votes:,})")
    f.write(f"{name}: {percent_votes}.000% ({votes:,})")
    f.write("\n")
    if votes > greatest_vote_total:
        greatest_vote_total = votes
        winner_name = str(x)

print("-----------------------------------")
f.write("-----------------------------------")


# Print Winner to Terminal and Write Winner to Text File 

print(f"Winner: {winner_name}")
print("-----------------------------------")
f.write("\n")
f.write(f"Winner: {winner_name}")
f.write("\n")
f.write("-----------------------------------")

 # Close Text File

f.close()
