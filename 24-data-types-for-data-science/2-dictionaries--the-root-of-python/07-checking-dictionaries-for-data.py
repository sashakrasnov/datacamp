'''
Checking dictionaries for data

You can check to see if a key exists in a dictionary by using the in expression.

For example, you can check to see if 'cookies' is a key in the dictionary by using if 'cookies' in recipes_dict: this allows you to safely react to data being present in the dictionary.

You can also use the in expression so see if data is in the value of a dictionary such as if 'cookies' in recipes_dict.values(). Remember you have to handle nested dictionaries differently as illustrated in the video and previous exercises, and use the in expression on each nested dictionary.
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

*   Check to see if 2011 is in the baby_names dictionary.
    *   Print 'Found 2011' if it is present.
*   Check to see if 1 is in baby_names[2012].
    *   Print 'Found Rank 1 in 2012' if found and 'Rank 1 missing from 2012' if not found.
*   Check to see if rank 5 is in baby_names[2013].
    *   Print 'Found Rank 5' if it is present.
'''

# Check to see if 2011 is in baby_names
if 2011 in baby_names:
    # Print 'Found 2011'
    print('Found 2011')
    
# Check to see if rank 1 is in 2012
if 1 in baby_names[2012]:
    # Print 'Found Rank 1 in 2012' if found
    print('Found Rank 1 in 2012')
else:
    # Print 'Rank 1 missing from 2012' if not found
    print('Rank 1 missing from 2012')
    
# Check to see if Rank 5 is in 2013
if 5 in baby_names[2013]:
   # Print 'Found Rank 5'
   print('Found Rank 5')