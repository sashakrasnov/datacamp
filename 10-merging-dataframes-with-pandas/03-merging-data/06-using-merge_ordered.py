'''
Using merge_ordered()

This exercise uses pre-loaded DataFrames austin and houston that contain weather data from the cities Austin and Houston respectively. They have been printed in the IPython Shell for you to examine.

Weather conditions were recorded on separate days and you need to merge these two DataFrames together such that the dates are ordered. To do this, you'll use pd.merge_ordered(). After you're done, note the order of the rows before and after merging.

INSTRUCTIONS

*   Perform an ordered merge on austin and houston using pd.merge_ordered(). Store the result as tx_weather.
*   Print tx_weather. You should notice that the rows are sorted by the date but it is not possible to tell which observation came from which city.
*   Perform another ordered merge on austin and houston.
*   This time, specify the keyword arguments on='date' and suffixes=['_aus','_hus'] so that the rows can be distinguished. Store the result as tx_weather_suff.
*   Print tx_weather_suff to examine its contents. This has been done for you.
*   Perform a third ordered merge on austin and houston.
*   This time, in addition to the on and suffixes parameters, specify the keyword argument fill_method='ffill' to use forward-filling to replace NaN entries with the most recent non-null entry, and hit 'Submit Answer' to examine the contents of the merged DataFrames!
'''

import pandas as pd

austin  = pd.DataFrame({'date': ['2016-01-01','2016-02-08','2016-01-17'],
                        'rating': ['Cloudy','Cloudy','Sunny']})

houston = pd.DataFrame({'date': ['2016-01-04','2016-01-01','2016-03-01'],
                        'rating': ['Rainy','Cloudy','Sunny']})

# ---

# Perform the first ordered merge: tx_weather
tx_weather = pd.merge_ordered(austin, houston)

# Print tx_weather
print(tx_weather)

# Perform the second ordered merge: tx_weather_suff
tx_weather_suff = pd.merge_ordered(austin, houston, on='date', suffixes=['_aus','_hus'])

# Print tx_weather_suff
print(tx_weather_suff)

# Perform the third ordered merge: tx_weather_ffill
tx_weather_ffill = pd.merge_ordered(austin, houston, on='date', suffixes=['_aus','_hus'], fill_method='ffill')

# Print tx_weather_ffill
print(tx_weather_ffill)

'''
> tx_weather
        date ratings
0 2016-01-01  Cloudy
1 2016-01-04   Rainy
2 2016-01-17   Sunny
3 2016-02-08  Cloudy
4 2016-03-01   Sunny

> tx_weather_suff
        date ratings_aus ratings_hus
0 2016-01-01      Cloudy      Cloudy
1 2016-01-04         NaN       Rainy
2 2016-01-17       Sunny         NaN
3 2016-02-08      Cloudy         NaN
4 2016-03-01         NaN       Sunny

> tx_weather_ffill
        date ratings_aus ratings_hus
0 2016-01-01      Cloudy      Cloudy
1 2016-01-04      Cloudy       Rainy
2 2016-01-17       Sunny       Rainy
3 2016-02-08      Cloudy       Rainy
4 2016-03-01      Cloudy       Sunny
'''