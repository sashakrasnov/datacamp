'''
In PySpark, joins are performed using the DataFrame method .join(). This method takes three arguments. The first is the second DataFrame that you want to join with the first one. The second argument, on, is the name of the key column(s) as a string. The names of the key column(s) must be the same in each table. The third argument, how, specifies the kind of join to perform. In this course we'll always use the value how="leftouter".

The flights dataset and a new dataset called airports are already in your workspace.

INSTRUCTIONS
100 XP
Examine the airports DataFrame by printing the .show(). Note which key column will let you join airports to the flights table.
Rename the faa column in airports to dest by re-assigning the result of airports.withColumnRenamed("faa", "dest") to airports.
Join the airports DataFrame to the flights DataFrame on the dest column by calling the .join() method on flights. Save the result as flights_with_airports.
The first argument should be the other DataFrame, airports.
The argument on should be the key column.
The argument how should be "leftouter".
Print the .show() of flights_with_airports. Note the new information that has been added.
'''

# Examine the data
print(airports.show())

# Rename the faa column
airports = airports.withColumnRenamed("faa", "dest")

# Join the DataFrames
flights_with_airports = flights.join(airports, on='dest', how="leftouter")

# Examine the data again
print(flights_with_airports.show())