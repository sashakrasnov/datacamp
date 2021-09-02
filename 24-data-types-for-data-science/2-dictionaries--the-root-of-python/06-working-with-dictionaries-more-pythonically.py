'''
Popping and deleting from dictionaries

Often, you will want to remove keys and value from a dictionary. You can do so using the del Python instruction. It's important to remember that del will throw a KeyError if the key you are trying to delete does not exist. You can not use it with the .get() method to safely delete items; however, it can be used with try: catch:.

If you want to save that deleted data into another variable for further processing, the .pop() dictionary method will do just that. You can supply a default value for .pop() much like you did for .get() to safely deal with missing keys. It's also typical to use .pop() instead of del since it is a safe method.

Here, you'll remove 2011 and 2015 to save them for later, and then delete 2012 from the dictionary.
'''

baby_names = {}

with open('../datasets/baby_names.csv') as f:
    # Skipping header
    _ = f.readline()
    # Iterating over lines
    for row in f:
        year, sex, _, name, count, rank = row.strip().split(',')

        year = int(year)
        rank = int(rank)

        if sex == 'MALE' and year > 2011:
            # Empty dictionary for 2012
            if year in baby_names and year != 2012:
                baby_names[year][rank] = name
            else:
                baby_names[year] = {}

# Sorting dictionary year by year
for y in baby_names:
    baby_names[y] = dict(sorted(baby_names[y].items()))

'''
INSTRUCTIONS

*   Iterate over baby_names[2014], unpacking it into rank and name.
*   Print each rank and name.
*   Repeat the process for baby_names[2012].
'''

# Iterate over the 2014 nested dictionary
for rank, name in baby_names[2014].items():
    # Print rank and name
    print(rank, name)
    
# Iterate over the 2012 nested dictionary
for rank, name in baby_names[2012].items():
    # Print rank and name
    print(rank, name)
  