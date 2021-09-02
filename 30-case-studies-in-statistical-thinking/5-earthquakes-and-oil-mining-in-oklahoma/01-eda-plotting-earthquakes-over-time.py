'''
EDA: Plotting earthquakes over time

Make a plot where the y-axis is the magnitude and the x-axis is the time of all earthquakes in Oklahoma between 1980 and the first half of 2017. Each dot in the plot represents a single earthquake. The time of the earthquakes, as decimal years, is stored in the Numpy array time, and the magnitudes in the Numpy array mags.
'''

import numpy as np
import pandas as pd
import dc_stat_think as dcst
import matplotlib.pyplot as plt

df = pd.read_csv('../datasets/oklahoma_earthquakes_1950-2017.csv', comment='#', index_col='time', parse_dates=True, usecols=['time','mag'])

time = np.array([d.timestamp() / 31556925.9747 + 1970 for d in df['1980-01':'2017-06'].index.to_pydatetime()])
mags = df['1980-01':'2017-06'].mag.values

'''
INSTRUCTIONS

*   Plot the magnitude (mags) versus time (time) using plt.plot() with keyword arguments marker='.' and linestyle='none'. Also use the keyword argument alpha=0.1 to make the points transparent to better visualize overlapping points.
*   Label the x-axis 'time (year)', y-axis 'magnitude', and show the plot.
'''

# Plot time vs. magnitude
_ = plt.plot(time, mags, marker='.', linestyle='none', alpha=0.1)

# Label axes and show the plot
_ = plt.xlabel('time (year)')
_ = plt.ylabel('magnitude')
plt.show()
