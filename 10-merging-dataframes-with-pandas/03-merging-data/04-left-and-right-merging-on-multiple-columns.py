'''
Left & right merging on multiple columns

You now have, in addition to the revenue and managers DataFrames from prior exercises, a DataFrame sales that summarizes units sold from specific branches (identified by city and state but not branch_id).

Once again, the managers DataFrame uses the label branch in place of city as in the other two DataFrames. Your task here is to employ left and right merges to preserve data and identify where data is missing.

By merging revenue and sales with a right merge, you can identify the missing revenue values. Here, you don't need to specify left_on or right_on because the columns to merge on have matching labels.

By merging sales and managers with a left merge, you can identify the missing manager. Here, the columns to merge on have conflicting labels, so you must specify left_on and right_on. In both cases, you're looking to figure out how to connect the fields in rows containing Springfield.

pandas has been imported as pd and the three DataFrames revenue, managers, and sales have been pre-loaded. They have been printed for you to explore in the IPython Shell.

INSTRUCTIONS

*   Execute a right merge using pd.merge() with revenue and sales to yield a new DataFrame revenue_and_sales.
*   Use how='right' and on=['city', 'state'].
*   Print the new DataFrame revenue_and_sales. This has been done for you.
*   Execute a left merge with sales and managers to yield a new DataFrame sales_and_managers.
*   Use how='left', left_on=['city', 'state'], and right_on=['branch', 'state].
*   Print the new DataFrame sales_and_managers. This has been done for you, so hit 'Submit Answer' to see the result!
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

sales    = pd.DataFrame({'city': [ 'Mendocino','Denver','Austin','Springfield','Springfield'],
                         'state': ['CA','CO','TX','MO','IL'],
                         'units': [1,4,2,5,1]})

# ---

# Merge revenue and sales: revenue_and_sales
revenue_and_sales = pd.merge(revenue, sales, how='right', on=['city','state'])

# Print revenue_and_sales
print(revenue_and_sales)

# Merge sales and managers: sales_and_managers
sales_and_managers = pd.merge(sales, managers, how='left', left_on=['city','state'], right_on=['branch','state'])

# Print sales_and_managers
print(sales_and_managers)

'''
> revenue
   branch_id         city  revenue state
0         10       Austin      100    TX
1         20       Denver       83    CO
2         30  Springfield        4    IL
3         47    Mendocino      200    CA

> sales
          city state  units
0    Mendocino    CA      1
1       Denver    CO      4
2       Austin    TX      2
3  Springfield    MO      5
4  Springfield    IL      1

> managers
        branch  branch_id   manager state
0       Austin         10  Charlers    TX
1       Denver         20      Joel    CO
2    Mendocino         47     Brett    CA
3  Springfield         31     Sally    MO

> revenue_and_sales
   branch_id         city  revenue state  units
0       10.0       Austin    100.0    TX      2
1       20.0       Denver     83.0    CO      4
2       30.0  Springfield      4.0    IL      1
3       47.0    Mendocino    200.0    CA      1
4        NaN  Springfield      NaN    MO      5

> sales_and_managers
          city state  units       branch  branch_id  manager
0    Mendocino    CA      1    Mendocino       47.0    Brett
1       Denver    CO      4       Denver       20.0     Joel
2       Austin    TX      2       Austin       10.0  Charles
3  Springfield    MO      5  Springfield       31.0    Sally
4  Springfield    IL      1          NaN        NaN      NaN
'''