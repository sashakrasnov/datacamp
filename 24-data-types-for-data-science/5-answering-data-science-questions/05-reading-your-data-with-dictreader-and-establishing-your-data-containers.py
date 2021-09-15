'''
Reading your Data with DictReader and Establishing your Data Containers
Your data file, crime_sampler.csv contains in positional order: the date, block where it occurred, primary type of the crime, description of the crime, description of the location, if an arrest was made, was it a domestic case, and city district.

You'll now use a DictReader to load up a dictionary to hold your data with the district as the key and the rest of the data in a list. The csv, defaultdict, and datetime modules have already been imported for you.
'''

import csv

from collections import defaultdict
from datetime import datetime

'''
INSTRUCTIONS

*   Create a Python file object in read mode for crime_sampler.csv called csvfile.
*   Create a dictionary that defaults to a list called crimes_by_district.
*   Loop over a DictReader of the CSV file:
    *   Pop 'District' from each row and store it as district.
    *   Append the rest of the data (row) to the district key of crimes_by_district.
'''

# Create the CSV file: csvfile
csvfile = open('../datasets/crime_sampler.csv', 'r')

# Create a dictionary that defaults to a list: crimes_by_district
crimes_by_district = defaultdict(list)

# Loop over a DictReader of the CSV file
for row in csv.DictReader(csvfile):
    # Pop the district from each row: district
    district = row.pop('District')

    # Append the rest of the data to the list for proper district in crimes_by_district
    crimes_by_district[district].append(row)