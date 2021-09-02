'''
Creating and looping through dictionaries

You'll often encounter the need to loop over some array type data, like in Chapter 1, and provide it some structure so you can find the data you desire quickly.

You start that by creating an empty dictionary and assigning part of your array data as the key and the rest as the value.

Previously, you used sorted() to organize your data in a list. Dictionaries can also be sorted. By default, using sorted() on a dictionary will sort by the keys of the dictionary. You can also reverse the order by passing reverse=True as a keyword argument.

Finally, since sorted returns a list, you can use slice notation to select only part of the list. For example, [:10] will slice the first ten items off a list and return only those items.
'''

female_baby_names_2012 = set()

with open('../datasets/baby_names.csv') as f:
    # Skipping header
    _ = f.readline()
    # Iterating over lines
    for row in f:
        year, sex, _, name, count, _ = row.strip().split(',')

        if year == '2012' and sex == 'FEMALE':
            female_baby_names_2012.add((name, count))

'''
INSTRUCTIONS

*   Create an empty dictionary called names.
*   Loop over female_baby_names_2012, unpacking it into the variables name and rank.
*   Inside the loop, add each name to the names dictionary using the rank as the key.
*   Sort the names dictionary in descending order, select the first ten items. Print each item.
'''

# Create an empty dictionary: names
names = {}

# Loop over the girl names
for name, rank in female_baby_names_2012:
    # Add each name to the names dictionary using rank as the key
    names[rank] = name
    
# Sort the names list by rank in descending order and slice the first 10 items
for rank in sorted(names, reverse=True)[:10]:
    # Print each item
    print(names[rank])