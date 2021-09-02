'''
Computing the K-S statistic

Write a function to compute the Kolmogorov-Smirnov statistic from two data sets, data1 and data2. In practice using hacker stats, the second data set will be samples from the theoretical distribution you are comparing your data to. Conveniently, the function you just selected for computing values of the formal ECDF is given as dcst.ecdf_formal().
'''

import numpy as np
import dc_stat_think as dcst

'''
INSTRUCTIONS

*   Compute the values of the convex corners of the formal ECDF for data1 using dcst.ecdf(). Store the results in the variables x and y.
*   Use dcst.ecdf_formal() to compute the values of the theoretical CDF, determined from data2, at the convex corners x. Store the result in the variable cdf.
*   Compute the distances between the concave corners of the formal ECDF and the theoretical CDF. Store the result as D_top.
*   Compute the distance between the convex corners of the formal ECDF and the theoretical CDF. Note that you will need to subtract 1/len(data1) from y to get the y-value at the convex corner. Store the result in D_bottom.
*   Return the K-S statistic as the maximum of all entries in D_top and D_bottom. You can pass D_top and D_bottom together as a tuple to np.max() to do this.
'''

def ks_stat(data1, data2):
    # Compute ECDF from data: x, y
    x, y = dcst.ecdf(data1)
    
    # Compute corresponding values of the target CDF
    cdf = dcst.ecdf_formal(x, data2)

    # Compute distances between concave corners and CDF
    D_top = y - cdf

    # Compute distance between convex corners and CDF
    D_bottom = cdf - y +1/len(data1)

    return np.max((D_top, D_bottom))

'''
You now have another useful function in your tool box. We have kindly put it in the dcst module for your future use.
'''