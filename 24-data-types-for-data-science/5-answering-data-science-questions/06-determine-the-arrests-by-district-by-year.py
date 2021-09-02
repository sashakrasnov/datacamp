'''
Determine the Arrests by District by Year

Using your crimes_by_district dictionary from the previous exercise, you'll now determine the number arrests in each City district for each year. Counter is already imported for you. You'll want to use the IPython Shell to explore the crimes_by_district dictionary to determine how to check if an arrest was made.
'''

import csv

from collections import defaultdict, Counter
from datetime import datetime

csvfile = open('../datasets/crime_sampler.csv', 'r')

crimes_by_district = defaultdict(list)

for row in csv.DictReader(csvfile):
    district = row.pop('District')
    crimes_by_district[district].append(row)

'''
INSTRUCTIONS

*   Loop over the crimes_by_district dictionary, unpacking it into the variables district and crimes.
    *   Create an empty Counter object called year_count.
    *   Loop over the crimes:
        *   If there was an arrest,
            *   Convert crime['Date'] to a datetime object called year.
            *   Add the crime to the Counter for the year, by using year as the key of year_count.
    *   Print the Counter. This has been done for you, so hit 'Submit Answer' to see the result!
'''

# Loop over the crimes_by_district using expansion as district and crimes
for district, crimes in crimes_by_district.items():
    # Print the district
    print(district)
    
    # Create an empty Counter object: year_count
    year_count = Counter()
    
    # Loop over the crimes:
    for crime in crimes:
        # If there was an arrest
        if crime['Arrest'] == 'true':
            # Convert the Date to a datetime and get the year
            year = datetime.strptime(crime['Date'], '%m/%d/%Y %I:%M:%S %p').year
            # Increment the Counter for the year
            year_count[year] += 1
            
    # Print the counter
    print(year_count)