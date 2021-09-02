'''
Using margins in pivot tables

Sometimes it's useful to add totals in the margins of a pivot table. You can do this with the argument margins=True. In this exercise, you will practice using margins in a pivot table along with a new aggregation function: sum.

The users DataFrame, which you are now probably very familiar with, has been pre-loaded for you.

INSTRUCTIONS

*   Define a DataFrame signups_and_visitors that shows the breakdown of signups and visitors by day, as well as the totals.
*   You will need to use aggfunc=sum to do this.
*   Print signups_and_visitors. This has been done for you.
*   Now pass the additional argument margins=True to the .pivot_table() method to obtain the totals.
*   Print signups_and_visitors_total. This has been done for you, so hit 'Submit Answer' to see the result.
'''

import pandas as pd

users = pd.read_csv('../datasets/users.csv', index_col=0)

# ---

# Create the DataFrame with the appropriate pivot table: signups_and_visitors
signups_and_visitors = users.pivot_table(index='weekday', aggfunc=sum)

# Print signups_and_visitors
print(signups_and_visitors)

# Add in the margins: signups_and_visitors_total 
signups_and_visitors_total = users.pivot_table(index='weekday', margins=True, aggfunc=sum)

# Print signups_and_visitors_total
print(signups_and_visitors_total)

'''
> users
  weekday    city  visitors  signups
0     Sun  Austin       139        7
1     Sun  Dallas       237       12
2     Mon  Austin       326        3
3     Mon  Dallas       456        5

> signups_and_visitors
         signups  visitors
weekday                   
Mon            8       782
Sun           19       376

> signups_and_visitors_total
         signups  visitors
weekday                   
Mon            8       782
Sun           19       376
All           27      1158
'''