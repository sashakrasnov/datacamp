'''
Powerful Ordered popping

Where OrderedDicts really shine is when you need to access the data in the dictionary in the order you added it. OrderedDict has a .popitem() method that will return items in reverse of which they were inserted. You can also pass .popitem() the last=False keyword argument and go through the items in the order of how they were added.

Here, you'll use the ridership_date OrderedDict you created in the previous exercise.
'''

import csv

with open('../datasets/cta_daily_station_totals.csv' ,'r') as csvfile:
    entries = [(row['date'], int(row['rides'])) for row in csv.DictReader(csvfile)]

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
    
'''
INSTRUCTIONS

*   Print the first key in ridership_date (Remember to make keys a list before slicing).
*   Pop the first item from ridership_date and print it.
*   Print the last key in ridership_date.
*   Pop the last item from ridership_date and print it.
'''

# Print the first key in ridership_date
print(list(ridership_date.keys())[0])

# Pop the first item from ridership_date and print it
print(ridership_date.popitem(last=False))

# Print the last key in ridership_date
print(list(ridership_date.keys())[-1])

# Pop the last item from ridership_date and print it
print(ridership_date.popitem())
