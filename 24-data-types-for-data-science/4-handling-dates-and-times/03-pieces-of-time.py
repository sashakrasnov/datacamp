'''
Pieces of Time

When working with datetime objects, you'll often want to group them by some component of the datetime such as the month, year, day, etc. Each of these are available as attributes on an instance of a datetime object.

You're going to work with the summary of the CTA's daily ridership. It contains the following columns, in order: service_date, day_type, bus, rail_boardings, and total_rides. The modules defaultdict and datetime have already been imported for you.
'''

import csv

from datetime import datetime
from collections import defaultdict

with open('../datasets/cta_daily_summary_totals.csv' ,'r') as csvfile:
    daily_summaries = [tuple(row.values()) for row in csv.DictReader(csvfile)]

'''
INSTRUCTIONS

*   Create a defaultdict of an integer called monthly_total_rides.
*   Loop over the list daily_summaries, which contains the columns mentioned above in the assignment text.
    *   Convert the service_date (1st element of daily_summary) to a datetime object called service_datetime. Use '%m/%d/%Y' as your format string.
    *   Use the month of the service_datetime as the dict key and add the total_rides (5th element of daily_summary) to the current amount for the month. Be sure to convert this into an integer.
*   Print monthly_total_rides.
'''

# Create a defaultdict of an integer: monthly_total_rides
monthly_total_rides = defaultdict(int)

# Loop over the list daily_summaries
for daily_summary in daily_summaries:
    # Convert the service_date to a datetime object
    service_datetime = datetime.strptime(daily_summary[0], '%m/%d/%Y')

    # Add the total rides to the current amount for the month
    monthly_total_rides[service_datetime.month] += int(daily_summary[4])

# Print monthly_total_rides
print(monthly_total_rides)