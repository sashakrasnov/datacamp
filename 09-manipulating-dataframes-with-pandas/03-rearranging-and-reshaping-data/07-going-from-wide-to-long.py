'''
Going from wide to long

You can move multiple columns into a single column (making the data long and skinny) by "melting" multiple columns. In this exercise, you will practice doing this.

The users DataFrame has been pre-loaded for you. As always, explore it in the IPython Shell and note the index.

INSTRUCTIONS

*   Define a DataFrame skinny where you melt the 'visitors' and 'signups' columns of users into a single column.
*   Print skinny to verify the results. Note the value column that had the cell values in users.
'''

import pandas as pd

users = pd.read_csv('../datasets/users.csv', index_col=0)

# ---

# Melt users: skinny
skinny = pd.melt(users, id_vars=['weekday','city'])

# Print skinny
print(skinny)

'''
> users
  weekday    city  visitors  signups
0     Sun  Austin       139        7
1     Sun  Dallas       237       12
2     Mon  Austin       326        3
3     Mon  Dallas       456        5

> skinny
  weekday    city  variable  value
0     Sun  Austin  visitors    139
1     Sun  Dallas  visitors    237
2     Mon  Austin  visitors    326
3     Mon  Dallas  visitors    456
4     Sun  Austin   signups      7
5     Sun  Dallas   signups     12
6     Mon  Austin   signups      3
7     Mon  Dallas   signups      5
'''