'''
Finding a time in the future and from the past

Another common case when working with times is to get a date 30, 60, or 90 days in the past from some date. In Python, the timedelta object from the datetime module is used to represent differences in datetime objects. You can create a timedelta by passing any number of keyword arguments such as days, seconds, microseconds, milliseconds, minutes, hours, and weeks to timedelta().

Once you have a timedelta object, you can add or subtract it from a datetime object to get a datetime object relative to the original datetime object.

A dictionary, daily_summaries, has been supplied for you. It contains the datetime as the key with a dict as the value that has 'day_type' and 'total_ridership' keys. A list of datetimes to review called review_dates is also available.
'''

import csv

from datetime import datetime

review_dates = [datetime(2013, 12, d) for d in range(22,32)]

with open('../datasets/cta_daily_summary_totals.csv' ,'r') as csvfile:
    daily_summaries = {datetime.strptime(row['service_date'], '%m/%d/%Y'):{'day_type': row['day_type'], 'total_ridership': row['total_rides']} for row in csv.DictReader(csvfile)}

'''
INSTRUCTIONS

*   Import timedelta from the datetime module.
*   Build a timedelta of 30 days called glanceback using timedelta().
*   Iterate over the review_dates, using date as your iterator variable.
    *   Calculate the date 30 days back by subtracting glanceback from date.
    *   Print the date, along with 'day_type' and 'total_ridership' from daily_summaries for that date.
    *   Print the prior_period_dt, along with 'day_type' and 'total_ridership' from daily_summaries for that date (prior_period_dt).
'''

# Import timedelta from the datetime module
from datetime import timedelta

# Build a timedelta of 30 days: glanceback
glanceback = timedelta(days=30)

# Iterate over the review_dates as date
for date in review_dates:
    # Calculate the date 30 days back: prior_period_dt
    prior_period_dt = date - glanceback
    
    # Print the review_date, day_type and total_ridership
    print('Date: %s, Type: %s, Total Ridership: %s' %
         (date, 
          daily_summaries[date]['day_type'], 
          daily_summaries[date]['total_ridership']))

    # Print the prior_period_dt, day_type and total_ridership
    print('Date: %s, Type: %s, Total Ridership: %s' %
         (prior_period_dt, 
          daily_summaries[prior_period_dt]['day_type'], 
          daily_summaries[prior_period_dt]['total_ridership']))