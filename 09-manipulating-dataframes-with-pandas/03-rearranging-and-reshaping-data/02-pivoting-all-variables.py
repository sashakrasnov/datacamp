'''
Pivoting all variables

If you do not select any particular variables, all of them will be pivoted. In this case - with the users DataFrame - both 'visitors' and 'signups' will be pivoted, creating hierarchical column labels.

You will explore this for yourself now in this exercise.

INSTRUCTIONS

*   Pivot the users DataFrame with the 'signups' indexed by 'weekday' in the rows and 'city' in the columns.
*   Print the new DataFrame. This has been done for you.
*   Pivot the users DataFrame with both 'signups' and 'visitors' pivoted - that is, all the variables. This will happen automatically if you do not specify an argument for the values parameter of .pivot().
*   Print the pivoted DataFrame. This has been done for you, so hit 'Submit Answer' to see the result.
'''

import pandas as pd

users = pd.read_csv('../datasets/users.csv', index_col=0)

# ---

# Pivot users with signups indexed by weekday and city: signups_pivot
signups_pivot = users.pivot(index='weekday', columns='city', values='signups')

# Print signups_pivot
print(signups_pivot)

# Pivot users pivoted by both signups and visitors: pivot
pivot = users.pivot(index='weekday', columns='city')

# Print the pivoted DataFrame
print(pivot)

'''
> users
  weekday    city  visitors  signups
0     Sun  Austin       139        7
1     Sun  Dallas       237       12
2     Mon  Austin       326        3
3     Mon  Dallas       456        5

> signups_pivot
city     Austin  Dallas
weekday                
Mon           3       5
Sun           7      12

> pivot
        visitors        signups       
city      Austin Dallas  Austin Dallas
weekday                               
Mon          326    456       3      5
Sun          139    237       7     12
'''
