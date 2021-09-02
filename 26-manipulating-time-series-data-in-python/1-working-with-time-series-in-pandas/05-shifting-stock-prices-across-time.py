'''
Set and change time series frequency

In the video, you have seen how to assign a frequency to a DateTimeIndex, and then change this frequency.

Now, you'll use data on the daily carbon monoxide concentration in NYC, LA and Chicago from 2005-17.

You'll set the frequency to calendar daily and then resample to monthly frequency, and visualize both series to see how the different frequencies affect the data.
'''

import pandas as pd
import matplotlib.pyplot as plt

'''
INSTRUCTIONS

We have already imported pandas as pd and matplotlib.pyplot as plt and we have already loaded the co_cities.csv file in a variable co.

*   Inspect co using .info().
*   Use .asfreq() to set the frequency to calendar daily.
*   Show a plot of 'co' using subplots=True.
*   Change the the frequency to monthly using the alias 'M'.
*   Show another plot of co using subplots=True.
'''

# Import data here
google = pd.read_csv('../datasets/stock_data/google.csv', index_col='Date', parse_dates=['Date'])

# Set data frequency to business daily
google = google.asfreq('B')

# Create 'lagged' and 'shifted'
google['lagged'] = google.Close.shift(periods=-90)
google['shifted'] = google.Close.shift(periods=90)

# Plot the google price series
google.plot(subplots=True)
plt.show()
