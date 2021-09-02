'''
Add shaded regions to your plot

When plotting time series data in Python, it is also possible to highlight complete regions of your time series plot. In order to add a shaded region between January 1, 1936 and January 1, 1950, you can use the command:

|   ax.axvspan('1936-01-01', '1950-01-01', color='red' , alpha=0.5)

Here we specified the overall transparency of the region by using the alpha argument (where 0 is completely transparent and 1 is full color).
'''

import pandas as pd
import matplotlib.pyplot as plt

url_discoveries = '../datasets/ch1_discoveries.csv'

discoveries = pd.read_csv(url_discoveries)

discoveries['date'] = pd.to_datetime(discoveries.date)
discoveries = discoveries.set_index('date')

'''
INSTRUCTIONS

*   Use the .axvspan() method to add a vertical red shaded region between the dates of January 1, 1900 and January 1, 1915 with a transparency of 0.3.
*   Use the .axhspan() method to add a horizontal green shaded region between the values of 6 and 8 with a transparency of 0.3.
'''

# Plot your the discoveries time series
ax = discoveries.plot(color='blue', fontsize=6)

# Add a vertical red shaded region
ax.axvspan('1900-01-01', '1915-01-01', color='red', alpha=0.3)

# Add a horizontal green shaded region
ax.axhspan(6, 8, color='green', alpha=0.3)

plt.show()