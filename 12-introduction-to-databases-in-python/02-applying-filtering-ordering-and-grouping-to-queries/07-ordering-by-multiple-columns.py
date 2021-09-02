'''
Ordering by Multiple Columns

We can pass multiple arguments to the .order_by() method to order by multiple columns. In fact, we can also sort in ascending or descending order for each individual column. Each column in the .order_by() method is fully sorted from left to right. This means that the first column is completely sorted, and then within each matching group of values in the first column, it's sorted by the next column in the .order_by() method. This process is repeated until all the columns in the .order_by() are sorted.
'''

from sqlalchemy import create_engine, select, desc, MetaData, Table

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

Select all records of the state and age columns from the census table.
Use .order_by() to sort the output of the state column in ascending order and age in descending order. (NOTE: desc is already imported).
Execute stmt using the .execute() method on connection and retrieve all the results using .fetchall().
Print the first 20 results.
'''

# Build a query to select state and age: stmt
stmt = select([census.columns.state, census.columns.age])

# Append order by to ascend by state and descend by age
stmt = stmt.order_by(census.columns.state, desc(census.columns.age))

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print the first 20 results
print(results[:20])
