'''
Setting & sorting a MultiIndex

In the previous exercise, the MultiIndex was created and sorted for you. Now, you're going to do this yourself! With a MultiIndex, you should always ensure the index is sorted. You can skip this only if you know the data is already sorted on the index fields.

To get started, print the pre-loaded sales DataFrame in the IPython Shell to verify that there is no MultiIndex.

INSTRUCTIONS

*   Create a MultiIndex by setting the index to be the columns ['month', 'state'].
*   Sort the MultiIndex using the .sort_index() method.
*   Print the sales DataFrame. This has been done for you, so hit 'Submit Answer' to verify that indeed you have an index with the fields month and state!
'''

import pandas as pd

sales = pd.read_csv('../datasets/sales.csv')

sales['state'] = ['CA', 'CA', 'NY', 'NY', 'TX', 'TX']
sales['month'] = [1, 2] * 3

# ---

# Set the index to be the columns ['month', 'state']: sales
sales = sales.set_index(['month', 'state'])
print(sales)

# Sort the MultiIndex: sales
sales = sales.sort_index()

# Print the sales DataFrame
print(sales)

'''
> sales
   month  eggs  salt  spam state
0      1    47  12.0    17    CA
1      2   110  50.0    31    CA
2      1   221  89.0    72    NY
3      2    77  87.0    20    NY
4      1   132   NaN    52    TX
5      2   205  60.0    55    TX

> sales
             eggs  salt  spam
month state
1     CA       47  12.0    17
2     CA      110  50.0    31
1     NY      221  89.0    72
2     NY       77  87.0    20
1     TX      132   NaN    52
2     TX      205  60.0    55

> sales
             eggs  salt  spam
month state
1     CA       47  12.0    17
      NY      221  89.0    72
      TX      132   NaN    52
2     CA      110  50.0    31
      NY       77  87.0    20
      TX      205  60.0    55
'''