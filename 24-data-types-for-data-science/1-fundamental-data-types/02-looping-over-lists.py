'''
Looping over lists

You can use a for loop to iterate through all the items in a list. You can take that a step further with the sorted() function which will sort the data in a list from lowest to highest in the case of numbers and alphabetical order if the list contains strings.

The sorted() function returns a new list and does not affect the list you passed into the function. You can learn more about sorted() in the Python documentation.

A list of lists, records has been pre-loaded. If you explore it in the IPython Shell, you'll see that each entry is a list of this form:

['2011', 'FEMALE', 'HISPANIC', 'GERALDINE', '13', '75']

The name of the baby ('GERALDINE') is the fourth entry of this list. Your job in this exercise is to loop over this list of lists and append the names of each baby to a new list called baby_names.
'''

with open('../datasets/baby_names.csv') as f:
    records = [r.strip().split(',') for r in f]

'''
INSTRUCTIONS

*   Create an empty list called baby_names.
*   Use a for loop to iterate over each row of records:
    *   Append the name in records to baby_names. The name is stored in the fourth element of row.
*   Print each name in baby_names in alphabetical order. To do this:
    *   Use the sorted() function as part of a for loop to iterate over the sorted names, printing each one.
'''

# Create the empty list: baby_names
baby_names = []

# Loop over records 
for row in records:
    # Add the name to the list
    baby_names.append(row[3])
    
# Sort the names in alphabetical order
for name in sorted(baby_names):
    # Print each name
    print(name)
    
