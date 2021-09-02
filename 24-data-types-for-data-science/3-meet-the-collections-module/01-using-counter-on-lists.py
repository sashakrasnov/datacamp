'''
Using Counter on lists

Counter is a powerful tool for counting, validating, and learning more about the elements within a dataset that is found in the collections module. You pass an iterable (list, set, tuple) or a dictionary to the Counter. You can also use the Counter object similarly to a dictionary with key/value assignment, for example counter[key] = value.

A common usage for Counter is checking data for consistency prior to using it, so let's do just that. In this exercise, you'll be using data from the Chicago Transit Authority on ridership.
'''

import csv

with open('../datasets/cta_daily_station_totals.csv' ,'r') as csvfile:
    stations = [row['stationname'] for row in csv.DictReader(csvfile)]

'''
INSTRUCTIONS

*   Import the Counter object from collections.
*   Print the first ten items from the stations list.
*   Create a Counter of the stations list called station_count.
*   Print the station_count.
'''

# Import the Counter object
from collections import Counter

# Print the first ten items from the stations list
print(stations[:10])

# Create a Counter of the stations list: station_count
station_count = Counter(stations)

# Print the station_count
print(station_count)
