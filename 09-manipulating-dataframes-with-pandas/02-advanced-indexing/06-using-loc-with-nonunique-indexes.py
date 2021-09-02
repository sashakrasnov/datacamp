'''
Using .loc[] with nonunique indexes

As Dhavide mentioned in the video, it is always preferable to have a meaningful index that uniquely identifies each row. Even though pandas does not require unique index values in DataFrames, it works better if the index values are indeed unique. To see an example of this, you will index your sales data by 'state' in this exercise.

As always, begin by printing the sales DataFrame in the IPython Shell and inspecting it.

INSTRUCTIONS

*   Set the index of sales to be the column 'state'.
*   Print the sales DataFrame to verify that indeed you have an index with state values.
*   Access the data from 'NY' and print it to verify that you obtain two rows.
'''

import pandas as pd

sales = pd.read_csv('../datasets/sales.csv')

sales['state'] = ['CA', 'CA', 'NY', 'NY', 'TX', 'TX']
sales['month'] = [1, 2] * 3
print(sales)
# ---

# Set the index to the column 'state': sales

sales = sales.set_index(['state'])

# Print the sales DataFrame
print(sales)

# Access the data from 'NY'
print(sales.loc['NY'])

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
       month  eggs  salt  spam
state                         
CA         1    47  12.0    17
CA         2   110  50.0    31
NY         1   221  89.0    72
NY         2    77  87.0    20
TX         1   132   NaN    52
TX         2   205  60.0    55
       month  eggs  salt  spam

> sales.loc['NY']
state                         
NY         1   221  89.0    72
NY         2    77  87.0    20
'''