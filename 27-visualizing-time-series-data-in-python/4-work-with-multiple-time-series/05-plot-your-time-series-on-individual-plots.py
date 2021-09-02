'''
Plot your time series on individual plots

It can be beneficial to plot individual time series on separate graphs as this may improve clarity and provide more context around each time series in your DataFrame.

It is possible to create a "grid" of individual graphs by "faceting" each time series by setting the subplots argument to True. In addition, the arguments that can be added are:

*   layout: specifies the number of rows x columns to use.
*   sharex and sharey: specifies whether the x-axis and y-axis values should be shared between your plots.
'''

import pandas as pd
import matplotlib.pyplot as plt

meat = pd.read_csv('../datasets/ch4_meat.csv', index_col=0, parse_dates=True)

'''
INSTRUCTIONS

*   Create a facetted plot of the meat DataFrame using a layout of 2 rows and 4 columns.
*   Ensure that the subgraphs do not share x-axis and y-axis values.
'''

# Create a facetted graph with 2 rows and 4 columns
meat.plot(subplots=True, 
          layout=(2,4),
          sharex=False,
          sharey=False,
          colormap='viridis', 
          fontsize=2, 
          legend=False, 
          linewidth=0.2)

plt.show()