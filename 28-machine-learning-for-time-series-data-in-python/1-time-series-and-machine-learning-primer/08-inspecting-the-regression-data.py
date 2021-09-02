'''
Inspecting the regression data

The next dataset contains information about company market value over several years of time. This is one of the most popular kind of time series data used for regression. If you can model the value of a company as it changes over time, you can make predictions about where that company will be in the future. This dataset was also originally provided as part of a public Kaggle competition (https://www.kaggle.com/dgawlik/nyse).

In this exercise, you'll plot the time series for a number of companies to get an understanding of how they are (or aren't) related to one another.
'''

import matplotlib.pyplot as plt
import pandas as pd

'''
INSTRUCTIONS

*   Import the data with Pandas (stored in the file 'prices.csv').
*   Convert the index of data to datetime.
*   Loop through each column of data and plot the the column's values over time.
'''

# Read in the data
data = pd.read_csv('../datasets/prices.csv', index_col=0)

# Convert the index of the DataFrame to datetime
data.index = pd.to_datetime(data.index)
print(data.head())

# Loop through each column, plot its values over time
fig, ax = plt.subplots()
for column in data.columns:
    data[column].plot(ax=ax, label=column)
ax.legend()
plt.show()