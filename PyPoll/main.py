# main.py for PyPoll

# Import the os module

import os

# Import the module for reading CSV files

import csv

csvpath = os.path.join('Resources','election_data.csv')

# Create a dictionary to store totals

candidate_data = {
"Khan":0,
"Correy":0,
"Li":0,
"O'Tooley":0
}

# Read CSV using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    # Set month counter and variables
    total_votes = 0

# Create and Open Text Output File

# Set Path for Text File
    file_name = os.path.join("Analysis","PyPoll.txt")

# Open Text File
    f = open(file_name,'w', encoding="utf8")


# Read each row of data after the header
    for row in csvreader:
        total_votes += 1
        candidate_choice = str(row[2])
        candidate_data[candidate_choice] = candidate_data[candidate_choice] + 1

            
# Print Summary Terminal Report Header and Total Votes

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

# Print and Write Election Results

for x in candidate_data:
    name = str(x)
    votes = candidate_data[x]
    percent_votes = round((votes/total_votes)*100)

    print(f"{name}: {percent_votes}.000% ({votes:,})")
    f.write(f"{name}: {percent_votes}.000% ({votes:,})")
    f.write("\n")

print("-----------------------------------")
f.write("-----------------------------------")

#f.write("\n")
#f.write(f"Winner: {winner_name}")
#f.write("\n")
#f.write("-----------------------------------")

 # Close Text File

f.close()
