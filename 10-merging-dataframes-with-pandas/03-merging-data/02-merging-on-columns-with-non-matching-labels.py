'''
Merging on columns with non-matching labels

You continue working with the revenue & managers DataFrames from before. This time, someone has changed the field name 'city' to 'branch' in the managers table. Now, when you attempt to merge DataFrames, an exception is thrown:

|   >>> pd.merge(revenue, managers, on='city')
|   Traceback (most recent call last):
|       ... <text deleted> ...
|       pd.merge(revenue, managers, on='city')
|       ... <text deleted> ...
|   KeyError: 'city'

Given this, it will take a bit more work for you to join or merge on the city/branch name. You have to specify the left_on and right_on parameters in the call to pd.merge().

As before, pandas has been pre-imported as pd and the revenue and managers DataFrames are in your namespace. They have been printed in the IPython Shell so you can examine the columns prior to merging.

Are you able to merge better than in the last exercise? How should the rows with Springfield be handled?

INSTRUCTIONS

*   Merge the DataFrames revenue and managers into a single DataFrame called combined using the 'city' and 'branch' columns from the appropriate DataFrames.
*   In your call to pd.merge(), you will have to specify the parameters left_on and right_on appropriately.
*   Print the new DataFrame combined.
'''

import pandas as pd

revenue  = pd.DataFrame({'branch_id': [10,20,30,47],
                         'city': ['Austin','Denver','Springfield','Mendocino'],
                         'revenue': [100,83,4,200],
                         'state': ['TX','CO','IL','CA']})

managers = pd.DataFrame({'branch': ['Austin','Denver','Mendocino','Springfield'],
                         'branch_id': [10,20,47,31],
                         'manager': ['Charles','Joel','Brett','Sally'],
                         'state': ['TX','CO','CA','MO']})

# ---

# Merge revenue & managers on 'city' & 'branch': combined
combined = pd.merge(revenue, managers, left_on='city', right_on='branch')

# Print combined
print(combined)

'''
> revenue
   branch_id         city  revenue state
0         10       Austin      100    TX
1         20       Denver       83    CO
2         30  Springfield        4    IL
3         47    Mendocino      200    CA

> managers
        branch  branch_id  manager state
0       Austin         10  Charles    TX
1       Denver         20     Joel    CO
2    Mendocino         47    Brett    CA
3  Springfield         31    Sally    MO

> combined
   branch_id_x         city  revenue state_x       branch  branch_id_y  manager state_y
0           10       Austin      100      TX       Austin           10  Charles      TX
1           20       Denver       83      CO       Denver           20     Joel      CO
2           30  Springfield        4      IL  Springfield           31    Sally      MO
3           47    Mendocino      200      CA    Mendocino           47    Brett      CA
'''