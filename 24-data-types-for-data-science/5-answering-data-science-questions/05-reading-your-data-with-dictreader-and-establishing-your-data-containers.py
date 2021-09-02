'''
Find the Most Common Crimes by Location Type by Month in 2016

Using the locations_by_month dictionary from the prior exercise, you'll now determine common crimes by month and location type. Because your dataset is so large, it's a good idea to use Counter to look at an aspect of it in an easier to manageable size and learn more about it.
'''

import csv

from collections import defaultdict
from datetime import datetime

'''
INSTRUCTIONS

*   Import Counter from collections.
*   Loop over the items from your dictionary, using tuple expansion to unpack locations_by_month.items() into month and locations.
    *   Make a Counter of the locations called location_count.
    *   Print the month.
    *   Print the five most common crime locations.
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
