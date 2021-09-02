'''
Transforming your Data Containers to Month and Location

Now let's flip your crime_data list into a dictionary keyed by month with a list of location values for each month, and filter down to the records for the year 2016. Remember you can use the shell to look at the crime_data list, such as crime_data[1][4] to see the location of the crime in the second item of the list (since lists start at 0).
'''

import csv

csvfile = open('../datasets/crime_sampler.csv', 'r')

crime_data = []

for row in csv.reader(csvfile):
    crime_data.append(row)
    
crime_data.pop(0)

'''
INSTRUCTIONS

*   Import defaultdict from collections and datetime from datetime.
*   Create a dictionary that defaults to a list called locations_by_month.
*   Loop over the crime_data list:
    *   Convert the first element to a date object exactly like you did in the previous exercise.
    *   If the year is 2016, set the key of locations_by_month to be the month of date and append the location (fifth element of row) to the values list.
*   Print the dictionary. This has been done for you, so hit 'Submit Answer' to see the result!
'''

# Import necessary modules
from collections import defaultdict
from datetime import datetime

# Create a dictionary that defaults to a list: locations_by_month
locations_by_month = defaultdict(list)

# Loop over the crime_data list
for row in crime_data:
    # Convert the first element to a date object
    date = datetime.strptime(row[0], '%m/%d/%Y %I:%M:%S %p')
    
    # If the year is 2016 
    if date.year == 2016:
        # Set the dictionary key to the month and add the location (fifth element) to the values list
       locations_by_month[date.month].append(row[4])
    
# Print the dictionary
print(locations_by_month)