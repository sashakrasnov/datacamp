'''
Set and change time series frequency

In the video, you have seen how to assign a frequency to a DateTimeIndex, and then change this frequency.

Now, you'll use data on the daily carbon monoxide concentration in NYC, LA and Chicago from 2005-17.

You'll set the frequency to calendar daily and then resample to monthly frequency, and visualize both series to see how the different frequencies affect the data.
'''

import pandas as pd
import matplotlib.pyplot as plt

co = pd.read_csv('../datasets/air_quality_data/co_cities.csv', index_col=0, parse_dates=True)

'''
INSTRUCTIONS

We have already imported pandas as pd and matplotlib.pyplot as plt and we have already loaded the co_cities.csv file in a variable co.

*   Inspect co using .info().
*   Use .asfreq() to set the frequency to calendar daily.
*   Show a plot of 'co' using subplots=True.
*   Change the the frequency to monthly using the alias 'M'.
*   Show another plot of co using subplots=True.
'''

# Inspect data
print(co.info())

# Set the frequency to calendar daily
co = co.asfreq('D')

# Plot the data
co.plot(subplots=True)
plt.show()

# Set frequency to monthly
co = co.asfreq('M')

# Plot the data
co.plot(subplots=True)
plt.show()
