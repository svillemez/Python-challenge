# main.py for PyBoss

# Import the os module

import os

# Import the module for reading CSV files and set CSV path

import csv

csvpath = os.path.join('Resources','employee_data.csv')

# Read CSV using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

# Set Path for Converted CSV File
    file_name = os.path.join("Analysis","employee_data_converted.csv")

# Open Text File
    f = open(file_name,'w', encoding="utf8")


# Read each row of data from CSV file and tally votes
    for row in csvreader:
        emp_id = str(row[0])
        first_name = str(row[1])
        last_name = str(row[1])
        dob = str(row[2]
        ssn = str("***-**-") + str(row[3])
        state = 

        f.write(f{emp_id},{first_name},{last+name},

# Print Report Header and Total Votes to Terminal
 

# Write Report Header and Total Votes to Text File

# Move to next row
f.write("\n")


# Print Election Results to Terminal and Write Election Results to Text File

for x in sorted_candidate_data:
    name = str(x)
    votes = int(sorted_candidate_data[x])
    percent_votes = round((votes/total_votes)*100)
    f.write(f"{name}: {percent_votes}.000% ({votes:,})")
    f.write("\n")

 # Close Converted CSV File

f.close()
