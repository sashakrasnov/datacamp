'''
Plotting the temperature

In this exercise, you'll examine the temperature columns from the weather dataset to assess whether the data seems trustworthy. First you'll print the summary statistics, and then you'll visualize the data using a box plot.

When deciding whether the values seem reasonable, keep in mind that the temperature is measured in degrees Fahrenheit, not Celsius!
'''

import pandas as pd
import matplotlib.pyplot as plt

'''
INSTRUCTIONS

*   Read weather.csv into a DataFrame named weather.
*   Select the temperature columns (TMIN, TAVG, TMAX) and print their summary statistics using the .describe() method.
*   Create a box plot to visualize the temperature columns.
*   Display the plot.
'''

# Read 'weather.csv' into a DataFrame named 'weather'
weather = pd.read_csv('../datasets/weather.csv')

# Describe the temperature columns
print(weather[['TMIN', 'TAVG', 'TMAX']].describe())

# Create a box plot of the temperature columns
weather[['TMIN', 'TAVG', 'TMAX']].plot(kind='box')

# Display the plot
plt.show()