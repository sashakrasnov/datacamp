'''
Parkfield earthquake magnitudes

As usual, you will start with EDA and plot the ECDF of the magnitudes of earthquakes detected in the Parkfield region from 1950 to 2016. The magnitudes of all earthquakes in the region from the ANSS ComCat are stored in the Numpy array mags.

When you do it this time, though, take a shortcut in generating the ECDF. You may recall that putting an asterisk before an argument in a function splits what follows into separate arguments. Since dcst.ecdf() returns two values, we can pass them as the x, y positional arguments to plt.plot() as plt.plot(*dcst.ecdf(data_you_want_to_plot)).

You will use this shortcut in this exercise and going forward.
'''

import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt

mags = np.loadtxt('../datasets/parkfield_earthquakes_1950-2017.csv', delimiter=',', comments='#', skiprows=3, usecols=4)

'''
INSTRUCTIONS

*   Generate a plot of the ECDF in one line, using the *dcst.ecdf() approach describe above. Call plt.plot() with the marker='.' and linestyle='none' keyword arguments as usual.
*   Label the x-axis 'magnitude', y-axis 'ECDF', and show the plot.
'''

# Make the plot
plt.plot(*dcst.ecdf(mags), marker='.', linestyle='none')

# Label axes and show plot
_ = plt.xlabel('magnitude')
_ = plt.ylabel('ECDF')
plt.show()
