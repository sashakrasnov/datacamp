'''
Adding and extending dictionaries

If you have a dictionary and you want to add data to it, you can simply create a new key and assign the data you desire to it. It's important to remember that if it's a nested dictionary, then all the keys in the data path must exist, and each key in the path must be assigned individually.

You can also use the .update() method to update a dictionary with keys and values from another dictionary, tuples or keyword arguments.

Here, you'll combine several techniques used in prior exercises to setup your dictionary in a way that makes it easy to find the least popular baby name for each year.

Your job is to add data for the year 2011 to your dictionary by assignment, 2012 by update, and then find the least popular baby name for each year.
'''

boy_names = {}

with open('../datasets/baby_names.csv') as f:
    # Skipping header
    _ = f.readline()
    # Iterating over lines
    for row in f:
        year, sex, _, name, count, rank = row.strip().split(',')

        year = int(year)
        rank = int(rank)

        if sex == 'MALE':
            # Empty dictionary for 2012
            if year in boy_names and year != 2012:
                boy_names[year][rank] = name
            else:
                boy_names[year] = {}

# Sorting dictionary year by year
for y in boy_names:
    boy_names[y] = dict(sorted(boy_names[y].items()))

# Separating 2011 year from main dictionary
names_2011 = boy_names.pop(2011)

'''
INSTRUCTIONS

*   Assign the names_2011 dictionary as the value to the 2011 key of the boy_names dictionary.
*   Update the 2012 key in the boy_names dictionary with the following data in a list of tuples: (1, 'Casey'), (2, 'Aiden').
*   Loop over the boy_names dictionary.
    *   Inside the first for loop, use another for loop to loop over and sort the data for each year of boy_names by descending rank.
    *   Make sure you have a rank and print 'No Data Available' if not. This has been done for you.
    *   Safely print the year and least popular name or 'Not Available' if it is not found. Take advantage of the .get() method.
'''

# Assign the names_2011 dictionary as the value to the 2011 key of boy_names
boy_names[2011] = names_2011

# Update the 2012 key in the boy_names dictionary
boy_names[2012].update([(1, 'Casey'), (2, 'Aiden')])

# Loop over the boy_names dictionary 
for year in boy_names:
    # Loop over and sort the data for each year by descending rank
    for rank in sorted(boy_names[year], reverse=True)[:1]:
        # Check that you have a rank
        if not rank:
            print(year, 'No Data Available')
        # Safely print the year and the least popular name or 'Not Available'
        print(year, boy_names[year].get(rank, 'Not Available'))