'''
Plotting violations by district

Now that you've created a frequency table focused on the "K" zones, you'll visualize the data to help you compare what violations are being caught in each zone.

First you'll create a bar plot, which is an appropriate plot type since you're comparing categorical data. Then you'll create a stacked bar plot in order to get a slightly different look at the data. Which plot do you find to be more insightful?
'''

import pandas as pd
import matplotlib.pyplot as plt

ri = pd.read_csv('../datasets/RI_cleaned.csv', low_memory=False)

ri.drop(['county_name', 'state'], axis='columns', inplace=True)
ri.dropna(subset=['driver_gender'], inplace=True)

ri['is_arrested'] = ri.is_arrested.astype('bool')

combined = ri.stop_date.str.cat(ri.stop_time, sep=' ')
ri['stop_datetime'] = pd.to_datetime(combined)

ri.set_index('stop_datetime', inplace=True)

all_zones = pd.crosstab(ri.district, ri.violation)

k_zones = all_zones.loc['Zone K1':'Zone K3']

'''
INSTRUCTIONS 1/2

*   Create a bar plot of k_zones.
*   Display the plot and examine it. What do you notice about each of the zones?
'''

# Create a bar plot of 'k_zones'
k_zones.plot(kind='bar')

# Display the plot
plt.show()

'''
INSTRUCTIONS 2/2

*   Create a stacked bar plot of k_zones.
*   Display the plot and examine it. Do you notice anything different about the data than you did previously?
'''

# Create a stacked bar plot of 'k_zones'
k_zones.plot(kind='bar', stacked=True)

# Display the plot
plt.show()