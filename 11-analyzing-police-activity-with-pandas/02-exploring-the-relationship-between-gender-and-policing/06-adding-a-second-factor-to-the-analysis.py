'''
Adding a second factor to the analysis

Even though the search rate for males is much higher than for females, it's possible that the difference is mostly due to a second factor.

For example, you might hypothesize that the search rate varies by violation type, and the difference in search rate between males and females is because they tend to commit different violations.

You can test this hypothesis by examining the search rate for each combination of gender and violation. If the hypothesis was true, you would find that males and females are searched at about the same rate for each violation. Find out below if that's the case!
'''

import pandas as pd

ri = pd.read_csv('../datasets/RI_cleaned.csv', nrows=100000, low_memory=False)

ri.drop(['county_name', 'state'], axis='columns', inplace=True)
ri.dropna(subset=['driver_gender'], inplace=True)

ri['is_arrested'] = ri.is_arrested.astype('bool')

combined = ri.stop_date.str.cat(ri.stop_time, sep=' ')
ri['stop_datetime'] = pd.to_datetime(combined)

ri.set_index('stop_datetime', inplace=True)

'''
INSTRUCTIONS 1/2

*   Use a .groupby() to calculate the search rate for each combination of gender and violation. Are males and females searched at about the same rate for each violation?
'''

# Calculate the search rate for each combination of gender and violation
print(ri.groupby(['driver_gender', 'violation']).search_conducted.mean())

'''
INSTRUCTIONS 2/2

*   Reverse the ordering to group by violation before gender. The results may be easier to compare when presented this way.
'''

# Reverse the ordering to group by violation before gender
print(ri.groupby(['violation', 'driver_gender']).search_conducted.mean())

'''
driver_gender  violation
F              Equipment              0.091828
               Moving violation       0.053781
               Other                  0.065957
               Registration/plates    0.119534
               Speeding               0.007380
M              Equipment              0.118743
               Moving violation       0.088704
               Other                  0.146558
               Registration/plates    0.164004
               Speeding               0.027358
Name: search_conducted, dtype: float64

violation            driver_gender
Equipment            F                0.091828
                     M                0.118743
Moving violation     F                0.053781
                     M                0.088704
Other                F                0.065957
                     M                0.146558
Registration/plates  F                0.119534
                     M                0.164004
Speeding             F                0.007380
                     M                0.027358
Name: search_conducted, dtype: float64
'''