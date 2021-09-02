'''
Confidence interval on the rate of no-hitters

Consider again the inter-no-hitter intervals for the modern era of baseball. Generate 10,000 bootstrap replicates of the optimal parameter <tau>. Plot a histogram of your replicates and report a 95% confidence interval.
'''

import matplotlib.pyplot as plt
import numpy as np

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

def bootstrap_replicate_1d(data, func):
    return func(np.random.choice(data, size=len(data)))

def draw_bs_reps(data, func, size=1):
    return np.array([bootstrap_replicate_1d(data, func) for _ in range(size)])

'''
INSTRUCTIONS

*   Generate 10000 bootstrap replicates of <tau> from the nohitter_times data using your draw_bs_reps() function. Recall that the the optimal <tau> is calculated as the mean of the data.
*   Compute the 95% confidence interval using np.percentile() and passing in two arguments: The array bs_replicates, and the list of percentiles - in this case 2.5 and 97.5.
*   Print the confidence interval.
*   Plot a histogram of your bootstrap replicates. This has been done for you, so hit 'Submit Answer' to see the plot!
'''

# Draw bootstrap replicates of the mean no-hitter time (equal to tau): bs_replicates
bs_replicates = draw_bs_reps(nohitter_times, np.mean, size=10000)

# Compute the 95% confidence interval: conf_int
conf_int = np.percentile(bs_replicates, [2.5, 97.5])

# Print the confidence interval
print('95% confidence interval =', conf_int, 'games')

# Plot the histogram of the replicates
_ = plt.hist(bs_replicates, bins=50, normed=True)
_ = plt.xlabel(r'$\tau$ (games)')
_ = plt.ylabel('PDF')

# Show the plot
plt.show()
