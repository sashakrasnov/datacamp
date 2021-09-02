'''
Safely appending to a key's value list

Often when working with dictionaries, you know the data type you want to have each key be; however, some data types such as lists have to be initialized on each key before you can append to that list.

A defaultdict allows you to define what each uninitialized key will contain. When establishing a defaultdict, you pass it the type you want it to be, such as a list, tuple, set, int, string, dictionary or any other valid type object.
'''

import csv

with open('../datasets/cta_daily_station_totals.csv' ,'r') as csvfile:
    entries = [(row['date'], row['stationname'], row['rides']) for row in csv.DictReader(csvfile)]

'''
INSTRUCTIONS

*   Import defaultdict from collections.
*   Create a defaultdict with a default type of list called ridership.
*   Iterate over the list entries, unpacking it into the variables date, stop, and riders, exactly as you did in the previous exercise.
    *   Use stop as the key of the ridership dictionary and append riders to its value.
*   Print the first 10 items of the ridership dictionary. You can use the .items() method for this. Remember, you have to convert ridership.items() to a list before slicing.
'''

# Import defaultdict
from collections import defaultdict

# Create a defaultdict with a default type of list: ridership
ridership = defaultdict(list)

# Iterate over the entries
for date, stop, riders in entries:
    # Use the stop as the key of ridership and append the riders to its value
    ridership[stop].append(riders)
    
# Print the first 10 items of the ridership dictionary
print(list(ridership.items())[:10])