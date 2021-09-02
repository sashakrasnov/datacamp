'''
Find missing values

In the field of Data Science, it is common to encounter datasets with missing values. This is especially true in the case of time series data, where missing values can occur if a measurement fails to record the value at a specific timestamp. To count the number of missing values in a DataFrame called df that contains time series data, you can use the command:

|   missing_values = df.isnull().sum()

In this exercise, you will learn how to find whether your data contains any missing values.
'''

import pandas as pd

co2_levels = pd.read_csv('../datasets/ch2_co2_levels.csv')

'''
INSTRUCTIONS 1/2

*   The co2_levels time series DataFrame contains time series data on global CO2 levels. Start by printing the first seven rows of co2_levels.
'''

# Display first seven rows of co2_levels
print(co2_levels.head(7))

'''
INSTRUCTIONS 2/2

*   Set the 'datestamp' column as the index of the co2_levels DataFrame.
*   Print the total number of missing values in co2_levels.
'''

# Set datestamp column as index
co2_levels = co2_levels.set_index('datestamp')

# Print out the number of missing values
print(co2_levels.isnull().sum())