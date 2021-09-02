'''
Re-assigning column names

After the initial step of reading in the data, the next step is to clean and tidy it so that it is easier to work with.

In this exercise, you will begin this cleaning process by re-assigning column names and dropping unnecessary columns.

pandas has been imported in the workspace as pd, and the file NOAA_QCLCD_2011_hourly_13904.txt has been parsed and loaded into a DataFrame df. The comma separated string of column names, column_labels, and list of columns to drop, list_to_drop, have also been loaded for you.

INSTRUCTIONS

*   Convert the comma separated string column_labels to a list of strings using .split(','). Assign the result to column_labels_list.
*   Reassign df.columns using the list of strings column_labels_list.
*   Call df.drop() with list_to_drop and axis='columns'. Assign the result to df_dropped.
*   Print df_dropped.head() to examine the result. This has already been done for you.
'''

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


# Split on the comma to create a list: column_labels_list
column_labels_list = column_labels.split(',')

# Assign the new column labels to the DataFrame: df.columns
df.columns = column_labels_list

# Remove the appropriate columns: df_dropped
df_dropped = df.drop(list_to_drop, axis='columns')

# Print the output of df_dropped.head()
print(df_dropped.head())
