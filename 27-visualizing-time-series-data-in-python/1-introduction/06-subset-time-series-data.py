'''
Subset time series data

When plotting time series data, you may occasionally want to visualize only a subset of the data. The pandas library provides powerful indexing and subsetting methods that allow you to extract specific portions of a DataFrame. For example, you can subset all the data between 1950 and 1960 in the discoveries DataFrame by specifying the following date range:

|   subset_data = discoveries['1950-01-01':'1960-01-01']

Note: Subsetting your data this way is only possible if the index of your DataFrame contains dates of the datetime type. Failing that, the pandas library will return an error message.
'''

import pandas as pd
import matplotlib.pyplot as plt

url_discoveries = '../datasets/ch1_discoveries.csv'

discoveries = pd.read_csv(url_discoveries)

discoveries['date'] = pd.to_datetime(discoveries.date)
discoveries = discoveries.set_index('date')

'''
INSTRUCTIONS 1/2

*   Use discoveries to create a new DataFrame discoveries_subset_1 that contains all the data between January 1, 1945 and January 1, 1950.
*   Plot the time series of discoveries_subset_1 using a "blue" line plot.
'''

# Select the subset of data between 1945 and 1950
discoveries_subset_1 = discoveries['1945':'1950']

# Plot the time series in your DataFrame as a blue area chart
ax = discoveries_subset_1.plot(color='blue', fontsize=15)

# Show plot
plt.show()

'''
INSTRUCTIONS 2/2

*   Use discoveries to create a new DataFrame discoveries_subset_2 that contains all the data between January 1, 1939 and January 1, 1958.
*   Plot the time series of discoveries_subset_2 using a "blue" line plot.
'''

# Select the subset of data between 1939 and 1958
discoveries_subset_2 = discoveries['1939':'1958']

# Plot the time series in your DataFrame as a blue area chart
ax = discoveries_subset_2.plot(color='blue', fontsize=15)

# Show plot
plt.show()