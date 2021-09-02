'''
Working with OrderedDictionaries

Recently in Python 3.6, dictionaries were made to maintain the order in which the keys were inserted; however, in all versions prior to that you need to use an OrderedDict to maintain insertion order.

Let's create a dictionary of all the stop times by route and rider, then use it to find the ridership throughout the day.
'''

import csv

with open('../datasets/cta_daily_station_totals.csv' ,'r') as csvfile:
    entries = [(row['date'], int(row['rides'])) for row in csv.DictReader(csvfile)]

'''
INSTRUCTIONS

*   Import OrderedDict from collections.
*   Create an OrderedDict called ridership_date.
*   Iterate over the list entries, unpacking it into date and riders.
*   If a key does not exist in ridership_date for the date, set it equal to 0 (if only you could use defaultdict here!)
*   Add riders to the date key of ridership_date.
*   Print the first 31 records. Remember to convert the items into a list.
'''

# Import OrderedDict from collections
from collections import OrderedDict

# Create an OrderedDict called: ridership_date
ridership_date = OrderedDict()

# Iterate over the entries
for date, riders in entries:
    # If a key does not exist in ridership_date, set it to 0
    if not date in ridership_date:
        ridership_date[date] = 0
        
    # Add riders to the date key in ridership_date
    ridership_date[date] += riders
    
# Print the first 31 records
print(list(ridership_date.items())[:31])

