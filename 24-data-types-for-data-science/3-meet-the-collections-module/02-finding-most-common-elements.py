'''
Finding most common elements

Another powerful usage of Counter is finding the most common elements in a list. This can be done with the .most_common() method.

Practice using this now to find the most common stations in a stations list.
'''

import csv

with open('../datasets/cta_daily_station_totals.csv' ,'r') as csvfile:
    stations = [row['stationname'] for row in csv.DictReader(csvfile)]

'''
INSTRUCTIONS

*   Import the Counter object from collections.
*   Create a Counter of the stations list called station_count.
*   Print the 5 most common elements.
'''

# Import the Counter object
from collections import Counter

# Create a Counter of the stations list: station_count
station_count = Counter(stations)

# Find the 5 most common elements
print(station_count.most_common(5))
