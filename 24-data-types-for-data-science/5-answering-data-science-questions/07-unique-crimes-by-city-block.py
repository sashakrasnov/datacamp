'''
Unique Crimes by City Block

You're in the home stretch!

Here, your data has been reshaped into a dictionary called crimes_by_block in which crimes are listed by city block. Your task in this exercise is to get a unique list of crimes that have occurred on a couple of the blocks that have been selected for you to learn more about. You might remember that you used set() to solve problems like this in Chapter 1.

Go for it!
'''

import csv

from collections import defaultdict, Counter
from datetime import datetime

csvfile = open('../datasets/crime_sampler.csv', 'r')

crimes_by_block = defaultdict(list)

for row in csv.DictReader(csvfile):
    block = row.pop('Block')
    crimes_by_block[block].append(row['Primary Type'])

#print(crimes_by_block)
#quit()

'''
INSTRUCTIONS

*   Create a unique list of crimes for the '001XX N STATE ST' block called n_state_st_crimes and print it.
*   Create a unique list of crimes for the '0000X W TERMINAL ST' block called w_terminal_st_crimes and print it.
*   Find the crimes committed on 001XX N STATE ST but not 0000X W TERMINAL ST. Store the result as crime_differences and print it.
'''

# Create a unique list of crimes for the first block: n_state_st_crimes
n_state_st_crimes = set(crimes_by_block['001XX N STATE ST'])

# Print the list
print(n_state_st_crimes)

# Create a unique list of crimes for the second block: w_terminal_st_crimes
w_terminal_st_crimes = set(crimes_by_block['0000X W TERMINAL ST'])

# Print the list
print(w_terminal_st_crimes)

# Find the differences between the two blocks: crime_differences
crime_differences = n_state_st_crimes.difference(w_terminal_st_crimes)

# Print the differences
print(crime_differences)