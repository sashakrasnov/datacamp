'''
Merging on multiple columns

Another strategy to disambiguate cities with identical names is to add information on the states in which the cities are located. To this end, you add a column called state to both DataFrames from the preceding exercises. Again, pandas has been pre-imported as pd and the revenue and managers DataFrames are in your namespace.

Your goal in this exercise is to use pd.merge() to merge DataFrames using multiple columns (using 'branch_id', 'city', and 'state' in this case).

Are you able to match all your company's branches correctly?

INSTRUCTIONS

*   Create a column called 'state' in the DataFrame revenue, consisting of the list ['TX','CO','IL','CA'].
*   Create a column called 'state' in the DataFrame managers, consisting of the list ['TX','CO','CA','MO'].
*   Merge the DataFrames revenue and managers using three columns :'branch_id', 'city', and 'state'. Pass them in as a list to the on paramater of pd.merge()
'''

import pandas as pd

revenue  = pd.DataFrame({'branch_id': [10,20,30,47],
                         'city': ['Austin','Denver','Springfield','Mendocino'],
                         'revenue': [100,83,4,200]})

managers = pd.DataFrame({'branch_id': [10,20,47,31],
                         'city': ['Austin','Denver','Mendocino','Springfield'],
                         'manager': ['Charles','Joel','Brett','Sally']})

# ---

# Add 'state' column to revenue: revenue['state']
revenue['state'] = ['TX','CO','IL','CA']

# Add 'state' column to managers: managers['state']
managers['state'] = ['TX','CO','CA','MO']

# Merge revenue & managers on 'branch_id', 'city', & 'state': combined
combined = pd.merge(revenue, managers, on=['branch_id', 'city', 'state'])

# Print combined
print(combined)

'''
> revenue
   branch_id         city  revenue
0         10       Austin      100
1         20       Denver       83
2         30  Springfield        4
3         47    Mendocino      200

> managers
   branch_id         city  manager
0         10       Austin  Charles
1         20       Denver     Joel
2         47    Mendocino    Brett
3         31  Springfield    Sally

> combined
   branch_id       city  revenue state  manager
0         10     Austin      100    TX  Charles
1         20     Denver       83    CO     Joel
2         47  Mendocino      200    CA    Brett
'''