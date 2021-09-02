'''
Your first plot!

Let's take everything you have learned so far and plot your first time series plot. You will set the groundwork by producing a time series plot of your data and labeling the axes of your plot, as this makes the plot more readable and interpretable for the intended audience.

matplotlib is the most widely used plotting library in Python, and would be the most appropriate tool for this job. Fortunately for us, the pandas library has implemented a .plot() method on Series and DataFrame objects that is a wrapper around matplotlib.pyplot.plot(), which makes it easier to produce plots.
'''

import pandas as pd
import matplotlib.pyplot as plt

url_discoveries = '../datasets/ch1_discoveries.csv'

discoveries = pd.read_csv(url_discoveries)

discoveries['date'] = pd.to_datetime(discoveries.date)

'''
INSTRUCTIONS

*   Set the 'date' column as the index of your DataFrame.
*   Using the discoveries DataFrame, plot the time series in your DataFrame using a "blue" line plot and assign it to ax.
*   Specify the x-axis label on your plot: 'Date'.
*   Specify the y-axis label on your plot: 'Number of great discoveries'.
'''

# Set the date column as the index of your DataFrame discoveries
discoveries = discoveries.set_index('date')

# Plot the time series in your DataFrame
ax = discoveries.plot(color='blue')

# Specify the x-axis label in your plot
ax.set_xlabel('Date')

# Specify the y-axis label in your plot
ax.set_ylabel('Number of great discoveries')

# Show plot
plt.show()