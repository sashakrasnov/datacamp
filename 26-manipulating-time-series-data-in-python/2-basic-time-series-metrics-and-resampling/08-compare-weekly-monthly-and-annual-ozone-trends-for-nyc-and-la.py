'''
Compare weekly, monthly and annual ozone trends for NYC & LA

You have seen in the video how to downsample and aggregate time series on air quality.

First, you'll apply this new skill to ozone data for both NYC and LA since 2000 to compare the air quality trend at weekly, monthly and annual frequencies and explore how different resampling periods impact the visualization.
'''

import pandas as pd
import matplotlib.pyplot as plt

'''
INSTRUCTIONS

We have again imported pandas as pd and matplotlib.pyplot as plt for you.

*   Use pd.read_csv() to import 'ozone_nyla.csv' and set a DateTimeIndex based on the 'date' column using parse_dates and index_col, assign the result to ozone and inspect using .info().
*   Apply .resample() with weekly frequency ('W') to ozone, aggregate using .mean() and plot the result.
*   Repeat with monthly ('M') and annual ('A') frequencies, plotting each result.
'''

# Import and inspect data here
ozone = pd.read_csv('../datasets/air_quality_data/ozone_nyla.csv', index_col='date', parse_dates=['date'])
print(ozone.info())

# Calculate and plot the weekly average ozone trend
ozone.resample('W').mean().plot()
plt.show()

# Calculate and plot the monthly average ozone trend
ozone.resample('M').mean().plot()
plt.show()

# Calculate and plot the annual average ozone trend
ozone.resample('A').mean().plot()
plt.show()
