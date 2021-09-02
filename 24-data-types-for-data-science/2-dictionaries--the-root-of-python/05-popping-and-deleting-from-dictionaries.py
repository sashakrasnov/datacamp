'''
Popping and deleting from dictionaries

Often, you will want to remove keys and value from a dictionary. You can do so using the del Python instruction. It's important to remember that del will throw a KeyError if the key you are trying to delete does not exist. You can not use it with the .get() method to safely delete items; however, it can be used with try: catch:.

If you want to save that deleted data into another variable for further processing, the .pop() dictionary method will do just that. You can supply a default value for .pop() much like you did for .get() to safely deal with missing keys. It's also typical to use .pop() instead of del since it is a safe method.

Here, you'll remove 2011 and 2015 to save them for later, and then delete 2012 from the dictionary.
'''

female_names = {}

with open('../datasets/baby_names.csv') as f:
    # Skipping header
    _ = f.readline()
    # Iterating over lines
    for row in f:
        year, sex, _, name, count, rank = row.strip().split(',')

        year = int(year)
        rank = int(rank)

        if sex == 'FEMALE':
            # Empty dictionary for 2012
            if year in female_names and year != 2012:
                female_names[year][rank] = name
            else:
                female_names[year] = {}

# Sorting dictionary year by year
for y in female_names:
    female_names[y] = dict(sorted(female_names[y].items()))

'''
INSTRUCTIONS

*   Remove 2011 from female_names and store it as female_names_2011.
*   Safely remove 2015 from female_names with a empty dictionary as the default and store it as female_names_2015. To do this, pass in an empty dictionary {} as a second argument to .pop().
*   Delete 2012 from female_names.
*   Print female_names.
'''

# Remove 2011 and store it: female_names_2011
female_names_2011 = female_names.pop(2011)

# Safely remove 2015 with an empty dictionary as the default: female_names_2015
female_names_2015 = female_names.pop(2015, {})

# Delete 2012
del female_names[2012]

# Print female_names
print(female_names)
