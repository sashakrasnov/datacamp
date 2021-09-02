'''
EDA of beak length and depth

The beak length data are stored as bl_1975 and bl_2012, again with units of millimeters (mm). You still have the beak depth data stored in bd_1975 and bd_2012. Make scatter plots of beak depth (y-axis) versus beak length (x-axis) for the 1975 and 2012 specimens.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

bd = {}
bl = {}

for y in [1975, 2012]:
    df = pd.read_csv('../datasets/finch_beaks_{}.csv'.format(y), skiprows=1, header=None)

    scns = (df[1] == 'scandens')

    bl[y] = df[scns][2].values
    bd[y] = df[scns][3].values

'''
INSTRUCTIONS

*   Make a scatter plot of the 1975 data. Use the color='blue' keyword argument. Also use an alpha=0.5 keyword argument to have transparency in case data points overlap.
*   Do the same for the 2012 data, but use the color='red' keyword argument.
*   Add a legend and label the axes.
*   Show your plot.
'''

# Make scatter plot of 1975 data
_ = plt.plot(bl[1975], bd[1975], marker='.', linestyle='none', color='blue', alpha=0.5)

# Make scatter plot of 2012 data
_ = plt.plot(bl[2012], bd[2012], marker='.', linestyle='none', color='red', alpha=0.5)

# Label axes and make legend
_ = plt.xlabel('beak length (mm)')
_ = plt.ylabel('beak depth (mm)')
_ = plt.legend(('1975', '2012'), loc='upper left')

# Show the plot
plt.show()
