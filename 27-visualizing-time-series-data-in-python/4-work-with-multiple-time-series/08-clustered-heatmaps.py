'''
Clustered heatmaps

Heatmaps are extremely useful to visualize a correlation matrix, but clustermaps are better. A Clustermap allows to uncover structure in a correlation matrix by producing a hierarchically-clustered heatmap:

|   df_corr = df.corr()
|
|   fig = sns.clustermap(df_corr)
|   plt.setp(fig.ax_heatmap.xaxis.get_majorticklabels(), rotation=90)
|   plt.setp(fig.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)

To prevent overlapping of axis labels, you can reference the Axes from the underlying fig object and specify the rotation. You can learn about the arguments to the clustermap() function here (https://seaborn.pydata.org/generated/seaborn.clustermap.html).
'''

import pandas as pd
import matplotlib.pyplot as plt

meat = pd.read_csv('../datasets/ch4_meat.csv', index_col=0, parse_dates=True)

'''
INSTRUCTIONS

*   Import seaborn as sns.
*   Compute the correlation between all columns in the meat DataFrame using the Pearson method and assign the results to a new variable called corr_meat.
*   Plot the clustermap of corr_meat.
'''

# Import seaborn library
import seaborn as sns

# Get correlation matrix of the meat DataFrame
corr_meat = meat.corr(method='pearson')

# Customize the heatmap of the corr_meat correlation matrix and rotate the x-axis labels
fig = sns.clustermap(corr_meat,
                     row_cluster=True,
                     col_cluster=True,
                     figsize=(10, 10))

plt.setp(fig.ax_heatmap.xaxis.get_majorticklabels(), rotation=90)
plt.setp(fig.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)
plt.show()