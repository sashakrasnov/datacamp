'''
Plotting stop length

If you were stopped for a particular violation, how long might you expect to be detained?

In this exercise, you'll visualize the average length of time drivers are stopped for each type of violation. Rather than using the violation column in this exercise, you'll use violation_raw since it contains more detailed descriptions of the violations.
'''
import pandas as pd
import matplotlib.pyplot as plt

ri = pd.read_csv('../datasets/RI_cleaned.csv', low_memory=False)

ri.drop(['county_name', 'state'], axis='columns', inplace=True)
ri.dropna(subset=['driver_gender'], inplace=True)

ri['is_arrested'] = ri.is_arrested.astype('bool')

combined = ri.stop_date.str.cat(ri.stop_time, sep=' ')
ri['stop_datetime'] = pd.to_datetime(combined)

ri.set_index('stop_datetime', inplace=True)

ri.loc[(ri['stop_duration']=='1') | (ri['stop_duration']=='2'), 'stop_duration'] = '0-15 Min'

mapping = {'0-15 Min': 8, '16-30 Min':23, '30+ Min': 45}

ri['stop_minutes'] = ri.stop_duration.map(mapping)

'''
INSTRUCTIONS

*   For each value in the violation_raw column, calculate the mean number of stop_minutes that a driver is detained.
*   Save the resulting Series as a new object, stop_length.
*   Sort stop_length by its values, and then visualize it using a horizontal bar plot.
*   Display the plot.
'''

# Calculate the mean 'stop_minutes' for each value in 'violation_raw'
print(ri.groupby('violation_raw').stop_minutes.mean())

# Save the resulting Series as 'stop_length'
stop_length = ri.groupby('violation_raw').stop_minutes.mean()

# Sort 'stop_length' by its values and create a horizontal bar plot
stop_length.sort_values().plot(kind='barh')

# Display the plot
plt.show()