'''
Using other aggregations in pivot tables

You can also use aggregation functions with in a pivot table by specifying the aggfunc parameter. In this exercise, you will practice using the 'count' and len aggregation functions - which produce the same result - on the users DataFrame.

INSTRUCTIONS

*   Define a DataFrame count_by_weekday1 that shows the count of each column with the parameter aggfunc='count'. The index here is 'weekday'.
*   Print count_by_weekday1. This has been done for you.
*   Replace aggfunc='count' with aggfunc=len and verify you obtain the same result.
'''

import pandas as pd

users = pd.read_csv('../datasets/users.csv', index_col=0)

# ---

# Use a pivot table to display the count of each column: count_by_weekday1
count_by_weekday1 = users.pivot_table(index='weekday', aggfunc='count')

# Print count_by_weekday
print(count_by_weekday1)

# Replace 'aggfunc='count'' with 'aggfunc=len': count_by_weekday2
count_by_weekday2 = users.pivot_table(index='weekday', aggfunc=len)

# Verify that the same result is obtained
print('==========================================')
print(count_by_weekday1.equals(count_by_weekday2))

'''
> users
  weekday    city  visitors  signups
0     Sun  Austin       139        7
1     Sun  Dallas       237       12
2     Mon  Austin       326        3
3     Mon  Dallas       456        5

> count_by_weekday1
         city  signups  visitors
weekday
Mon         2        2         2
Sun         2        2         2

==========================================
True
'''