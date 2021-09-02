'''
Computing percentage change in fraction of medals won

Here, you'll start with the DataFrames editions, medals, medal_counts, & fractions from prior exercises.

To see if there is a host country advantage, you first want to see how the fraction of medals won changes from edition to edition.

The expanding mean provides a way to see this down each column. It is the value of the mean with all the data available up to that point in time. If you are interested in learning more about pandas' expanding transformations, this section of the pandas documentation has additional information.

INSTRUCTIONS

*   Create mean_fractions by chaining the methods .expanding().mean() to fractions.
*   Compute the percentage change in mean_fractions down each column by applying .pct_change() and multiplying by 100. Assign the result to fractions_change.
*   Reset the index of fractions_change using the .reset_index() method. This will make 'Edition' an ordinary column.
*   Print the first and last 5 rows of the DataFrame fractions. This has been done for you, so hit 'Submit Answer' to see the results!
'''

import pandas as pd

editions = pd.read_csv('../datasets/summer-olympic-medals/Summer Olympic medalists 1896 to 2008 - EDITIONS.tsv', sep='\t')[['Edition', 'Grand Total', 'City', 'Country']]

medals = pd.read_csv('../datasets/summer-olympic-medals/Summer Olympic medalists 1896 to 2008 - ALL MEDALISTS.tsv', sep='\t', skiprows=4)[['Athlete', 'NOC', 'Medal', 'Edition']]

medal_counts = medals.pivot_table(aggfunc='count', index='Edition', values='Athlete', columns='NOC')

totals = editions.set_index('Edition')
totals = totals['Grand Total']

fractions = medal_counts.divide(totals, axis='rows')

# ---

# Apply the expanding mean: mean_fractions
mean_fractions = fractions.expanding().mean()

# Compute the percentage change: fractions_change
fractions_change = mean_fractions.pct_change() * 100

# Reset the index of fractions_change: fractions_change
fractions_change = fractions_change.reset_index()

# Print first & last 5 rows of fractions_change
print(fractions_change.head())
print(fractions_change.tail())
