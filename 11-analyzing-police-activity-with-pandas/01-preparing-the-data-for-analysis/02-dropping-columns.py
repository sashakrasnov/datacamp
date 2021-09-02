'''
Dropping columns

Often, a DataFrame will contain columns that are not useful to your analysis. Such columns should be dropped from the DataFrame, to make it easier for you to focus on the remaining columns.

In this exercise, you'll drop the county_name column because it only contains missing values, and you'll drop the state column because all of the traffic stops took place in one state (Rhode Island). Thus, these columns can be dropped because they contain no useful information.
'''

import pandas as pd

ri = pd.read_csv('../datasets/RI_cleaned.csv', nrows=100000, low_memory=False)

'''
INSTRUCTIONS

*   Count the number of missing values in each column. (This has been done for you.)
*   Examine the DataFrame's .shape to find out the number of rows and columns.
*   Drop both the county_name and state columns by passing the column names to the .drop() method as a list of strings.
*   Examine the .shape again to verify that there are now two fewer columns.
'''

# Count the number of missing values in each column
print(ri.isnull().sum())

# Examine the shape of the DataFrame
print(ri.shape)

# Drop the 'county_name' and 'state' columns
ri.drop(['county_name', 'state'], axis='columns', inplace=True)

# Examine the shape of the DataFrame (again)
print(ri.shape)