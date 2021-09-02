'''
Add vertical and horizontal markers

Additional annotations can help further emphasize specific observations or events. Here, you will learn how to highlight significant events by adding markers at specific timestamps of your time series plot. The matplotlib library makes it possible to draw vertical and horizontal lines to identify particular dates.

Recall that the index of the discoveries DataFrame are of the datetime type, so the x-axis values of a plot will also contain dates, and it is possible to directly input a date when annotating your plots with vertical lines. For example, a vertical line at January 1, 1945 can be added to your plot by using the command:

|   ax.axvline('1945-01-01', linestyle='--')
'''

import pandas as pd
import matplotlib.pyplot as plt

url_discoveries = '../datasets/ch1_discoveries.csv'

discoveries = pd.read_csv(url_discoveries)

discoveries['date'] = pd.to_datetime(discoveries.date)
discoveries = discoveries.set_index('date')

'''
INSTRUCTIONS

*   Add a red vertical line at the date January 1, 1939 using the .axvline() method.
*   Add a green horizontal line at the y-axis value 4 using the .axhline() method.
'''

# Plot your the discoveries time series
ax = discoveries.plot(color='blue', fontsize=6)

# Add a red vertical line
ax.axvline(x='1939-01-01', color='red', linestyle='--')

# Add a green horizontal line
ax.axhline(y=4, color='green', linestyle='--')

plt.show()