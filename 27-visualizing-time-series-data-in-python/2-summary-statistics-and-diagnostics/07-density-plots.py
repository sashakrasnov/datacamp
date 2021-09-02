'''
Density plots

In practice, histograms can be a substandard method for assessing the distribution of your data because they can be strongly affected by the number of bins that have been specified. Instead, kernel density plots represent a more effective way to view the distribution of your data. An example of how to generate a density plot of is shown below:

|   ax = df.plot(kind='density', linewidth=2)

The standard .plot() method is specified with the kind argument set to 'density'. We also specified an additional parameter linewidth, which controls the width of the line to be plotted.
'''

import pandas as pd
import matplotlib.pyplot as plt

co2_levels = pd.read_csv('../datasets/ch2_co2_levels.csv', index_col=0, parse_dates=True)
co2_levels = co2_levels.fillna(method='bfill')

'''
INSTRUCTIONS

*   Using the co2_levels DataFrame, produce a density plot of the CO2 level data with line width parameter of 4.
*   Annotate the x-axis labels of your boxplot with the string 'CO2'.
*   Annotate the y-axis labels of your boxplot with the string 'Density plot of CO2 levels in Maui Hawaii'.
'''

# Display density plot of CO2 levels values
ax = co2_levels.plot(kind='density', linewidth=4, fontsize=6)

# Annotate x-axis labels
ax.set_xlabel('CO2', fontsize=10)

# Annotate y-axis labels
ax.set_ylabel('Density plot of CO2 levels in Maui Hawaii', fontsize=10)

plt.show()