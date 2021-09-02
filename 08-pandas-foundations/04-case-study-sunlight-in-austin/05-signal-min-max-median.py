'''
Signal min, max, median

Now that you have the data read and cleaned, you can begin with statistical EDA. First, you will analyze the 2011 Austin weather data.

Your job in this exercise is to analyze the 'dry_bulb_faren' column and print the median temperatures for specific time ranges. You can do this using partial datetime string selection.

The cleaned dataframe is provided in the workspace as df_clean.

INSTRUCTIONS

*   Select the 'dry_bulb_faren' column and print the output of .median().
*   Use .loc[] to select the range '2011-Apr':'2011-Jun' from dry_bulb_faren' and print the output of .median().
*   Use .loc[] to select the month '2011-Jan' from 'dry_bulb_faren' and print the output of .median()
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

df_clean['dry_bulb_faren'] = pd.to_numeric(df_clean['dry_bulb_faren'], errors='coerce')
df_clean['wind_speed'] = pd.to_numeric(df_clean['wind_speed'], errors='coerce')
df_clean['dew_point_faren'] = pd.to_numeric(df_clean['dew_point_faren'], errors='coerce')

# ---


# Print the median of the dry_bulb_faren column
print(df_clean['dry_bulb_faren'].median())

# Print the median of the dry_bulb_faren column for the time range '2011-Apr':'2011-Jun'
print(df_clean.loc['2011-Apr':'2011-Jun', 'dry_bulb_faren'].median())

# Print the median of the dry_bulb_faren column for the month of January
print(df_clean.loc['2011-Jan', 'dry_bulb_faren'].median())