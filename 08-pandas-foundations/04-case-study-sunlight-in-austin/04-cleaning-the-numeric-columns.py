'''
Cleaning the numeric columns

The numeric columns contain missing values labeled as 'M'. In this exercise, your job is to transform these columns such that they contain only numeric values and interpret missing data as NaN.

The pandas function pd.to_numeric() is ideal for this purpose: It converts a Series of values to floating-point values. Furthermore, by specifying the keyword argument errors='coerce', you can force strings like 'M' to be interpreted as NaN.

A DataFrame df_clean is provided for you at the start of the exercise, and as usual, pandas has been imported as pd.

INSTRUCTIONS

*   Print the 'dry_bulb_faren' temperature between 8 AM and 9 AM on June 20, 2011.
*   Convert the 'dry_bulb_faren' column to numeric values with pd.to_numeric(). Specify errors='coerce'.
*   Print the transformed dry_bulb_faren temperature between 8 AM and 9 AM on June 20, 2011.
*   Convert the 'wind_speed' and 'dew_point_faren' columns to numeric values with pd.to_numeric(). Again, specify errors='coerce'.
'''

# --- From the previous exercise

import pandas as pd

df = pd.read_csv('../datasets/NOAA_QCLCD_2011_hourly_13904', header=None)

list_to_drop = ['sky_conditionFlag',
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
                'junk']

column_labels =  'Wban,date,Time,StationType,sky_condition,sky_conditionFlag,visibility,visibilityFlag,wx_and_obst_to_vision,wx_and_obst_to_visionFlag,dry_bulb_faren,dry_bulb_farenFlag,dry_bulb_cel,dry_bulb_celFlag,wet_bulb_faren,wet_bulb_farenFlag,wet_bulb_cel,wet_bulb_celFlag,dew_point_faren,dew_point_farenFlag,dew_point_cel,dew_point_celFlag,relative_humidity,relative_humidityFlag,wind_speed,wind_speedFlag,wind_direction,wind_directionFlag,value_for_wind_character,value_for_wind_characterFlag,station_pressure,station_pressureFlag,pressure_tendency,pressure_tendencyFlag,presschange,presschangeFlag,sea_level_pressure,sea_level_pressureFlag,record_type,hourly_precip,hourly_precipFlag,altimeter,altimeterFlag,junk';

column_labels_list = column_labels.split(',')

df.columns = column_labels_list

df_dropped = df.drop(list_to_drop, axis='columns')

df_dropped['date'] = df_dropped['date'].astype(str)
df_dropped['Time'] = df_dropped['Time'].apply(lambda x:'{:0>4}'.format(x))

date_string = df_dropped['date'] + df_dropped['Time']
date_times = pd.to_datetime(date_string, format='%Y%m%d%H%M')

df_clean = df_dropped.set_index(date_times)

# ---


# Print the dry_bulb_faren temperature between 8 AM and 9 AM on June 20, 2011
print(df_clean.loc['2011-6-20 08:00:00':'2011-6-20 09:00:00', 'dry_bulb_faren'])

# Convert the dry_bulb_faren column to numeric values: df_clean['dry_bulb_faren']
df_clean['dry_bulb_faren'] = pd.to_numeric(df_clean['dry_bulb_faren'], errors='coerce')

# Print the transformed dry_bulb_faren temperature between 8 AM and 9 AM on June 20, 2011
print(df_clean.loc['2011-6-20 08:00:00':'2011-6-20 09:00:00','dry_bulb_faren'])

# Convert the wind_speed and dew_point_faren columns to numeric values
df_clean['wind_speed'] = pd.to_numeric(df_clean['wind_speed'], errors='coerce')
df_clean['dew_point_faren'] = pd.to_numeric(df_clean['dew_point_faren'], errors='coerce')