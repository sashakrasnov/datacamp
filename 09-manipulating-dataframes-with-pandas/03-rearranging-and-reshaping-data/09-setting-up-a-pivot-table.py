'''
Setting up a pivot table

Recall from the video that a pivot table allows you to see all of your variables as a function of two other variables. In this exercise, you will use the .pivot_table() method to see how the users DataFrame entries appear when presented as functions of the 'weekday' and 'city' columns. That is, with the rows indexed by 'weekday' and the columns indexed by 'city'.

Before using the pivot table, print the users DataFrame in the IPython Shell and observe the layout.

INSTRUCTIONS

*   Use a pivot table to index the rows of users by 'weekday' and the columns of users by 'city'. These correspond to the index and columns parameters of .pivot_table().
*   Print by_city_day. This has been done for you, so hit 'Submit Answer' to see the result.
'''

import pandas as pd

users = pd.read_csv('../datasets/users.csv', index_col=0)

# ---

# Create the DataFrame with the appropriate pivot table: by_city_day
by_city_day = users.pivot_table(index='weekday',columns='city')

# Print by_city_day
print(by_city_day)

'''
> users
  weekday    city  visitors  signups
0     Sun  Austin       139        7
1     Sun  Dallas       237       12
2     Mon  Austin       326        3
3     Mon  Dallas       456        5

> by_city_day
        signups        visitors
city     Austin Dallas   Austin Dallas
weekday
Mon           3      5      326    456
Sun           7     12      139    237
'''