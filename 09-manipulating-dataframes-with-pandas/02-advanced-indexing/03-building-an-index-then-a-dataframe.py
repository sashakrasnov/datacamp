'''
Building an index, then a DataFrame

You can also build the DataFrame and index independently, and then put them together. If you take this route, be careful, as any mistakes in generating the DataFrame or the index can cause the data and the index to be aligned incorrectly.

In this exercise, the sales DataFrame has been provided for you without the month index. Your job is to build this index separately and then assign it to the sales DataFrame. Before getting started, print the sales DataFrame in the IPython Shell and note that it's missing the month information.

INSTRUCTIONS

*   Generate a list months with the data ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']. This has been done for you.
*   Assign months to sales.index.
*   Print the modified sales dataframe and verify that you now have month information in the index.
'''

import pandas as pd

sales = pd.read_csv('../datasets/sales.csv').drop('month', axis=1)

# ---

# Generate the list of months: months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# Assign months to sales.index
sales.index = months

# Print the modified sales DataFrame
print(sales)

'''
> sales
   eggs  salt  spam
0    47  12.0    17
1   110  50.0    31
2   221  89.0    72
3    77  87.0    20
4   132   NaN    52
5   205  60.0    55

> sales
     eggs  salt  spam
Jan    47  12.0    17
Feb   110  50.0    31
Mar   221  89.0    72
Apr    77  87.0    20
May   132   NaN    52
Jun   205  60.0    55
'''
