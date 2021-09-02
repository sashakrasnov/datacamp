'''
Graphical EDA of men's 200 free heats

In the heats, all contestants swim, the very fast and the very slow. To explore how the swim times are distributed, plot an ECDF of the men's 200 freestyle.
'''

import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt

# Original dataset
mens_200_free_heats = np.array([
       118.32, 107.73, 107.00, 106.39, 108.75, 117.74, 108.43, 111.96,
       114.36, 121.77, 108.23, 107.47, 118.41, 108.29, 106.00, 109.32,
       111.49, 112.92, 117.38, 110.95, 108.27, 111.78, 107.87, 110.77,
       109.05, 111.00, 108.77, 106.10, 106.61, 113.68, 108.20, 106.20,
       111.01, 109.25, 112.00, 118.55, 109.56, 108.18, 111.67, 108.09,
       110.04, 113.97, 109.91, 112.12, 111.65, 110.18, 116.36, 124.59,
       115.59, 121.01, 106.88, 108.96, 109.09, 108.67, 109.60, 111.85,
       118.54, 108.12, 124.38, 107.17, 107.48, 106.65, 106.91, 140.68,
       117.93, 120.66, 111.29, 107.10, 108.49, 112.43, 110.61, 110.38,
       109.87, 106.73, 107.18, 110.98, 108.55, 114.31, 112.05])
    
'''
INSTRUCTIONS

*   Generate x and y values for the ECDF using dcst.ecdf(). The swim times of the heats are stored in the numpy array mens_200_free_heats.
*   Plot the ECDF as dots. Remember to specify the appropriate marker and linestyle.
*   Label the axes and show the plot. Use 'time (s)' as the x-axis label and 'ECDF' as the y-axis label.
'''

# Generate x and y values for ECDF: x, y
x, y = dcst.ecdf(mens_200_free_heats)

# Plot the ECDF as dots
_ = plt.plot(x, y, marker='.', linestyle='none')

# Label axes and show plot
_ = plt.xlabel('time (s)')
_ = plt.ylabel('ECDF')
plt.show()
