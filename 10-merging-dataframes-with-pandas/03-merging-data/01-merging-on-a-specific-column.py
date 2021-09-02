'''
Merging on a specific column

This exercise follows on the last one with the DataFrames revenue and managers for your company. You expect your company to grow and, eventually, to operate in cities with the same name on different states. As such, you decide that every branch should have a numerical branch identifier. Thus, you add a branch_id column to both DataFrames. Moreover, new cities have been added to both the revenue and managers DataFrames as well. pandas has been imported as pd and both DataFrames are available in your namespace.

At present, there should be a 1-to-1 relationship between the city and branch_id fields. In that case, the result of a merge on the city columns ought to give you the same output as a merge on the branch_id columns. Do they? Can you spot an ambiguity in one of the DataFrames?

INSTRUCTIONS

*   Using pd.merge(), merge the DataFrames revenue and managers on the 'city' column of each. Store the result as merge_by_city.
*   Print the DataFrame merge_by_city. This has been done for you.
*   Merge the DataFrames revenue and managers on the 'branch_id' column of each. Store the result as merge_by_id.
*   Print the DataFrame merge_by_id. This has been done for you, so hit 'Submit Answer' to see the result!
'''

import pandas as pd

revenue  = pd.DataFrame({'branch_id': [10,20,30,47],
                         'city': ['Austin','Denver','Springfield','Mendocino'],
                         'revenue': [100,83,4,200]})

managers = pd.DataFrame({'branch_id': [10,20,47,31],
                         'city': ['Austin','Denver','Mendocino','Springfield'],
                         'manager': ['Charles','Joel','Brett','Sally']})

# ---

# Merge revenue with managers on 'city': merge_by_city
merge_by_city = pd.merge(revenue, managers, on='city')

# Print merge_by_city
print(merge_by_city)

# Merge revenue with managers on 'branch_id': merge_by_id
merge_by_id = pd.merge(revenue, managers, on='branch_id')

# Print merge_by_id
print(merge_by_id)

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

> merge_by_city
   branch_id_x         city  revenue  branch_id_y  manager
0           10       Austin      100           10  Charles
1           20       Denver       83           20     Joel
2           30  Springfield        4           31    Sally
3           47    Mendocino      200           47    Brett

> merge_by_id
   branch_id     city_x  revenue     city_y  manager
0         10     Austin      100     Austin  Charles
1         20     Denver       83     Denver     Joel
2         47  Mendocino      200  Mendocino    Brett
'''