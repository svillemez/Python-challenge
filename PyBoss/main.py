# main.py for PyBoss

# Import the os module

import os

# Import the module for reading CSV files and set CSV path

import csv

csvpath = os.path.join('Resources','employee_data.csv')

#Create state abbreviation dictionary
us_state_cd = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

# Open CSV Input File Using CSV module

with open(csvpath) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

# Read the header row first 
    csv_header = next(csvreader)

# Set Output File Path for Converted CSV File
    file_name = os.path.join("Analysis","employee_data_converted.csv")

# Open CSV File for Output
    f = open(file_name,'w', encoding="utf8")


# Read each row of data from CSV file and tally votes
    for row in csvreader:
        emp_id = str(row[0])
        name = str(row[1])
        first_name = name[:name.index(" ")]
        last_name = name[name.index(" "):]
# convert DOB YYYY-MM-DD to MM/DD/YYYY
        dob = str(row[2])
        dob_year = (dob[4:])
        dob_day = (dob[-2:])
        dob_mo = (dob[-5:])
        print(dob_mo)
        print(dob_day)
        print(dob_year)
# convert SSN to hide all but last 4 digits
        ssn_in = str(row[3])
        last4 = ssn_in[-4:]
        ssn = str("***") + str("-") + str("**") + str("-") + str(last4)
        state = str(row[4])
        state_cd = str(us_state_cd[state])
# write converted emplyee file
        f.write(f"{emp_id},{first_name},{last_name},{dob_mo}/{dob_day}/{dob_year},{ssn},{state_cd}")
        f.write("\n")
# Close Converted CSV File

f.close()
