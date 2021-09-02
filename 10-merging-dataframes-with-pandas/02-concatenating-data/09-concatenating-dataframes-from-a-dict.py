'''
You're now going to revisit the sales data you worked with earlier in the chapter. Three DataFrames jan, feb, and mar have been pre-loaded for you. Your task is to aggregate the sum of all sales over the 'Company' column into a single DataFrame. You'll do this by constructing a dictionary of these DataFrames and then concatenating them.

INSTRUCTIONS

*   Create a list called month_list consisting of the tuples ('january', jan), ('february', feb), and ('march', mar).
*   Create an empty dictionary called month_dict.
*   Inside the for loop:
    *   Group month_data by 'Company' and use .sum() to aggregate.
*   Construct a new DataFrame called sales by concatenating the DataFrames stored in month_dict.
*   Create an alias for pd.IndexSlice and print all sales by 'Mediacore'. This has been done for you, so hit 'Submit Answer' to see the result!
'''

import pandas as pd

jan = pd.read_csv('../datasets/sales/sales-jan-2015.csv')
feb = pd.read_csv('../datasets/sales/sales-feb-2015.csv')
mar = pd.read_csv('../datasets/sales/sales-mar-2015.csv')

# ---

# Make the list of tuples: month_list
month_list = [('january', jan), ('february', feb), ('march', mar)]

# Create an empty dictionary: month_dict
month_dict = {}

for month_name, month_data in month_list:

    # Group month_data: month_dict[month_name]
    month_dict[month_name] = month_data.groupby('Company').sum()

# Concatenate data in month_dict: sales
sales = pd.concat(month_dict)

# Print sales
print(sales)

# Print all sales by Mediacore
idx = pd.IndexSlice
print(sales.loc[idx[:, 'Mediacore'], :])

'''
> sales
                          Units
         Company               
february Acme Coporation     34
         Hooli               30
         Initech             30
         Mediacore           45
         Streeplex           37
january  Acme Coporation     76
         Hooli               70
         Initech             37
         Mediacore           15
         Streeplex           50
march    Acme Coporation      5
         Hooli               37
         Initech             68
         Mediacore           68
         Streeplex           40

> sales.loc[idx[:, 'Mediacore'], :]
                    Units
         Company
february Mediacore     45
january  Mediacore     15
march    Mediacore     68
'''