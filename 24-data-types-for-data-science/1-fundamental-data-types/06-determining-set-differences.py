'''
Determining set differences

Another way of comparing sets is to use the difference() method. It returns all the items found in one set but not another. It's important to remember the set you call the method on will be the one from which the items are returned. Unlike tuples, you can add() items to a set. A set will only add items that do not exist in the set.

In this exercise, you'll explore what names were common in 2011, but are no longer common in 2014. The set baby_names_2014 has been pre-loaded into your workspace. As in the previous exercise, the names have been converted to title case to ensure a proper comparison.
'''

baby_names_2014 = set()

with open('../datasets/baby_names.csv') as f:
    records = [r.strip().split(',') for r in f]
    for row in records:
       if row[0] == '2014':
            baby_names_2014.add(row[3])

'''
INSTRUCTIONS

*   Create an empty set called baby_names_2011. You can do this using set().
*   Use a for loop to iterate over each row in records:
    *   If the first column of each row in records is '2011', add its fourth column to baby_names_2011. Remember that Python is 0-indexed!
*   Find the difference between baby_names_2011 and baby_names_2014. Store the result as differences.
*   Print the differences. This has been done for you, so hit 'Submit Answer' to see the result!
'''

# Create the empty set: baby_names_2011
baby_names_2011 = set()

# Loop over records and add the names from 2011 to the baby_names_2011 set
for row in records:
    # Check if the first column is '2011'
    if row[0] == '2011':
        # Add the fourth column to the set
        baby_names_2011.add(row[3].title())

# Find the difference between 2011 and 2014: differences
differences = baby_names_2011.difference(baby_names_2014)

# Print the differences
print(differences)
