'''
Detecting outliers with Z-Scores

As Dhavide demonstrated in the video using the zscore function, you can apply a .transform() method after grouping to apply a function to groups of data independently. The z-score is also useful to find outliers: a z-score value of +/- 3 is generally considered to be an outlier.

In this example, you're going to normalize the Gapminder data in 2010 for life expectancy and fertility by the z-score per region. Using boolean indexing, you will filter out countries that have high fertility rates and low life expectancy for their region.

The Gapminder DataFrame for 2010 indexed by 'Country' is provided for you as gapminder_2010.

INSTRUCTIONS

*   Import zscore from scipy.stats.
*   Group gapminder_2010 by 'region' and transform the ['life','fertility'] columns by zscore.
*   Construct a boolean Series of the bitwise or between standardized['life'] < -3 and standardized['fertility'] > 3.
*   Filter gapminder_2010 using .loc[] and the outliers Boolean Series. Save the result as gm_outliers.
*   Print gm_outliers. This has been done for you, so hit 'Submit Answer' to see the results.
'''

import pandas as pd

gapminder = pd.read_csv('../datasets/gapminder_tidy.csv', index_col=['Year', 'Country'])

gapminder_2010 = gapminder.loc[2010]

# ---

# Import zscore
from scipy.stats import zscore

# Group gapminder_2010: standardized
standardized = gapminder_2010.groupby('region')[['life','fertility']].transform(zscore)

# Construct a Boolean Series to identify outliers: outliers
outliers = (standardized['life'] < -3) | (standardized['fertility'] > 3)

# Filter gapminder_2010 by the outliers: gm_outliers
gm_outliers = gapminder_2010.loc[outliers]

# Print gm_outliers
print(gm_outliers)

'''
> gapminder.info()
<class 'pandas.core.frame.DataFrame'>
MultiIndex: 10111 entries, (1964, Afghanistan) to (2006, Åland)
Data columns (total 6 columns):
fertility          10100 non-null float64
life               10111 non-null float64
population         10108 non-null float64
child_mortality    9210 non-null float64
gdp                9000 non-null float64
region             10111 non-null object
dtypes: float64(5), object(1)
memory usage: 508.2+ KB

> gapminder_2010.info()
<class 'pandas.core.frame.DataFrame'>
Index: 202 entries, Afghanistan to Zimbabwe
Data columns (total 6 columns):
fertility          202 non-null float64
life               202 non-null float64
population         202 non-null float64
child_mortality    189 non-null float64
gdp                180 non-null float64
region             202 non-null object
dtypes: float64(5), object(1)
memory usage: 11.0+ KB

> gm_outliers
             fertility    life  population  child_mortality     gdp                 region
Country                                                                                   
Guatemala        3.974  71.100  14388929.0             34.5  6849.0                America
Haiti            3.350  45.000   9993247.0            208.8  1518.0                America
Tajikistan       3.780  66.830   6878637.0             52.6  2110.0  Europe & Central Asia
Timor-Leste      6.237  65.952   1124355.0             63.8  1777.0    East Asia & Pacific
'''