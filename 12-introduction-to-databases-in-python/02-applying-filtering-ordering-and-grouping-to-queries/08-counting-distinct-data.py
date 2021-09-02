'''
Counting Distinct Data

As mentioned in the video, SQLAlchemy's func module provides access to built-in SQL functions that can make operations like counting and summing faster and more efficient.

In the video, Jason used func.sum() to get a sum of the pop2008 column of census as shown below:

|   select([func.sum(census.columns.pop2008)])

If instead you want to count the number of values in pop2008, you could use func.count() like this:

|   select([func.count(census.columns.pop2008)])

Furthermore, if you only want to count the distinct values of pop2008, you can use the .distinct() method:

|   select([func.count(census.columns.pop2008.distinct())])

In this exercise, you will practice using func.count() and .distinct() to get a count of the distinct number of states in census.

So far, you've seen .fetchall() and .first() used on a ResultProxy to get the results. The ResultProxy also has a method called .scalar() for getting just the value of a query that returns only one row and column.

This can be very useful when you are querying for just a count or sum.
'''

from sqlalchemy import create_engine, select, func, MetaData, Table

# DataCamp PostgreSQL on AWS does not acceppt remote connections. Permission denied
# Local MySQL or SQLite may be used instead
#engine = create_engine('postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')
engine = create_engine('mysql://root:@localhost:3306/circle')
#engine = create_engine('sqlite:///../datasets/census.sqlite')

connection = engine.connect()

metadata = MetaData()

census = Table('census', metadata, autoload=True, autoload_with=engine)

'''
INSTRUCTIONS

*   Build a select statement to count the distinct values in the state field of census.
*   Execute stmt to get the count and store the results as distinct_state_count.
*   Print the value of distinct_state_count.
'''

# Build a query to count the distinct states values: stmt
stmt = select([func.count(census.columns.state.distinct())])

# Execute the query and store the scalar result: distinct_state_count
distinct_state_count = connection.execute(stmt).scalar()

# Print the distinct_state_count
print(distinct_state_count)
