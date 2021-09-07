'''
Comparing drug and search rates

As you saw in the last exercise, the rate of drug-related stops increased significantly between 2005 and 2015. You might hypothesize that the rate of vehicle searches was also increasing, which would have led to an increase in drug-related stops even if more drivers were not carrying drugs.

You can test this hypothesis by calculating the annual search rate, and then plotting it against the annual drug rate. If the hypothesis is true, then you'll see both rates increasing over time.
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

#annual_drug_rate = ri.drugs_related_stop.resample('A').mean()
annual_drug_rate = ri.drugs_related_stop.dropna().astype('int').resample('A').mean()

'''
INSTRUCTIONS

*   Calculate the annual search rate by resampling the search_conducted column, and save the result as annual_search_rate.
*   Concatenate annual_drug_rate and annual_search_rate along the columns axis, and save the result as annual.
*   Create subplots of the drug and search rates from the annual DataFrame.
*   Display the subplots.
'''

# Calculate and save the annual search rate
#annual_search_rate = ri.search_conducted.resample('A').mean()
annual_search_rate = ri.search_conducted.dropna().astype('int').resample('A').mean()

# Concatenate 'annual_drug_rate' and 'annual_search_rate'
annual = pd.concat([annual_drug_rate, annual_search_rate], axis='columns')

# Create subplots from 'annual'
annual.plot(subplots=True)

# Display the subplots
plt.show()