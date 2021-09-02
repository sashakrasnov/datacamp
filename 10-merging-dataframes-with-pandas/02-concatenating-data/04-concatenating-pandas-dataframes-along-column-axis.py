'''
Concatenating pandas DataFrames along column axis

The function pd.concat() can concatenate DataFrames horizontally as well as vertically (vertical is the default). To make the DataFrames stack horizontally, you have to specify the keyword argument axis=1 or axis='columns'.

In this exercise, you'll use weather data with maximum and mean daily temperatures sampled at different rates (quarterly versus monthly). You'll concatenate the rows of both and see that, where rows are missing in the coarser DataFrame, null values are inserted in the concatenated DataFrame. This corresponds to an outer join (which you will explore in more detail in later exercises).

The files 'quarterly_max_temp.csv' and 'monthly_mean_temp.csv' have been pre-loaded into the DataFrames weather_max and weather_mean respectively, and pandas has been imported as pd.

INSTRUCTIONS

*   Create a new DataFrame called weather by concatenating the DataFrames weather_max and weather_mean horizontally.
*   Pass the DataFrames to pd.concat() as a list and specify the keyword argument axis=1 to stack them horizontally.
*   Print the new DataFrame weather.
'''

import pandas as pd

weather_max = pd.DataFrame({'Max TemperatureF': [68, 89, 91, 84]}, index=['Jan', 'Apr', 'Jul', 'Oct'])
weather_mean = pd.DataFrame({'Mean TemperatureF': [53.100000, 70.000000, 34.935484, 28.714286, 32.354839, 72.870968, 70.133333, 35.000000, 62.612903, 39.800000, 55.451613, 63.766667]}, index=['Apr', 'Aug', 'Dec', 'Feb', 'Jan', 'Jul', 'Jun', 'Mar', 'May', 'Nov', 'Oct', 'Sep'])

weather_max.index.name = weather_mean.index.name = 'Month'

# ---

# Concatenate weather_max and weather_mean horizontally: weather
weather = pd.concat([weather_max, weather_mean], axis=1)

# Print weather
print(weather)

'''
> weather
     Max TemperatureF  Mean TemperatureF
Apr              89.0          53.100000
Aug               NaN          70.000000
Dec               NaN          34.935484
Feb               NaN          28.714286
Jan              68.0          32.354839
Jul              91.0          72.870968
Jun               NaN          70.133333
Mar               NaN          35.000000
May               NaN          62.612903
Nov               NaN          39.800000
Oct              84.0          55.451613
Sep               NaN          63.766667
'''