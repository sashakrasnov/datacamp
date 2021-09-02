'''
Visualize multiple time series

If there are multiple time series in a single DataFrame, you can still use the .plot() method to plot a line chart of all the time series. Another interesting way to plot these is to use area charts. Area charts are commonly used when dealing with multiple time series, and can be used to display cumulated totals.

With the pandas library, you can simply leverage the .plot.area() method to produce area charts of the time series data in your DataFrame.
'''

import pandas as pd
import matplotlib.pyplot as plt

meat = pd.read_csv('../datasets/ch4_meat.csv', index_col=0, parse_dates=True)

'''
INSTRUCTIONS 1/2

*   Plot all the time series data in the meat DataFrame.
*   Make sure to specify a line width of 2 and a font size of 12.
'''

# Plot time series dataset
ax = meat.plot(linewidth=2, fontsize=12)

# Additional customizations
ax.set_xlabel('Date')
ax.legend(fontsize=15)

# Show plot
plt.show()

'''
INSTRUCTIONS 2/2

*   Plot an area chart all the time series data in the meat DataFrame.
'''

# Plot an area chart
ax = meat.plot.area(fontsize=12)

# Additional customizations
ax.set_xlabel('Date')
ax.legend(fontsize=15)

# Show plot
plt.show()