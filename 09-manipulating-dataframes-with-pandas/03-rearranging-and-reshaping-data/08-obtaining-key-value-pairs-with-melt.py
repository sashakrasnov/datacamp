'''
Obtaining key-value pairs with melt()

Sometimes, all you need is some key-value pairs, and the context does not matter. If said context is in the index, you can easily obtain what you want. For example, in the users DataFrame, the visitors and signups columns lend themselves well to being represented as key-value pairs. So if you created a hierarchical index with 'city' and 'weekday' columns as the index, you can easily extract key-value pairs for the 'visitors' and 'signups' columns by melting users and specifying col_level=0.

INSTRUCTIONS

*   Set the index of users to ['city', 'weekday'].
*   Print the DataFrame users_idx to see the new index.
*   Obtain the key-value pairs corresponding to visitors and signups by melting users_idx with the keyword argument col_level=0.
'''

import pandas as pd

users = pd.read_csv('../datasets/users.csv', index_col=0)

# ---

# Set the new index: users_idx
users_idx = users.set_index(['city','weekday'])

# Print the users_idx DataFrame
print(users_idx)

# Obtain the key-value pairs: kv_pairs
kv_pairs = pd.melt(users_idx, col_level=0)

# Print the key-value pairs
print(kv_pairs)

'''
> users
  weekday    city  visitors  signups
0     Sun  Austin       139        7
1     Sun  Dallas       237       12
2     Mon  Austin       326        3
3     Mon  Dallas       456        5

> users_idx
                visitors  signups
city   weekday                   
Austin Sun           139        7
Dallas Sun           237       12
Austin Mon           326        3
Dallas Mon           456        5

> kv_pairs
   variable  value
0  visitors    139
1  visitors    237
2  visitors    326
3  visitors    456
4   signups      7
5   signups     12
6   signups      3
7   signups      5
'''