'''
Leveraging attributes on namedtuples

Once you have a namedtuple, you can write more expressive code that is easier to understand. Remember, you can access the elements in the tuple by their name as an attribute. For example, you can access the date of the namedtuples in the previous exercise using the .date attribute.

Here, you'll use the tuples you made in the previous exercise to see how this works.
'''

import csv

with open('../datasets/cta_daily_station_totals.csv' ,'r') as csvfile:
    entries = [(row['date'], row['stationname'], row['rides']) for row in csv.DictReader(csvfile)]

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
    
'''
INSTRUCTIONS

*   Iterate over the first twenty items in the labeled_entries list.
    *   Print each item's stop.
    *   Print each item's date.
    *   Print each item's riders.
'''

# Iterate over the first twenty items in labeled_entries
for item in labeled_entries[:20]:
    # Print each item's stop
    print(item.stop)

    # Print each item's date
    print(item.date)

    # Print each item's riders
    print(item.riders)
    