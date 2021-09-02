'''
Create a time series of air quality data

You have seen in the video how to deal with dates that are not in the correct format, but instead are provided as string types, represented as dtype object in pandas.

We have prepared a data set with air quality data (ozone, pm25, and carbon monoxide for NYC, 2000-2017) for you to practice the use of pd.to_datetime().
'''

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../datasets/air_quality_data/nyc.csv')

'''
INSTRUCTIONS

We have already imported pandas as pd and matplotlib.pyplot as plt for you, and loaded the air quality DataFrame into the variable data.

*   Inspect data using .info().
*   Use pd.to_datetime to convert the column 'date' to dtype datetime64.
*   Set the 'date' column as index.
*   Validate the changes by inspecting data using .info() again.
*   Plot data using subplots=True.
'''

# Inspect data
print(data.info())

# Convert the date column to datetime64
data['date'] = pd.to_datetime(data.date)

# Set date column as index
data.set_index('date', inplace=True)

# Inspect data 
print(data.info())

# Plot data
data.plot(subplots=True)
plt.show()
