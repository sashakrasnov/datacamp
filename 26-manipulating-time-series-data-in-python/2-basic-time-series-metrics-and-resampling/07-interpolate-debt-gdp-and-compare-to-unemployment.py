'''
Interpolate debt/GDP and compare to unemployment

Since you have learned how to interpolate time series, you can now apply this new skill to the quarterly debt/GDP series, and compare the result to the monthly unemployment rate.
'''

import pandas as pd
import matplotlib.pyplot as plt

'''
INSTRUCTIONS

We have imported pandas as pd and matplotlib.pyplot as plt for you.

*   Use pd.read_csv() to import 'debt_unemployment.csv', creating a DateTimeIndex from the 'date' column using parse_dates and index_col, and assign the result to data. print() the .info() of the data.
*   Apply .interpolate() to data and assign this to interpolated, then inspect the result.
*   Plot interpolated with 'Unemployment' on the secondary_y axis.
'''

# Import & inspect data here
data = pd.read_csv('../datasets/stock_data/debt_unemployment.csv', index_col='date', parse_dates=['date'])

print(data.info())

# Interpolate and inspect here
interpolated = data.interpolate()

print(interpolated.info())

# Plot interpolated data here
interpolated.plot(secondary_y='Unemployment')
plt.show()
