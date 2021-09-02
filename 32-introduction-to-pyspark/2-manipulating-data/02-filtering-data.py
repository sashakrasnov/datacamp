'''
Now that you have a bit of SQL know-how under your belt, it's easier to talk about the analogous operations using Spark DataFrames.

Let's take a look at the .filter() method. As you might suspect, this is the Spark counterpart of SQL's WHERE clause. The .filter() method takes either a Spark Column of boolean (True/False) values or the WHERE clause of a SQL expression as a string.

For example, the following two expressions will produce the same output:

flights.filter(flights.air_time > 120).show()
flights.filter("air_time > 120").show()
Remember, a SparkSession called spark is already in your workspace, along with the Spark DataFrame flights.

INSTRUCTIONS
100 XP
Use the .filter() method to find all the flights that flew over 1000 miles two ways:
First, pass a SQL string to .filter() that checks the distance is greater than 1000. Save this as long_flights1.
Then pass a boolean column to .filter() that checks the same thing. Save this as long_flights2.
Print the .show() of both DataFrames and make sure they're actually equal!
'''

# Filter flights with a SQL string
long_flights1 = flights.filter('distance > 1000')

# Filter flights with a boolean column
long_flights2 = flights.filter(flights.distance > 1000)

# Examine the data to check they're equal
print(long_flights1.show())
print(long_flights2.show())