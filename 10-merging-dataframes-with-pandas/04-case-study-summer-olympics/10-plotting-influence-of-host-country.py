'''
Plotting influence of host country

This final exercise starts off with the DataFrames influence and editions in the namespace. Your job is to plot the influence of being a host country.

INSTRUCTIONS

*   Create a Series called change by extracting the 'Change' column from influence.
*   Create a bar plot of change using the .plot() method with kind='bar'. Save the result as ax to permit further customization.
*   Customize the bar plot of change to improve readability:
*   Apply the method .set_ylabel("% Change of Host Country Medal Count") toax.
*   Apply the method .set_title("Is there a Host Country Advantage?") to ax.
*   Apply the method .set_xticklabels(editions['City']) to ax.
*   Reveal the final plot using plt.show().
'''

import pandas as pd
from numpy import nan

editions = pd.read_csv('../datasets/summer-olympic-medals/Summer Olympic medalists 1896 to 2008 - EDITIONS.tsv', sep='\t')[['Edition', 'Grand Total', 'City', 'Country']]

medals = pd.read_csv('../datasets/summer-olympic-medals/Summer Olympic medalists 1896 to 2008 - ALL MEDALISTS.tsv', sep='\t', skiprows=4)[['Athlete', 'NOC', 'Medal', 'Edition']]

medal_counts = medals.pivot_table(aggfunc='count', index='Edition', values='Athlete', columns='NOC')

totals = editions.set_index('Edition')
totals = totals['Grand Total']

fractions = medal_counts.divide(totals, axis='rows')

mean_fractions = fractions.expanding().mean()

fractions_change = mean_fractions.pct_change() * 100
fractions_change = fractions_change.reset_index()

reshaped = pd.melt(fractions_change, id_vars='Edition', value_name='Change')

hosts = pd.DataFrame({'Edition': [1896.0,1900.0,1904.0,1908.0,1912.0,1920.0,1924.0,1928.0,1932.0,1936.0,1948.0,1952.0,1956.0,1960.0,1964.0,1968.0,1972.0,1976.0,1980.0,1984.0,1988.0,1992.0,1996.0,2000.0,2004.0,2008.0,nan,nan,nan],
                      'NOC': ['GRE','FRA','USA','GBR','SWE','BEL','FRA','NED','USA','GER','GBR','FIN','AUS','ITA','JPN','MEX',nan,'CAN',nan,'USA',nan,'ESP','USA','AUS','GRE','CHN','FRG','URS','KOR']},
                      index=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,1972,1980,1988])

merged = pd.merge(reshaped, hosts, how='inner')

influence = merged.set_index('Edition').sort_index()

# ---

# Import pyplot
import matplotlib.pyplot as plt

# Extract influence['Change']: change
change = influence['Change']

# Make bar plot of change: ax
ax = change.plot(kind='bar')

# Customize the plot to improve readability
ax.set_ylabel("% Change of Host Country Medal Count")
ax.set_title("Is there a Host Country Advantage?")
ax.set_xticklabels(editions['City'])

# Display the plot
plt.show()
