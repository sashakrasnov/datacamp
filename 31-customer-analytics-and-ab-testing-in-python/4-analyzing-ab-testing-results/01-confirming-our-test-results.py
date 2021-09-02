'''
Confirming our test results

To begin this chapter, you will confirm that everything ran correctly for an A/B test similar to that shown in the lesson. Like the A/B test in the lesson this one consists of trying to boost consumable sales through making changes to a paywall.

The data from the test is loaded for you as "ab_test_results" and it has already been merged with the relevant demographics data. The checks you will perform will allow you to confidently report any results you uncover.
'''

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

'''
INSTRUCTIONS 1/3

*   As discussed we created our test and control groups by assigning unique users to each. Confirm the size the groups are similar by grouping by group and aggregating to find the number of unique uid in each with the pd.Series.nunique() method.
'''

# Compute and print the results
results = ab_test_results.groupby('group').agg({'uid': pd.Series.nunique}) 
print(results)

'''
INSTRUCTIONS 2/3

*   Now convert this number to the percentage of overall users in each group. This will help in presenting the result and speaking about it precisely. To do this, use the len() function and unique()method to find the number of unique uid in ab_test_results and to then divide by this result.
'''

# Find the unique users in each group 
results = ab_test_results.groupby('group').agg({'uid': pd.Series.nunique}) 

# Find the overall number of unique users using "len" and "unique"
unique_users = len(ab_test_results.uid.unique())

# Find the percentage in each group
results = results / unique_users * 100
print(results)

'''
INSTRUCTIONS 3/3

*   Finally, additionally group by 'device' and 'gender' when finding the number of users in each group. This will let us compute our percentage calculation broken out by 'device' and 'gender' to confirm our result is truly random across cohorts.
'''

# Find the unique users in each group 
results = ab_test_results.groupby(by=['group', 'device', 'gender']).agg({'uid': pd.Series.nunique}) 

# Find the overall number of unique users using "len" and "unique"
unique_users = len(ab_test_results.uid.unique())

# Find the percentage in each group
results = results / unique_users * 100
print(results)

