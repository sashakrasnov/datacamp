'''
Humanizing Differences with Pendulum

Pendulum provides a powerful way to convert strings to pendulum datetime objects via the .parse() method. Just pass it a date string and it will attempt to convert into a valid pendulum datetime. By default, .parse() can process dates in ISO 8601 format. To allow it to parse other date formats, pass strict = False.

It also has a wonderful alternative to timedelta. When calculating the difference between two dates by subtraction, pendulum provides methods such as .in_days() to output the difference in a chosen metric. These are just the beginning of what pendulum can do for you.

A list of tuples called date_ranges is provided for you. This is the same list of tuples that contain two dates that was used a few exercises prior. You'll be focusing on comparing ranges of records.

You can learn more in the pendulum documentation. Here, it has been imported for you.
'''

import csv
import pendulum

slice = 30

with open('../datasets/cta_daily_summary_totals.csv' ,'r') as csvfile:
    daily_summaries = [row['service_date'] for row in csv.DictReader(csvfile)][slice-1::slice]

date_ranges = zip(daily_summaries[0::2], daily_summaries[1::2])

'''
INSTRUCTIONS

*   Iterate over the date_ranges list, unpacking it into start_date and end_date. These dates are not in ISO 8601 format.
*   Use pendulum to convert the start_date string to a pendulum date called start_dt.
*   Use pendulum to convert the end_date string to pendulum date called end_dt.
*   Calculate the difference between end_dt and start_dt. Store the result as diff_period.
*   Print the difference in days, using the .in_days() method.
'''

# Iterate over date_ranges
for start_date, end_date in date_ranges:

    # Convert the start_date string to a pendulum date: start_dt 
    start_dt = pendulum.parse(start_date, strict=False)
    
    # Convert the end_date string to a pendulum date: end_dt 
    end_dt = pendulum.parse(end_date, strict=False)
    
    # Print the End and Start Date
    print(end_dt, start_dt)
    
    # Calculate the difference between end_dt and start_dt: diff_period
    diff_period = end_dt - start_dt
    
    # Print the difference in days
    print(diff_period.in_days())