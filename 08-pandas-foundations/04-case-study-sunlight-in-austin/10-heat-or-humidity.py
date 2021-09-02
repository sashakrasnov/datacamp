'''
Heat or humidity

Dew point is a measure of relative humidity based on pressure and temperature. A dew point above 65 is considered uncomfortable while a temperature above 90 is also considered uncomfortable.

In this exercise, you will explore the maximum temperature and dew point of each month. The columns of interest are 'dew_point_faren' and 'dry_bulb_faren'. After resampling them appropriately to get the maximum temperature and dew point in each month, generate a histogram of these values as subplots. Uncomfortably, you will notice that the maximum dew point is above 65 every month!

df_clean has been pre-loaded for you.

INSTRUCTIONS

*   Select the 'dew_point_faren' and 'dry_bulb_faren' columns (in that order). Resample by month and aggregate the maximum monthly temperatures. Assign the result to monthly_max.
*   Plot a histogram of the resampled data with bins=8, alpha=0.5, and subplots=True.
'''

# --- From the previous exercises

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


# Resample dew_point_faren and dry_bulb_faren by Month, aggregating the maximum values: monthly_max
monthly_max = df_clean[['dew_point_faren', 'dry_bulb_faren']].resample('M').max()

# Generate a histogram with bins=8, alpha=0.5, subplots=True
monthly_max.plot(kind='hist', bins=8, alpha=0.5, subplots=True)

# Show the plot
plt.show()