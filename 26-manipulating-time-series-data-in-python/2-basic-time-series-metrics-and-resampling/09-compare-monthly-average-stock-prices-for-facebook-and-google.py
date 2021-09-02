'''
Compare monthly average stock prices for Facebook and Google

Now, you'll apply your new resampling skills to daily stock price series for Facebook and Google for the 2015-2016 period to compare the trend of the monthly averages.
'''

import pandas as pd
import matplotlib.pyplot as plt

'''
INSTRUCTIONS

We have again imported pandas as pd and matplotlib.pyplot as plt for you.

*   Use pd.read_csv() to import 'stocks.csv' and set a DateTimeIndex based on the 'date' column using parse_dates and index_col, assign the result to stocks and inspect using .info().
*   Create monthly_average by applying .resample() with monthly frequency to data, using .mean() to aggregate. Plot the result using subplots.
'''

# Import and inspect data here
stocks = pd.read_csv('../datasets/stock_data/goog_fb.csv', index_col='date', parse_dates=['date'])
print(stocks.info())

# Calculate and plot the monthly averages
monthly_average = stocks.resample('M').mean()
monthly_average.plot(subplots=True)
plt.show()
