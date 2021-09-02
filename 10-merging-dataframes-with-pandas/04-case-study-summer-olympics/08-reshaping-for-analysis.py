'''
Reshaping for analysis

This exercise starts off with fractions_change and hosts already loaded.

Your task here is to reshape the fractions_change DataFrame for later analysis.

Initially, fractions_change is a wide DataFrame of 26 rows (one for each Olympic edition) and 139 columns (one for the edition and 138 for the competing countries).

On reshaping with pd.melt(), as you will see, the result is a tall DataFrame with 3588 rows and 3 columns that summarizes the fractional change in the expanding mean of the percentage of medals won for each country in blocks.

INSTRUCTIONS
100XP
Create a DataFrame reshaped by reshaping the DataFrame fractions_change with pd.melt().
You'll need to use the keyword argument id_vars='Edition' to set the identifier variable.
You'll also need to use the keyword argument value_name='Change' to set the measured variables.
Print the shape of the DataFrames reshaped and fractions_change. This has been done for you.
Create a DataFrame chn by extracting all the rows from reshaped in which the three letter code for each country ('NOC') is 'CHN'.
Print the last 5 rows of the DataFrame chn using the .tail() method. This has been done for you, so hit 'Submit Answer' to see the results!
'''

import pandas as pd

editions = pd.read_csv('../datasets/summer-olympic-medals/Summer Olympic medalists 1896 to 2008 - EDITIONS.tsv', sep='\t')[['Edition', 'Grand Total', 'City', 'Country']]

medals = pd.read_csv('../datasets/summer-olympic-medals/Summer Olympic medalists 1896 to 2008 - ALL MEDALISTS.tsv', sep='\t', skiprows=4)[['Athlete', 'NOC', 'Medal', 'Edition']]

medal_counts = medals.pivot_table(aggfunc='count', index='Edition', values='Athlete', columns='NOC')

totals = editions.set_index('Edition')
totals = totals['Grand Total']

fractions = medal_counts.divide(totals, axis='rows')

mean_fractions = fractions.expanding().mean()

fractions_change = mean_fractions.pct_change() * 100
fractions_change = fractions_change.reset_index()

# ---

# Reshape fractions_change: reshaped
reshaped = pd.melt(fractions_change, id_vars='Edition', value_name='Change')

# Print reshaped.shape and fractions_change.shape
print(reshaped.shape, fractions_change.shape)

# Extract rows from reshaped where 'NOC' == 'CHN': chn
chn = reshaped.loc[reshaped.NOC == 'CHN']

# Print last 5 rows of chn with .tail()
print(chn.tail())

'''
> reshaped.shape, fractions_change.shape
(3588, 3) (26, 139)

> chn.tail()
     Edition  NOC     Change
567     1992  CHN   4.240630
568     1996  CHN   7.860247
569     2000  CHN  -3.851278
570     2004  CHN   0.128863
571     2008  CHN  13.251332
'''