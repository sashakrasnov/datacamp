'''
Finding all the data and the overlapping data between sets

Sets have several methods to combine, compare, and study them all based on mathematical set theory. The .union() method returns a set of all the names found in the set you used the method on plus any sets passed as arguments to the method. You can also look for overlapping data in sets by using the .intersection() method on a set and passing another set as an argument. It will return an empty set if nothing matches.

Your job in this exercise is to find the union and intersection in the names from 2011 and 2014. For this purpose, two sets have been pre-loaded into your workspace: baby_names_2011 and baby_names_2014.

One quirk in the baby names dataset is that names in 2011 and 2012 are all in upper case, while names in 2013 and 2014 are in title case (where the first letter of each name is capitalized). Consequently, if you were to compare the 2011 and 2014 data in this form, you would find no overlapping names between the two years! To remedy this, we converted the names in 2011 to title case using Python's .title() method.

Real-world data can often come with quirks like this - it's important to catch them to ensure your results are meaningful.
'''

baby_names_2011 = set()
baby_names_2014 = set()

with open('../datasets/baby_names.csv') as f:
    # Skipping header
    _ = f.readline()
    # Iterating over lines
    for row in f:
        year, sex, _, name, _, _ = row.strip().split(',')

        if year == '2011':
            baby_names_2011.add(name.title())
        if year == '2014':
            baby_names_2014.add(name)

'''
INSTRUCTIONS

*   Combine all the names in baby_names_2011 and baby_names_2014 by computing their union. Store the result as all_names.
*   Print the number of names that occur in all_names. You can use the len() function to compute the number of names in all_names.
*   Find all the names that occur in both baby_names_2011 and baby_names_2014 by computing their intersection. Store the result as overlapping_names.
*   Print the number of names that occur in overlapping_names.
'''

# Find the union: all_names
all_names = baby_names_2011.union(baby_names_2014)

# Print the count of names in all_names
print(len(all_names))

# Find the intersection: overlapping_names
overlapping_names = baby_names_2011.intersection(baby_names_2014)

# Print the count of names in overlapping_names
print(len(overlapping_names))
