'''
Signal variance

You're now ready to compare the 2011 weather data with the 30-year normals reported in 2010. You can ask questions such as, on average, how much hotter was every day in 2011 than expected from the 30-year average?

The DataFrames df_clean and df_climate from previous exercises are available in the workspace.

Your job is to first resample df_clean and df_climate by day and aggregate the mean temperatures. You will then extract the temperature related columns from each - 'dry_bulb_faren' in df_clean, and 'Temperature' in df_climate - as NumPy arrays and compute the difference.

Notice that the indexes of df_clean and df_climate are not aligned - df_clean has dates in 2011, while df_climate has dates in 2010. This is why you extract the temperature columns as NumPy arrays. An alternative approach is to use the pandas .reset_index() method to make sure the Series align properly. You will practice this approach as well.
'''

import pandas as pd

df = pd.read_csv('../datasets/NOAA_QCLCD_2011_hourly_13904.txt', header=None)

list_to_drop = [
    'sky_conditionFlag',
    'visibilityFlag',
    'wx_and_obst_to_vision',
    'wx_and_obst_to_visionFlag',
    'dry_bulb_farenFlag',
    'dry_bulb_celFlag',
    'wet_bulb_farenFlag',
    'wet_bulb_celFlag',
    'dew_point_farenFlag',
    'dew_point_celFlag',
    'relative_humidityFlag',
    'wind_speedFlag',
    'wind_directionFlag',
    'value_for_wind_character',
    'value_for_wind_characterFlag',
    'station_pressureFlag',
    'pressure_tendencyFlag',
    'pressure_tendency',
    'presschange',
    'presschangeFlag',
    'sea_level_pressureFlag',
    'hourly_precip',
    'hourly_precipFlag',
    'altimeter',
    'record_type',
    'altimeterFlag',
    'junk'
]

column_labels =  'Wban,date,Time,StationType,sky_condition,sky_conditionFlag,visibility,visibilityFlag,wx_and_obst_to_vision,wx_and_obst_to_visionFlag,dry_bulb_faren,dry_bulb_farenFlag,dry_bulb_cel,dry_bulb_celFlag,wet_bulb_faren,wet_bulb_farenFlag,wet_bulb_cel,wet_bulb_celFlag,dew_point_faren,dew_point_farenFlag,dew_point_cel,dew_point_celFlag,relative_humidity,relative_humidityFlag,wind_speed,wind_speedFlag,wind_direction,wind_directionFlag,value_for_wind_character,value_for_wind_characterFlag,station_pressure,station_pressureFlag,pressure_tendency,pressure_tendencyFlag,presschange,presschangeFlag,sea_level_pressure,sea_level_pressureFlag,record_type,hourly_precip,hourly_precipFlag,altimeter,altimeterFlag,junk'

column_labels_list = column_labels.split(',')

df.columns = column_labels_list

df_dropped = df.drop(list_to_drop, axis='columns')

df_dropped['date'] = df_dropped['date'].astype(str)
df_dropped['Time'] = df_dropped['Time'].apply(lambda x:'{:0>4}'.format(x))

date_string = df_dropped['date'] + df_dropped['Time']
date_times = pd.to_datetime(date_string, format='%Y%m%d%H%M')

df_clean = df_dropped.set_index(date_times)

df_clean['dry_bulb_faren'] = pd.to_numeric(df_clean['dry_bulb_faren'], errors='coerce')
df_clean['wind_speed'] = pd.to_numeric(df_clean['wind_speed'], errors='coerce')
df_clean['dew_point_faren'] = pd.to_numeric(df_clean['dew_point_faren'], errors='coerce')

df_climate = pd.read_csv('../datasets/weather_data_austin_2010.csv', parse_dates=['Date'], index_col='Date')

'''
INSTRUCTIONS

*   Downsample df_clean with daily frequency and aggregate by the mean. Store the result as daily_mean_2011.
*   Extract the 'dry_bulb_faren' column from daily_mean_2011 as a NumPy array using .values. Store the result as daily_temp_2011. Note: .values is an attribute, not a method, so you don't have to use ().
*   Downsample df_climate with daily frequency and aggregate by the mean. Store the result as daily_climate.
*   Extract the 'Temperature' column from daily_climate using the .reset_index() method. To do this, first reset the index of daily_climate, and then use bracket slicing to access 'Temperature'. Store the result as daily_temp_climate.
'''

# Downsample df_clean by day and aggregate by mean: daily_mean_2011
daily_mean_2011 = df_clean.resample('D').mean()

# Extract the dry_bulb_faren column from daily_mean_2011 using .values: daily_temp_2011
daily_temp_2011 = daily_mean_2011['dry_bulb_faren'].values

# Downsample df_climate by day and aggregate by mean: daily_climate
daily_climate = df_climate.resample('D').mean()

# Extract the Temperature column from daily_climate using .reset_index(): daily_temp_climate
daily_temp_climate = daily_climate.reset_index()['Temperature (deg F)']

# Compute the difference between the two arrays and print the mean difference
difference = daily_temp_2011 - daily_temp_climate

print(difference.mean())
