'''
EDA: finals versus semifinals

First, you will get an understanding of how athletes' performance changes from the semifinals to the finals by computing the fractional improvement from the semifinals to finals and plotting an ECDF of all of these values.

The arrays final_times and semi_times contain the swim times of the respective rounds. The arrays are aligned such that final_times[i] and semi_times[i] are for the same swimmer/event. If you are interested in the strokes/events, you can check out the data frame df in your namespace, which has more detailed information, but is not used in the analysis.
'''

import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt

# Original datasets
final_times = np.array([
     52.52,  24.12,  52.82,  24.36,  57.67, 116.41,  58.26,  27.66,
    125.81,  58.75,  27.92, 126.78,  25.93,  24.44,  27.26,  58.22,
    128.66,  24.39,  57.69, 143.61, 128.51,  30.74,  59.02,  27.11,
     57.85,  66.55, 142.76,  57.48,  25.37, 116.27,  54.76, 126.51,
     27.58, 130.20, 142.76,  57.05,  25.34,  58.86,  27.73,  25.78,
    142.76,  25.85,  24.51,  59.78,  27.99,  57.94, 126.78, 128.49,
     28.17, 116.19, 126.84, 127.76, 129.53,  67.10,  31.12, 115.32,
     67.60,  66.42,  30.11, 125.56,  66.43, 141.15, 143.19,  66.36,
     30.14, 116.79,  53.58,  53.17,  24.22,  25.64,  26.20, 116.16,
    127.64,  65.66,  30.13,  59.66, 143.59,  55.64,  52.70,  24.96,
     24.31,  67.17,  30.05,  31.14,  53.93,  24.57, 142.44, 115.16,
     59.40, 115.49,  54.00, 126.34,  30.20, 126.95,  59.99, 126.40
])

semi_times = np.array([
     53.00,  24.32,  52.84,  24.22,  57.59, 116.95,  58.56,  27.70,
    126.56,  59.05,  27.83, 127.57,  25.81,  24.38,  27.41,  58.05,
    128.99,  24.52,  57.52, 142.82, 128.16,  31.03,  59.33,  27.18,
     57.63,  66.28, 143.06,  57.36,  25.79, 116.44,  53.91, 127.08,
     27.67, 127.69, 141.99,  57.04,  25.27,  58.84,  27.63,  25.88,
    142.90,  25.71,  24.50,  59.71,  27.88,  57.77, 126.64, 129.16,
     28.01, 116.51, 126.18, 127.05, 129.04,  67.11,  30.90, 116.23,
     66.95,  66.21,  30.78, 126.36,  66.64, 142.15, 142.88,  65.64,
     29.98, 116.91,  53.38,  53.78,  24.23,  25.90,  25.91, 116.56,
    128.74,  65.60,  30.14,  59.55, 142.72,  55.74,  52.78,  25.06,
     24.31,  66.76,  30.39,  30.64,  53.81,  24.47, 142.04, 116.76,
     59.42, 116.37,  53.92, 127.79,  30.25, 127.52,  59.63, 127.57
])

'''
INSTRUCTIONS

*   Compute the fractional improvement from the semifinals to finals. Store the results as f.
*   Compute the x and y values for plotting the ECDF.
*   Plot the ECDF as dots.
'''

# Compute fractional difference in time between finals and semis
f = (semi_times - final_times) / semi_times

# Generate x and y values for the ECDF: x, y
x, y = dcst.ecdf(f)

# Make a plot of the ECDF
_ = plt.plot(x, y, marker='.', linestyle='none')

# Label axes and show plot
_ = plt.xlabel('f')
_ = plt.ylabel('ECDF')

plt.show()