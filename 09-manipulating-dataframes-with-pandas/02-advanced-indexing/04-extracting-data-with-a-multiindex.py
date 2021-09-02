'''
Extracting data with a MultiIndex

In the video, Dhavide explained the concept of a hierarchical index, or a MultiIndex. You will now practice working with these types of indexes.

The sales DataFrame you have been working with has been extended to now include State information as well. In the IPython Shell, print the new sales DataFrame to inspect the data. Take note of the MultiIndex!

Extracting elements from the outermost level of a MultiIndex is just like in the case of a single-level Index. You can use the .loc[] accessor as Dhavide demonstrated in the video.

INSTRUCTIONS

*   Print sales.loc[['CA', 'TX']]. Note how New York is excluded.
*   Print sales['CA':'TX']. Note how New York is included.
'''

import pandas as pd

sales = pd.read_csv('../datasets/sales.csv').drop('month', axis=1)

sales.index = pd.MultiIndex.from_product([['CA', 'NY', 'TX'], [1, 2]], names=['state', 'month'])

# ---

# Print sales.loc[['CA', 'TX']]
print(sales.loc[['CA', 'TX']])

# Print sales['CA':'TX']
print(sales['CA':'TX'])

'''
> sales
             eggs  salt  spam
state month                  
CA    1        47  12.0    17
      2       110  50.0    31
NY    1       221  89.0    72
      2        77  87.0    20
TX    1       132   NaN    52
      2       205  60.0    55

> sales
             eggs  salt  spam
state month                  
CA    1        47  12.0    17
      2       110  50.0    31
TX    1       132   NaN    52
      2       205  60.0    55

>sales
state month                  
CA    1        47  12.0    17
      2       110  50.0    31
NY    1       221  89.0    72
      2        77  87.0    20
TX    1       132   NaN    52
      2       205  60.0    55
'''