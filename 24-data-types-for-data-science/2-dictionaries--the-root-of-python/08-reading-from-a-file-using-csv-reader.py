'''
Reading from a file using CSV reader

Python provides a wonderful module called csv to work with CSV files. You can pass the .reader() method of csv a Python file object and use it as you would any other iterable. To create a Python file object, you use the open() function, which accepts a file name and a mode. The mode is typically 'r' for read or 'w' for write.

Though you won't use it for this exercise, often CSV files will have a header row with field names, and you will need to use slice notation such as [1:] to skip the header row.
'''

baby_names = dict()

'''
INSTRUCTIONS

*   Import the python csv module.
*   Create a Python file object in read mode for baby_names.csv called csvfile.
*   Loop over a csv reader on the file object. Inside the loop:
    *   Print each row.
    *   Add the rank (the 6th element of row) as the key and name (the 4th element of row) as the value to the existing dictionary (baby_names).
*   Print the keys of baby_names.
'''

# Import the python CSV module
import csv

# Create a python file object in read mode for the baby_names.csv file: csvfile
csvfile = open('../datasets/baby_names.csv', 'r')

# Skipping first row, it is a header
csvfile.readline()

# Loop over a csv reader on the file object
for row in csv.reader(csvfile):
    # Print each row 
    print(row)
    # Add the rank and name to the dictionary
    baby_names[row[5]] = row[3]

# Print the dictionary keys
print(baby_names.keys())