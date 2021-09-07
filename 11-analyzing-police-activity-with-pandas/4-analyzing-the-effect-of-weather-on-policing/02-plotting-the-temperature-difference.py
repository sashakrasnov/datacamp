'''
Plotting the temperature difference

In this exercise, you'll continue to assess whether the dataset seems trustworthy by plotting the difference between the maximum and minimum temperatures.

What do you notice about the resulting histogram? Does it match your expectations, or do you see anything unusual?
'''

import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv('../datasets/weather.csv')

'''
INSTRUCTIONS

*   Create a new column in the weather DataFrame named TDIFF that represents the difference between the maximum and minimum temperatures.
*   Print the summary statistics for TDIFF using the .describe() method.
*   Create a histogram with 20 bins to visualize TDIFF.
*   Display the plot.
'''

# Create a 'TDIFF' column that represents temperature difference
weather['TDIFF'] = weather['TMAX'] - weather['TMIN']

# Describe the 'TDIFF' column
print(weather['TDIFF'].describe())

# Create a histogram with 20 bins to visualize 'TDIFF'
weather.TDIFF.plot(kind='hist', bins=20)

# Display the plot
plt.show()