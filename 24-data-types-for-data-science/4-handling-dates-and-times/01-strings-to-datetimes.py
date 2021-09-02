'''
Strings to DateTimes

Time to begin your DateTime journey! You'll start by using the .strptime() method from the datetime object as shown in the video, passing it both the string and the format. A full list of the format string components is available in the Python documentation.

You'll be using the datetime column from the Chicago Transist Authority data, which is available as dates_list. Feel free to explore it in the IPython Shell: You'll see that it has the format of Month, Day, Year.
'''

import csv

with open('../datasets/cta_daily_summary_totals.csv' ,'r') as csvfile:
    dates_list = [row['service_date'] for row in csv.DictReader(csvfile)]

'''
INSTRUCTIONS

*   Import the datetime object from datetime.
*   Iterate over the dates_list, using date_str as your iterator variable.
*   Convert each date_str into a datetime object called date_dt using the datetime.strptime() function, with '%m/%d/%Y' as your format.
*   Print each date_dt.
'''

# Import the datetime object from datetime
from datetime import datetime

# Iterate over the dates_list 
for date_str in dates_list:
    # Convert each date to a datetime object: date_dt
    date_dt = datetime.strptime(date_str, '%m/%d/%Y')
    
    # Print each date_dt
    print(date_dt)