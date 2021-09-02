'''
Safely finding by key

As demonstrated in the video, if you attempt to access a key that isn't present in a dictionary, you'll get a KeyError. One option to handle this type of error is to use a try: except: block. You can learn more about error handling in Python Data Science Toolbox (Part 1), specifically in this video.

Python provides a faster, more versatile tool to help with this problem in the form of the .get() method. The .get() method allows you to supply the name of a key, and optionally, what you'd like to have returned if the key is not found.

You'll be using same names dictionary from the previous exercise and will gain practice using the .get() method.
'''

names_2012 = {}

with open('../datasets/baby_names.csv') as f:
    # Skipping header
    _ = f.readline()
    # Iterating over lines
    for row in f:
        year, sex, _, name, count, rank = row.strip().split(',')

        if year == '2012' and sex == 'FEMALE':
            names_2012[int(rank)] = name

names = dict(sorted(names_2012.items()))

'''
INSTRUCTIONS

*   Safely print rank 7 from the names dictionary.
*   Safely print the type of rank 100 from the names dictionary.
*   Safely print rank 105 from the names dictionary or 'Not Found' if 105 is not found.
'''

# Safely print rank 7 from the names dictionary
print(names.get(7))

# Safely print the type of rank 100 from the names dictionary
print(type(names.get(100)))

# Safely print rank 105 from the names dictionary or 'Not Found'
print(names.get(105, 'Not Found'))
