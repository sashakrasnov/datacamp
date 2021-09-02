'''
EDA: Comparing magnitudes before and after 2010

Make an ECDF of earthquake magnitudes from 1980 through 2009. On the same plot, show an ECDF of magnitudes of earthquakes from 2010 through mid-2017. The time of the earthquakes, as decimal years, are stored in the Numpy array time and the magnitudes in the Numpy array mags.
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

*   Use Boolean indexing to slice out the magnitudes of all earthquakes before 2010 and store the result in mags_pre. Similarly, generate a numpy array mags_post that has all magnitudes of earthquakes in and after 2010.
*   Use plt.plot() with a *dcst.ecdf(____) argument to make ECDFs for pre- and post- 2010 earthquake magnitudes. Remember to specify arguments for the marker and linestyle parameters.
*   Hit 'Submit Answer' to view the plot.
'''

# Get magnitudes before and after 2010
mags_pre = mags[time < 2010]
mags_post = mags[time >= 2010]

# Generate ECDFs
_ = plt.plot(*dcst.ecdf(mags_pre), marker='.', linestyle='none')
_ = plt.plot(*dcst.ecdf(mags_post), marker='.', linestyle='none')

# Label axes and show plot
_ = plt.xlabel('magnitude')
_ = plt.ylabel('ECDF')
plt.legend(('1980 though 2009', '2010 through mid-2017'), loc='upper left')
plt.show()

'''
Both curves seem to follow the Gutenberg-Richter Law, but with different completeness thresholds, probably due to improvements in sensing capabilities in more recent years.
'''