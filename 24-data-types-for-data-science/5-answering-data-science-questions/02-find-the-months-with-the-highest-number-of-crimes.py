'''
Find the Months with the Highest Number of Crimes

Using the crime_data list from the prior exercise, you'll answer a common question that arises when dealing with crime data: How many crimes are committed each month?

Feel free to use the IPython Shell to explore the crime_data list - it has been pre-loaded for you. For example, crime_data[0][0] will show you the first column of the first row which, in this case, is the date and time time that the crime occurred.
'''

import csv

csvfile = open('../datasets/crime_sampler.csv', 'r')

crime_data = []

for row in csv.reader(csvfile):
    crime_data.append(row)
    
crime_data.pop(0)

'''
INSTRUCTIONS

*   Import Counter from collections and datetime from datetime.
*   Create a Counter object called crimes_by_month.
*   Loop over the crime_data list:
    *   Using the datetime.strptime() function, convert the first element of each item into a Python Datetime Object called date.
    *   Increment the counter for the month associated with this row by one. You can access the month of date using date.month.
*   Print the 3 most common months for crime.
'''

# Import necessary modules
from collections import Counter
from datetime import datetime

# Create a Counter Object: crimes_by_month
crimes_by_month = Counter()

# Loop over the crime_data list
for crime in crime_data:
    
    # Convert the first element of each item into a Python Datetime Object: date
    date = datetime.strptime(crime[0], '%m/%d/%Y %I:%M:%S %p')
    
    # Increment the counter for the month of the row by one
    crimes_by_month[date.month] += 1
    
# Print the 3 most common months for crime
print(crimes_by_month.most_common(3))