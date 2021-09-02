'''
Boxplots and Histograms

Boxplots represent a graphical rendition of the minimum, median, quartiles, and maximum of your data. You can generate a boxplot by calling the .boxplot() method on a DataFrame.

Another method to produce visual summaries is by leveraging histograms, which allow you to inspect the data and uncover its underlying distribution, as well as the presence of outliers and overall spread. An example of how to generate a histogram is shown below:

|   ax = co2_levels.plot(kind='hist', bins=100)

Here, we used the standard .plot() method but specified the kind argument to be 'hist'. In addition, we also added the bins=100 parameter, which specifies how many intervals (i.e bins) we should cut our data into.
'''

import pandas as pd
import matplotlib.pyplot as plt

co2_levels = pd.read_csv('../datasets/ch2_co2_levels.csv', index_col=0, parse_dates=True)
co2_levels = co2_levels.fillna(method='bfill')

'''
INSTRUCTIONS 1/2

*   Using the co2_levels DataFrame, produce a boxplot of the CO2 level data.
'''

# Generate a boxplot
ax = co2_levels.boxplot()

# Set the labels and display the plot
ax.set_xlabel('CO2', fontsize=10)
ax.set_ylabel('Boxplot CO2 levels in Maui Hawaii', fontsize=10)
plt.legend(fontsize=10)
plt.show()

'''
INSTRUCTIONS 2/2

*   Using the co2_levels DataFrame, produce a histogram plot of the CO2 level data with 50 bins.
'''

# Generate a histogram
ax = co2_levels.plot(kind='hist', bins=50, fontsize=6)

# Set the labels and display the plot
ax.set_xlabel('CO2', fontsize=10)
ax.set_ylabel('Histogram of CO2 levels in Maui Hawaii', fontsize=10)
plt.legend(fontsize=10)
plt.show()