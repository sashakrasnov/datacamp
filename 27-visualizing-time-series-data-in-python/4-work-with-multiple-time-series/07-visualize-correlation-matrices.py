'''
Visualize correlation matrices

The correlation matrix generated in the previous exercise can be plotted using a heatmap. To do so, you can leverage the heatmap() function from the seaborn library which contains several arguments to tailor the look of your heatmap.

|   df_corr = df.corr()
|
|   sns.heatmap(df_corr)
|   plt.xticks(rotation=90)
|   plt.yticks(rotation=0) 

You can use the .xticks() and .yticks() methods to rotate the axis labels so they don't overlap.

To learn about the arguments to the heatmap() function, refer to this page (https://seaborn.pydata.org/generated/seaborn.heatmap.html).
'''

import pandas as pd
import matplotlib.pyplot as plt

meat = pd.read_csv('../datasets/ch4_meat.csv', index_col=0, parse_dates=True)

'''
INSTRUCTIONS

*   Import seaborn as sns.
*   Compute the correlation between all columns in the meat DataFrame using the Spearman method and assign the results to a new variable called corr_meat.
*   Plot the heatmap of corr_meat.
'''

# Import seaborn library
import seaborn as sns

# Get correlation matrix of the meat DataFrame
corr_meat = meat.corr(method='spearman')

# Customize the heatmap of the corr_meat correlation matrix
sns.heatmap(corr_meat,
            annot=True,
            linewidths=0.4,
            annot_kws={"size": 10})

plt.xticks(rotation=90)
plt.yticks(rotation=0) 
plt.show()