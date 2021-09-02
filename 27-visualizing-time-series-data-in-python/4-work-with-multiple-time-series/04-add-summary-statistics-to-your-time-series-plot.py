'''
Add summary statistics to your time series plot

It is possible to visualize time series plots and numerical summaries on one single graph by using the pandas API to matplotlib along with the table method:

|   # Plot the time series data in the DataFrame
|   ax = df.plot()
|
|   # Compute summary statistics of the df DataFrame
|   df_summary = df.describe()
|
|   # Add summary table information to the plot
|   ax.table(cellText=df_summary.values, 
|            colWidths=[0.3]*len(df.columns), 
|            rowLabels=df_summary.index, 
|            colLabels=df_summary.columns, 
|            loc='top')
'''

import pandas as pd
import matplotlib.pyplot as plt

meat = pd.read_csv('../datasets/ch4_meat.csv', index_col=0, parse_dates=True)

meat_mean = meat.mean().to_frame().transpose()
meat_mean.index = ['mean']

'''
INSTRUCTIONS

Review meat_mean in the shell -- a DataFrame that contains the mean of all the time series in meat.

*   Assign all the values in meat_mean to the cellText argument.
*   Assign all the values in index of meat_mean to the rowLabels argument.
*   Assign the column names of meat_mean to the colLabels argument.
'''

# Plot the meat data
ax = meat.plot(fontsize=6, linewidth=1)

# Add x-axis labels
ax.set_xlabel('Date', fontsize=6)

# Add summary table information to the plot
ax.table(cellText=meat_mean.values,
         colWidths = [0.15]*len(meat_mean.columns),
         rowLabels=meat_mean.index,
         colLabels=meat_mean.columns,
         loc='top')

# Specify the fontsize and location of your legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 0.95), ncol=3, fontsize=6)

# Show plot
plt.show()