'''
SQLAlchemy ResultsProxy and Pandas Dataframes

We can feed a ResultProxy directly into a pandas DataFrame, which is the workhorse of many Data Scientists in PythonLand. Jason demonstrated this in the video. In this exercise, you'll follow exactly the same approach to convert a ResultProxy into a DataFrame.
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

pop2008_sum = func.sum(census.columns.pop2008).label('population')

stmt = select([census.columns.state, pop2008_sum])
stmt = stmt.group_by(census.columns.state)

results = connection.execute(stmt).fetchall()

'''
INSTRUCTIONS

*   Import pandas as pd.
*   Create a DataFrame df using pd.DataFrame() on the ResultProxy results.
*   Set the columns of the DataFrame df.columns to be the columns from the first result object results[0].keys().
*   Print the DataFrame.
'''

# import pandas
import pandas as pd

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set column names
df.columns = results[0].keys()

# Print the Dataframe
print(df)
