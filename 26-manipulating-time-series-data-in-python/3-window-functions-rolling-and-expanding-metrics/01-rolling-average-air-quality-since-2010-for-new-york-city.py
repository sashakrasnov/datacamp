'''
Rolling average air quality since 2010 for new york city

The last video was about rolling window functions. To practice this new tool, you'll start with air quality trends for New York City since 2010. In particular, you'll be using the daily Ozone concentration levels provided by the Environmental Protection Agency to calculate & plot the 90 and 360 day rolling average.
'''

import pandas as pd
import matplotlib.pyplot as plt

'''
INSTRUCTIONS

We have already imported pandas as pd and matplotlib.pyplot as plt.

*   Use pd.read_csv() to import 'ozone_nyc.csv', creating a DateTimeIndex from the 'date' column using parse_dates and index_col, and assign the result to data.
*   Add the columns '90D' and '360D' containing the 90 and 360 rolling calendar day .mean() for the column 'Ozone'.
*   Plot data starting 2010, setting 'New York City' as title.
'''

# Import and inspect ozone data here
data = pd.read_csv('../datasets/air_quality_data/ozone_nyc.csv', index_col='date', parse_dates=['date'])
print(data.info())

# Calculate 90d and 360d rolling mean for the last price
data['90D'] = data.Ozone.rolling(window='90D').mean()
data['360D'] = data.Ozone.rolling(window='360D').mean()

# Plot data
data['2010':].plot(title='New York City')
plt.show()
