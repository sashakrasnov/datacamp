'''
Display aggregated values

You may sometimes be required to display your data in a more aggregated form. For example, the co2_levels data contains weekly data, but you may need to display its values aggregated by month of year. In datasets such as the co2_levels DataFrame where the index is a datetime type, you can extract the year of each dates in the index:

|   # extract of the year in each dates of the df DataFrame
|   index_year = df.index.year

To extract the month or day of the dates in the indices of the df DataFrame, you would use df.index.month and df.index.day, respectively. You can then use the extracted year of each indices in the co2_levels DataFrame and the groupby function to compute the mean CO2 levels by year:

|   df_by_year = df.groupby(index_year).mean()
'''

import pandas as pd
import matplotlib.pyplot as plt

co2_levels = pd.read_csv('../datasets/ch2_co2_levels.csv', index_col=0, parse_dates=True)
co2_levels = co2_levels.fillna(method='bfill')

'''
INSTRUCTIONS

*   Extract the month for each of the dates in the index of the co2_levels DataFrame and assign the values to a variable called index_month.
*   Using the groupby and mean functions from the pandas library, compute the monthly mean CO2 levels in the co2_levels DataFrame and assign that to a new DataFrame called mean_co2_levels_by_month.
*   Plot the values of the mean_co2_levels_by_month DataFrame using a fontsize of 6 for the axis ticks.
'''

# Get month for each dates in the index of co2_levels
index_month = co2_levels.index.month

# Compute the mean CO2 levels for each month of the year
mean_co2_levels_by_month = co2_levels.groupby(index_month).mean()

# Plot the mean CO2 levels for each month of the year
mean_co2_levels_by_month.plot(fontsize=6)

# Specify the fontsize on the legend
plt.legend(fontsize=10)

# Show plot
plt.show()