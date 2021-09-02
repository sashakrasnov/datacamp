'''
EDA: mean differences between odd and even splits

To investigate the differences between odd and even splits, you first need to define a difference metric. In previous exercises, you investigated the improvement of moving from a low-numbered lane to a high-numbered lane, defining f = (Ta - Tb) / Ta. There, the ta in the denominator served as our reference time for improvement. Here, you are considering both improvement and decline in performance depending on the direction of swimming, so you want the reference to be an average. So, we will define the fractional difference as f = 2(Ta - Tb) / (Ta + Tb).

Your task here is to plot the mean fractional difference between odd and even splits versus lane number. I have already calculated the mean fractional differences for the 2013 and 2015 Worlds for you, and they are stored in f_13 and f_15. The corresponding lane numbers are in the array lanes.
'''

import numpy as np
import matplotlib.pyplot as plt

# Original datasets

f_13 = np.array([
       -0.01562214, -0.01463810, -0.00977673, -0.00525713,  0.00204104,
        0.00381014,  0.00756640,  0.01525869])

f_15 = np.array([
       -0.00516018, -0.00392952, -0.00099284,  0.00059953, -0.00242400,
       -0.00451099,  0.00047467,  0.00081962])

lanes = np.array([1, 2, 3, 4, 5, 6, 7, 8])

'''
INSTRUCTIONS

*   Plot f_13 versus lanes using keyword arguments marker='.', markersize=12, and linestyle='none'.
*   Do the same for f_15 versus lanes.
*   Label the x-axis 'lane', y-axis 'frac. diff. (odd - even)', and show it.
'''

# Plot the the fractional difference for 2013 and 2015
_ = plt.plot(lanes, f_13, marker='.', markersize=12, linestyle='none')
_ = plt.plot(lanes, f_15, marker='.', markersize=12, linestyle='none')

# Add a legend
_ = plt.legend((2013, 2015))

# Label axes and show plot

_ = plt.xlabel('lane')
_ = plt.ylabel('frac. diff. (odd - even)')
plt.show()
