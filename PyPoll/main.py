# main.py for PyPoll

# Import the os module

import os

# Import the module for reading CSV files

import csv

csvpath = os.path.join('Resources','election_data.csv')

# Read using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    # Set month counter and variables
    total_votes = 0
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    OTooley_votes = 0
    winner_name = "     "

    # Read each row of data after the header
    for row in csvreader:

        total_votes += 1

        if row[2] == "Khan":
            Khan_votes += 1
            
        if row[2] == "Correy":
            Correy_votes += 1

        if row[2] == "Li":
            Li_votes += 1
        
        if row[2] == "O'Tooley":
            OTooley_votes += 1
        

election = {
    "Khan": Khan_votes,
    "Correy": Correy_votes,
    "Li": Li_votes,
    "O'Tooley": OTooley_votes

}

    # Print Summary Report

print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {total_votes:,}")
print("-----------------------------------")

for x in election:
    print(x[0],x[1],end="\n" )


print("-----------------------------------")
print(f"Winner: {winner_name}")
print("-----------------------------------")

   

# Set Path for Text File
file_name = os.path.join("Analysis","PyPoll.txt")

# Open Text File
f = open(file_name,'w', encoding="utf8")

# Write Report to Text File

f.write("Election Results")
f.write("\n")
f.write("-----------------------------------")
f.write("\n")
f.write(f"Total Votes: {total_votes:,}")
f.write("\n")
f.write("-----------------------------------")
f.write("\n")

f.write(f"Khan: {round(Khan_Percent)}.000% ({Khan_votes:,})")
f.write("\n")
f.write(f"Correy: {round(Correy_Percent)}.000% ({Correy_votes:,})")
f.write("\n")
f.write(f"Li: {round(Li_Percent)}.000% ({Li_votes:,}")
f.write("\n")
f.write(f"O'Tooley: {round(OTooley_Percent)}.000% ({OTooley_votes:,})")
f.write("\n")

f.write("-----------------------------------")
f.write("\n")
f.write(f"Winner: {winner_name}")
f.write("\n")
f.write("-----------------------------------")

 # Close Text File

f.close()
