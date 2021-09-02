'''
Parsing dates

In this exercise you will practice parsing dates in Python. While often data pulled from a database will be correctly formatted, other data sources can be less nice. Knowing how to properly parse dates is crucial to get the data in a workable format. For reference refer to http://strftime.org/ throughout this exercise to see date format to use.
'''

import pandas as pd

date_data_one = ['Saturday January 27, 2017', 'Saturday December 2, 2017']
date_data_two = ['2017-01-01', '2016-05-03']
date_data_three = ['08/17/1978', '01/07/1976']
date_data_four = ['2016 March 01 01:56', '2016 January 4 02:16']

'''
INSTRUCTIONS 1/4

*   Provide the correct format for the following date:

Saturday January 27, 2017
'''

# Provide the correct format for the date
date_data_one = pd.to_datetime(date_data_one, format='%A %B %d, %Y')
print(date_data_one)

'''
INSTRUCTIONS 2/4

*   Provide the correct format for the following date:

Saturday January 27, 2017
'''

# Provide the correct format for the date
date_data_two = pd.to_datetime(date_data_two, format='%Y-%m-%d')
print(date_data_two)

'''
INSTRUCTIONS 3/4

*   Provide the correct format for the following date.

08/17/1978
'''

# Provide the correct format for the date
date_data_three = pd.to_datetime(date_data_three, format='%m/%d/%Y')
print(date_data_three)

'''
INSTRUCTIONS 4/4

*   Provide the correct format for the following date:

2016 March 01 01:56
'''

# Provide the correct format for the date
date_data_four = pd.to_datetime(date_data_four, format='%Y %B %d %H:%M')
print(date_data_four)
