'''
Creating DateTime Objects... Now

Often when working with datetime objects, you'll want to work on windows or ranges that start from the current date and time. You can do this using the datetime now functions. There is a .now() method on the datetime object in the datetime module and a .utcnow() method. The .now() method returns the current local time on the machine on which it is run, and .utcnow() does the same thing but returns the value in UTC time. You'll need to be very familiar with these methods.

No dataset is used in this exercise, but bear with us as you'll need to do this often to compare year/month-to-date etc.

INSTRUCTIONS

*   Import datetime from the datetime module.
*   Store the local datetime as local_dt and print it.
*   Store the UTC datetime as utc_dt and print it.
'''

# Import datetime from the datetime module
from datetime import datetime

# Compute the local datetime: local_dt
local_dt = datetime.now()

# Print the local datetime
print(local_dt)

# Compute the UTC datetime: utc_dt
utc_dt = datetime.utcnow()

# Print the UTC datetime
print(utc_dt)