'''
Manipulating lists for fun and profit

You may be familiar with adding individual data elements to a list by using the .append() method. However, if you want to combine a list with another array type (list, set, tuple), you can use the .extend() method on the list.

You can also use the .index() method to find the position of an item in a list. You can then use that position to remove the item with the .pop() method.

In this exercise, you'll practice using all these methods!

INSTRUCTIONS

*   Create a list called baby_names with the names 'Ximena', 'Aliza', 'Ayden', and 'Calvin'.
*   Use the .extend() method on baby_names to add 'Rowen' and 'Sandeep' and print the list.
*   Use the .index() method to find the position of 'Aliza' in the list. Save the result as position.
*   Use the .pop() method with position to remove 'Aliza' from the list.
*   Print the baby_names list. This has been done for you, so hit 'Submit Answer' to see the results!
'''

# Create a list containing the names: baby_names
baby_names = ['Ximena', 'Aliza', 'Ayden', 'Calvin']

# Extend baby_names with 'Rowen' and 'Sandeep'
baby_names.extend(['Rowen', 'Sandeep'])

# Print baby_names
print(baby_names)

# Find the position of 'Aliza': position
position = baby_names.index('Aliza')

# Remove 'Aliza' from baby_names
baby_names.pop(position)

# Print baby_names
print(baby_names)
