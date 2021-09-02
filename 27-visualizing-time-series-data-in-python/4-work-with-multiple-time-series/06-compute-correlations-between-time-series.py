'''
Compute correlations between time series

The correlation coefficient can be used to determine how multiple variables (or a group of time series) are associated with one another. The result is a correlation matrix that describes the correlation between time series. Note that the diagonal values in a correlation matrix will always be 1, since a time series will always be perfectly correlated with itself.

Correlation coefficients can be computed with the pearson, kendall and spearman methods. A full discussion of these different methods is outside the scope of this course, but the pearson method should be used when relationships between your variables are thought to be linear, while the kendall and spearman methods should be used when relationships between your variables are thought to be non-linear.
'''

import pandas as pd
import matplotlib.pyplot as plt

meat = pd.read_csv('../datasets/ch4_meat.csv', index_col=0, parse_dates=True)

'''
INSTRUCTIONS 1/2

*   Print the correlation matrix between the beef and pork columns in the meat DataFrame using the Spearman method.
*   Based on the above matrix, print the correlation value between beef and pork columns.
'''

# Compute the correlation between the beef and pork columns using the spearman method
print(meat[['beef', 'pork']].corr(method='spearman'))

# Print the correlation between beef and pork columns
print(meat[['beef', 'pork']].corr(method='spearman').iloc[0,1])

'''
INSTRUCTIONS 2/2

*   Compute the correlation between the pork, veal and turkey columns in meat using the Pearson method. Based on these results, print the correlation between:
    *   veal and pork
    *   veal and turkey
    *   pork and turkey
'''

# Compute the correlation between the pork, veal and turkey columns using the pearson method
print(meat[['pork', 'veal', 'turkey']].corr(method='pearson'))

# Print the correlation between veal and pork columns
print(meat[['pork', 'veal', 'turkey']].corr(method='pearson').iloc[0,1])

# Print the correlation between veal and turkey columns
print(meat[['pork', 'veal', 'turkey']].corr(method='pearson').iloc[1,2])

# Print the correlation between pork and turkey columns
print(meat[['pork', 'veal', 'turkey']].corr(method='pearson').iloc[0,2])
