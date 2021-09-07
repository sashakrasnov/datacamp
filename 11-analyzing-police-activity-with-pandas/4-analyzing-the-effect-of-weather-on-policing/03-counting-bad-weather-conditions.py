'''
Counting bad weather conditions

The weather DataFrame contains 20 columns that start with 'WT', each of which represents a bad weather condition. For example:

*   WT05 indicates "Hail"
*   WT11 indicates "High or damaging winds"
*   WT17 indicates "Freezing rain"

For every row in the dataset, each WT column contains either a 1 (meaning the condition was present that day) or NaN (meaning the condition was not present).

In this exercise, you'll quantify "how bad" the weather was each day by counting the number of 1 values in each row.
'''

import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv('../datasets/weather.csv')

'''
INSTRUCTIONS

*   Copy the columns WT01 through WT22 from weather to a new DataFrame named WT.
*   Calculate the sum of each row in WT, and store the results in a new weather column named bad_conditions.
*   Replace any missing values in bad_conditions with a 0. (This has been done for you.)
*   Create a histogram to visualize bad_conditions, and then display the plot.
'''

# Copy 'WT01' through 'WT22' to a new DataFrame
WT = weather.loc[:, 'WT01':'WT22']

# Calculate the sum of each row in 'WT'
weather['bad_conditions'] = WT.sum(axis='columns')

# Replace missing values in 'bad_conditions' with '0'
weather['bad_conditions'] = weather.bad_conditions.fillna(0).astype('int')

# Create a histogram to visualize 'bad_conditions'
weather.bad_conditions.plot(kind='hist')

# Display the plot
plt.show()