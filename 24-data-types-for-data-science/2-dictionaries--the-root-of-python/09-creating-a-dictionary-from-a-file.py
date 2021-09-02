'''
Creating a dictionary from a file

The csv module also provides a way to directly create a dictionary from a CSV file with the DictReader class. If the file has a header row, that row will automatically be used as the keys for the dictionary. However, if not, you can supply a list of keys to be used. Each row from the file is returned as a dictionary. Using DictReader can make it much easier to read your code and understand what data is being used, especially when compared to the numbered indexes you used in the prior exercise.

Your job in this exercise is to create a dictionary directly from the data file using DictReader. NOTE: The misspellings are from the original data, and this is a very common issue. Again, the baby_names dictionary has already been created for you.
'''

baby_names = dict()

'''
INSTRUCTIONS

*   Import the Python csv module.
*   Create a Python file object in read mode for the baby_names.csv called csvfile.
*   Loop over a csv DictReader on csvfile. Inside the loop:
    *   Print each row.
    *   Add the 'RANK' of each row as the key and 'NAME' of each row as the value to the existing dictionary.
*   Print the dictionary keys.
'''

# Import the python CSV module
import csv

# Create a python file object in read mode for the `baby_names.csv` file: csvfile
csvfile = open('../datasets/baby_names.csv' ,'r')

# Loop over a DictReader on the file
for row in csv.DictReader(csvfile):
    # Print each row 
    print(row)
    # Add the rank and name to the dictionary: baby_names
    baby_names[row['RANK']] = row['NAME']

# Print the dictionary keys
print(baby_names.keys())
