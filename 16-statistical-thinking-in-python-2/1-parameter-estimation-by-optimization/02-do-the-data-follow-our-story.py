'''
Do the data follow our story?

You have modeled no-hitters using an Exponential distribution. Create an ECDF of the real data. Overlay the theoretical CDF with the ECDF from the data. This helps you to verify that the Exponential distribution describes the observed data.

It may be helpful to remind yourself of the function you created in the previous course to compute the ECDF, as well as the code you wrote to plot it.
'''

import numpy as np
import matplotlib.pyplot as plt

nohitter_times = np.array([843, 1613, 1101,  215,  684,  814,  278,  324,  161,  219,  545,
                           715,  966,  624,   29,  450,  107,   20,   91, 1325,  124, 1468,
                           104, 1309,  429,   62, 1878, 1104,  123,  251,   93,  188,  983,
                           166,   96,  702,   23,  524,   26,  299,   59,   39,   12,    2,
                           308, 1114,  813,  887,  645, 2088,   42, 2090,   11,  886, 1665,
                          1084, 2900, 2432,  750, 4021, 1070, 1765, 1322,   26,  548, 1525,
                            77, 2181, 2752,  127, 2147,  211,   41, 1575,  151,  479,  697,
                           557, 2267,  542,  392,   73,  603,  233,  255,  528,  397, 1529,
                          1023, 1194,  462,  583,   37,  943,  996,  480, 1497,  717,  224,
                           219, 1531,  498,   44,  288,  267,  600,   52,  269, 1086,  386,
                           176, 2199,  216,   54,  675, 1243,  463,  650,  171,  327,  110,
                           774,  509,    8,  197,  136,   12, 1124,   64,  380,  811,  232,
                           192,  731,  715,  226,  605,  539, 1491,  323,  240,  179,  702,
                           156,   82, 1397,  354,  778,  603, 1001,  385,  986,  203,  149,
                           576,  445,  180, 1403,  252,  675, 1351, 2983, 1568,   45,  899,
                          3260, 1025,   31,  100, 2055, 4043,   79,  238, 3931, 2351,  595,
                           110,  215,    0,  563,  206,  660,  242,  577,  179,  157,  192,
                           192, 1848,  792, 1693,   55,  388,  225, 1134, 1172, 1555,   31,
                          1582, 1044,  378, 1687, 2915,  280,  765, 2819,  511, 1521,  745,
                          2491,  580, 2072, 6450,  578,  745, 1075, 1103, 1549, 1520,  138,
                          1202,  296,  277,  351,  391,  950,  459,   62, 1056, 1128,  139,
                           420,   87,   71,  814,  603, 1349,  162, 1027,  783,  326,  101,
                           876,  381,  905,  156,  419,  239,  119,  129,  467])
def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y

tau = np.mean(nohitter_times)

np.random.seed(42)

inter_nohitter_time = np.random.exponential(tau, 100000)

'''
INSTRUCTIONS

*   Compute an ECDF from the actual time between no-hitters (nohitter_times). Use the ecdf() function you wrote in the prequel course.
*   Create a CDF from the theoretical samples you took in the last exercise (inter_nohitter_time).
*   Plot x_theor and y_theor as a line using plt.plot(). Then overlay the ECDF of the real data x and y  as points. To do this, you have to specify the keyword arguments marker = '.' and linestyle = 'none' in addition to x and y inside plt.plot().
*   Set a 2% margin on the plot.
*   Show the plot.
'''

# Create an ECDF from real data: x, y
x, y = ecdf(nohitter_times)

# Create a CDF from theoretical samples: x_theor, y_theor
x_theor, y_theor = ecdf(inter_nohitter_time)

# Overlay the plots
plt.plot(x_theor, y_theor)
plt.plot(x, y, marker='.', linestyle='none')

# Margins and axis labels
plt.margins(0.02)
plt.xlabel('Games between no-hitters')
plt.ylabel('CDF')

# Show the plot
plt.show()
