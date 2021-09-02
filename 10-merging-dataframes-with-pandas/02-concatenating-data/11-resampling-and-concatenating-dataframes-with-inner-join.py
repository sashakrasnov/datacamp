'''
Resampling & concatenating DataFrames with inner join

In this exercise, you'll compare the historical 10-year GDP (Gross Domestic Product) growth in the US and in China. The data for the US starts in 1947 and is recorded quarterly; by contrast, the data for China starts in 1966 and is recorded annually.

You'll need to use a combination of resampling and an inner join to align the index labels. You'll need an appropriate offset alias for resampling, and the method .resample() must be chained with some kind of aggregation method (.pct_change() and .last() in this case).

pandas has been imported as pd, and the DataFrames china and us have been pre-loaded, with the output of china.head() and us.head() printed in the IPython Shell.

INSTRUCTIONS

*   Make a new DataFrame china_annual by resampling the DataFrame china with .resample('A') (i.e., with annual frequency) and chaining two method calls:
*   Chain .pct_change(10) as an aggregation method to compute the percentage change with an offset of ten years.
*   Chain .dropna() to eliminate rows containing null values.
*   Make a new DataFrame us_annual by resampling the DataFrame us exactly as you resampled china.
*   Concatenate china_annual and us_annual to construct a DataFrame called gdp. Use join='inner' to perform an inner join and use axis=1 to concatenate horizontally.
*   Print the result of resampling gdp every decade (i.e., using .resample('10A')) and aggregating with the method .last(). This has been done for you, so hit 'Submit Answer' to see the result!
'''

import pandas as pd

china = pd.read_csv('../datasets/gdp/gdp_china.csv', parse_dates=True, index_col='Year')
us = pd.read_csv('../datasets/gdp/gdp_usa.csv', parse_dates=True, index_col='DATE')

# ---

# Resample and tidy china: china_annual
china_annual = china.resample('A').mean().pct_change(10).dropna()

# Resample and tidy us: us_annual
us_annual = us.resample('A').mean().pct_change(10).dropna()

# Concatenate china_annual and us_annual: gdp
gdp = pd.concat([china_annual, us_annual], join='inner', axis=1)

# Resample gdp and print
print(gdp.resample('10A').last())

'''
                 GDP     VALUE
Year
1970-12-31  0.546128  0.980397
1980-12-31  1.072537  1.660540
1990-12-31  0.892820  1.088953
2000-12-31  2.357522  0.719980
2010-12-31  4.011081  0.455009
2020-12-31  3.789936  0.377506
'''