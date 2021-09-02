'''
Creating dictionaries of an unknown structure

Occasionally, you'll need a structure to hold nested data, and you may not be certain that the keys will all actually exist. This can be an issue if you're trying to append items to a list for that key. You might remember the NYC data that we explored in the video. In order to solve the problem with a regular dictionary, you'll need to test that the key exists in the dictionary, and if not, add it with an empty list.

You'll be working with a list of entries that contains ridership details on the Chicago transit system. You're going to solve this same type of problem with a much easier solution in the next exercise.
'''

import csv

with open('../datasets/cta_daily_station_totals.csv' ,'r') as csvfile:
    entries = [(row['date'], row['stationname'], row['rides']) for row in csv.DictReader(csvfile)]

'''
INSTRUCTIONS

*   Create an empty dictionary called ridership.
*   Iterate over entries, unpacking it into the variables date, stop, and riders.
*   Check to see if the date already exists in the ridership dictionary. If it does not exist, create an empty list for the date key.
*   Append a tuple consisting of stop and riders to the date key of the ridership dictionary.
*   Print the ridership for '03/09/2016'.
'''

# Create an empty dictionary: ridership
ridership = {}

# Iterate over the entries
for date, stop, riders in entries:
    # Check to see if date is already in the dictionary
    if date not in ridership:
        # Create an empty list for any missing date
        ridership[date] = []
    # Append the stop and riders as a tuple to the date keys list
    ridership[date].append((stop, riders))
    
# Print the ridership for '03/09/2016'
print(ridership['03/09/2016'])
