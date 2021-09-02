'''
Timezones

In order to work effectively with other timezones, you can use the pytz library. To use timezones, you need to import the timezone object from the pytz module. Then you can use the timezone constructor and pass it a name of a timezone, such as CT = timezone('US/Central'). You can get a full list of timezone names at Wikipedia. In Python 3, you can make a datetime object "aware" by passing a timezone as the tzinfo keyword argument to the .replace() method on a datetime instance.

An "aware" datetime object has an .astimezone() method that accepts a timezone object and returns a new datetime object in the desired timezone. If the tzinfo is not set for the datetime object it assumes the timezone of the computer you are working on.

A list, daily_summaries, has been supplied for you it contains the datetime and rail ridership for trains going to New York. You need to determine the time in New York so you can align it with the New York Transit Authority data.
'''

import csv

from datetime import datetime
from pytz import timezone
from random import randint

with open('../datasets/cta_daily_summary_totals.csv' ,'r') as csvfile:
    daily_summaries = [(datetime.strptime(row['service_date'], '%m/%d/%Y').replace(hour=randint(0,23), minute=randint(0,59)), row['rail_boardings']) for row in csv.DictReader(csvfile)]

'''
INSTRUCTIONS

*   Create a Timezone object for Chicago ('US/Central') called chicago_usa_tz.
*   Create a Timezone object for New York ('US/Eastern') called ny_usa_tz.
*   Iterate over the daily_summaries, unpacking it into the variables orig_dt and ridership.
    *   Make the orig_dt timezone "aware" for Chicago, using chicago_usa_tz. Store the result in chicago_dt.
    *   Convert chicago_dt to the New York timezone, ny_dt.
    *   Print the chicago_dt, ny_dt, and ridership.
'''

# Create a Timezone object for Chicago
chicago_usa_tz = timezone('US/Central')

# Create a Timezone object for New York
ny_usa_tz = timezone('US/Eastern')

# Iterate over the daily_summaries list
for orig_dt, ridership in daily_summaries:

    # Make the orig_dt timezone "aware" for Chicago
    chicago_dt = orig_dt.replace(tzinfo=chicago_usa_tz)
    
    # Convert chicago_dt to the New York Timezone
    ny_dt = chicago_dt.astimezone(ny_usa_tz)
    
    # Print the chicago_dt, ny_dt, and ridership
    print('Chicago: %s, NY: %s, Ridership: %s' % (chicago_dt, ny_dt, ridership))