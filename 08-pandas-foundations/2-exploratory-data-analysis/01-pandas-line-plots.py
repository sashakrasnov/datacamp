'''
pandas line plots

In the previous chapter, you saw that the .plot() method will place the Index values on the x-axis by default. In this exercise, you'll practice making line plots with specific columns on the x and y axes.

You will work with a dataset consisting of monthly stock prices in 2015 for AAPL, GOOG, and IBM. The stock prices were obtained from Yahoo Finance. Your job is to plot the 'Month' column on the x-axis and the AAPL and IBM prices on the y-axis using a list of column names.

All necessary modules have been imported for you, and the DataFrame is available in the workspace as df. Explore it using methods such as .head(), .info(), and .describe() to see the column names.
'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../datasets/messy_stock_data.tsv', comment='#', skiprows=3, sep=' ').set_index('name').T

df.index.name = 'Month'
df.reset_index(inplace=True)

'''
INSTRUCTIONS

*   Create a list of y-axis column names called y_columns consisting of 'APPLE' and 'IBM'.
*   Generate a line plot with x='Month' and y=y_columns as inputs.
*   Give the plot a title of 'Monthly stock prices'.
*   Specify the y-axis label.
*   Display the plot.
'''

# Create a list of y-axis column names: y_columns
y_columns = ['APPLE', 'IBM']

# Generate a line plot
df.plot(x='Month', y=y_columns)

# Add the title
plt.title('Monthly stock prices')

# Add the y-axis label
plt.ylabel('Price ($US)')

# Display the plot
plt.show()
