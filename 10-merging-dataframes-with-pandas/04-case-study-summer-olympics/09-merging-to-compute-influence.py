'''
Merging to compute influence

This exercise starts off with the DataFrames reshaped and hosts in the namespace.

Your task is to merge the two DataFrames and tidy the result.

The end result is a DataFrame summarizing the fractional change in the expanding mean of the percentage of medals won for the host country in each Olympic edition.

INSTRUCTIONS
100XP
Merge reshaped and hosts using an inner join. Remember, how='inner' is the default behavior for pd.merge().
Print the first 5 rows of the DataFrame merged. This has been done for you. You should see that the rows are jumbled chronologically.
Set the index of merged to be 'Edition' and sort the index.
Print the first 5 rows of the DataFrame influence. This has been done for you, so hit 'Submit Answer' to see the results!
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

# ---

# Merge reshaped and hosts: merged
merged = pd.merge(reshaped, hosts, how='inner')

# Print first 5 rows of merged
print(merged.head())

# Set Index of merged and sort it: influence
influence = merged.set_index('Edition').sort_index()

# Print first 5 rows of influence
print(influence.head())

'''
> merged.head()
   Edition  NOC     Change
0     1956  AUS  54.615063
1     2000  AUS  12.554986
2     1920  BEL  54.757887
3     1976  CAN  -2.143977
4     2008  CHN  13.251332

> influence.head()
         NOC      Change
Edition
1896     GRE         NaN
1900     FRA  198.002486
1904     USA  199.651245
1908     GBR  134.489218
1912     SWE   71.896226
'''