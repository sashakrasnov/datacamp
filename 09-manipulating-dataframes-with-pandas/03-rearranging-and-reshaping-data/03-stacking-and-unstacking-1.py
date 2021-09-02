'''
Stacking & unstacking I

You are now going to practice stacking and unstacking DataFrames. The users DataFrame you have been working with in this chapter has been pre-loaded for you, this time with a MultiIndex. Explore it in the IPython Shell to see the data layout. Pay attention to the index, and notice that the index levels are ['city', 'weekday']. So 'weekday' - the second entry - has position 1. This position is what corresponds to the level parameter in .stack() and .unstack() calls. Alternatively, you can specify 'weekday' as the level instead of its position.

Your job in this exercise is to unstack users by 'weekday'. You will then use .stack() on the unstacked DataFrame to see if you get back the original layout of users.

INSTRUCTIONS

*   Define a DataFrame byweekday with the 'weekday' level of users unstacked.
*   Print the byweekday DataFrame to see the new data layout. This has been done for you.
*   Stack byweekday by 'weekday' and print it to check if you get the same layout as the original users DataFrame.
'''

import pandas as pd

users = pd.read_csv('../datasets/users.csv', index_col=0).set_index(['city', 'weekday']).sort_index()

# ---

# Unstack users by 'weekday': byweekday
byweekday = users.unstack(level='weekday')

# Print the byweekday DataFrame
print(byweekday)

# Stack byweekday by 'weekday' and print it
print(byweekday.stack(level='weekday'))

'''
> users
                visitors  signups
city   weekday                   
Austin Mon           326        3
       Sun           139        7
Dallas Mon           456        5
       Sun           237       12

> byweekday
        visitors      signups    
weekday      Mon  Sun     Mon Sun
city                             
Austin       326  139       3   7
Dallas       456  237       5  12

> byweekday.stack(level='weekday')
                visitors  signups
city   weekday                   
Austin Mon           326        3
       Sun           139        7
Dallas Mon           456        5
       Sun           237       12
'''