'''
Analyze the airline dataset

In Chapter 2 you learned:

*   How to check for the presence of missing values, and how to collect summary statistics of time series data contained in a pandas DataFrame.
*   To generate boxplots of your data to quickly gain insight in your data.
*   Display aggregate statistics of your data using groupby().

In this exercise, you will apply all these concepts on the airline DataFrame.
'''

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

airline = pd.read_csv('../datasets/ch3_airline_passengers.csv', index_col=0, parse_dates=True)

'''
INSTRUCTIONS 1/3

*   Print the numbers of missing values in the airline DataFrame.
*   Print the summary statistics of all the numeric columns in airline.
'''

# Print out the number of missing values
print(airline.isnull().sum())

# Print out summary statistics of the airline DataFrame
print(airline.describe())

'''
INSTRUCTIONS 2/3

*   Generate a boxplot of the monthly volume of airline passengers data.
'''

# Display boxplot of airline values
ax = airline.boxplot()

# Specify the title of your plot
ax.set_title('Boxplot of Monthly Airline\nPassengers Count', fontsize=20)
plt.show()

'''
INSTRUCTIONS 3/3

*   Extract the month from the index of airline.
*   Compute the mean number of passengers per month in airline and assign it to mean_airline_by_month.
*   Plot the mean number of passengers per month in airline.
'''

# Get month for each dates from the index of airline
index_month = airline.index.month

# Compute the mean number of passengers for each month of the year
mean_airline_by_month = airline.groupby(index_month).mean()

# Plot the mean number of passengers for each month of the year
mean_airline_by_month.plot()
plt.legend(fontsize=20)
plt.show()