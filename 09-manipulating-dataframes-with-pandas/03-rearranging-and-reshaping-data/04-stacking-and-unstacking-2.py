'''
Stacking & unstacking II

You are now going to continue working with the users DataFrame. As always, first explore it in the IPython Shell to see the layout and note the index.

Your job in this exercise is to unstack and then stack the 'city' level, as you did previously for 'weekday'. Note that you won't get the same DataFrame.

INSTRUCTIONS

*   Define a DataFrame bycity with the 'city' level of users unstacked.
*   Print the bycity DataFrame to see the new data layout. This has been done for you.
*   Stack bycity by 'city' and print it to check if you get the same layout as the original users DataFrame.
'''

import pandas as pd

users = pd.read_csv('../datasets/users.csv', index_col=0).set_index(['city', 'weekday']).sort_index()

# ---

# Unstack users by 'city': bycity
bycity = users.unstack(level='city')

# Print the bycity DataFrame
print(bycity)

# Stack bycity by 'city' and print it
print(bycity.stack(level='city'))

'''
> users
                visitors  signups
city   weekday                   
Austin Mon           326        3
       Sun           139        7
Dallas Mon           456        5
       Sun           237       12

> bycity
        visitors        signups       
city      Austin Dallas  Austin Dallas
weekday                               
Mon          326    456       3      5
Sun          139    237       7     12

> bycity
                visitors  signups
weekday city                     
Mon     Austin       326        3
        Dallas       456        5
Sun     Austin       139        7
        Dallas       237       12
'''