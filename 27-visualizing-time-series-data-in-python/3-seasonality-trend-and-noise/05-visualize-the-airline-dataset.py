'''
Visualize the airline dataset

You will now review the contents of chapter 1. You will have the opportunity to work with a new dataset that contains the monthly number of passengers who took a commercial flight between January 1949 and December 1960.

We have printed the first 5 and the last 5 rows of the airline DataFrame for you to review.
'''

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

airline = pd.read_csv('../datasets/ch3_airline_passengers.csv', index_col=0, parse_dates=True)

'''
INSTRUCTIONS

*   Plot the time series of airline using a "blue" line plot.
*   Add a vertical line on this plot at December 1, 1955.
*   Specify the x-axis label on your plot: 'Date'.
*   Specify the title of your plot: 'Number of Monthly Airline Passengers'.
'''

# Plot the time series in your dataframe
ax = airline.plot(color='blue', fontsize=12)

# Add a red vertical line at the date 1955-12-01
ax.axvline('1955-12-01', color='red', linestyle='--')

# Specify the labels in your plot
ax.set_xlabel('Date', fontsize=12)
ax.set_title('Number of Monthly Airline Passengers', fontsize=12)
plt.show()