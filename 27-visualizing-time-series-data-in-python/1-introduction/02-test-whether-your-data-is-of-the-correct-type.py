'''
Test whether your data is of the correct type

When working with time series data in pandas, any date information should be formatted as a datetime64 type. Therefore, it is important to check that the columns containing the date information are of the correct type. You can check the type of each column in a DataFrame by using the .dtypes attribute. Fortunately, if your date columns come as strings, epochs, etc... you can use the to_datetime() function to convert them to the appropriate datetime64 type:

|   df['date_column'] = pd.to_datetime(df['date_column'])

In this exercise, you will learn how to check the data type of the columns in your time series data and convert a date column to the appropriate datetime type.
'''

import pandas as pd

url_discoveries = '../datasets/ch1_discoveries.csv'

discoveries = pd.read_csv(url_discoveries)

'''
INSTRUCTIONS 1/3

*   Print out the data type of the column in the discoveries object.
'''

# Print the data type of each column in discoveries
print(discoveries.dtypes)

'''
INSTRUCTIONS 2/3

*   Convert the date column in the discoveries DataFrame to the datetime type.

'''

# Convert the date column to a datestamp type
discoveries['date'] = pd.to_datetime(discoveries.date)

'''
INSTRUCTIONS 3/3

*   Print out the data type of the column in the discoveries object again to check that your conversion worked.

'''

# Print the data type of each column in discoveries, again
print(discoveries.dtypes)