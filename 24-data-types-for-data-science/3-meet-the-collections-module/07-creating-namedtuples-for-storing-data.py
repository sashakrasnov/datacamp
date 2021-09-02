'''
Creating namedtuples for storing data

Often times when working with data, you will use a dictionary just so you can use key names to make reading the code and accessing the data easier to understand. Python has another container called a namedtuple that is a tuple, but has names for each position of the tuple. You create one by passing a name for the tuple type and a list of field names.

For example, Cookie = namedtuple("Cookie", ['name', 'quantity']) will create a container, and you can create new ones of the type using Cookie('chocolate chip', 1) where you can access the name using the name attribute, and then get the quantity using the quantity attribute.

In this exercise, you're going to restructure the transit data you've been working with into namedtuples for more descriptive code.
'''

import csv

with open('../datasets/cta_daily_station_totals.csv' ,'r') as csvfile:
    entries = [(row['date'], row['stationname'], row['rides']) for row in csv.DictReader(csvfile)]

'''
INSTRUCTIONS

*   Import namedtuple from collections.
*   Create a namedtuple called DateDetails with a type name of DateDetails and fields of 'date', 'stop', and 'riders'.
*   Create a list called labeled_entries.
*   Iterate over entries, unpacking it into date, stop, and riders.
*   Create a new DateDetails namedtuple instance for each entry and append it to labeled_entries.
*   Print the first 5 items in labeled_entries. This has been done for you, so hit 'Submit Answer' to see the result!
'''

# Import namedtuple from collections
from collections import namedtuple

# Create the namedtuple: DateDetails
DateDetails = namedtuple('DateDetails', ['date', 'stop', 'riders'])

# Create the empty list: labeled_entries
labeled_entries = []

# Iterate over the entries
for date, stop, riders in entries:
    # Append a new DateDetails namedtuple instance for each entry to labeled_entries
    labeled_entries.append(DateDetails(date, stop, riders))
    
# Print the first 5 items in labeled_entries
print(labeled_entries[:5])

