'''
From SQLAlchemy results to a Graph

We can also take advantage of pandas and Matplotlib to build figures of our data. Remember that data visualization is essential for both exploratory data analysis and communication of your data!
'''

from sqlalchemy import create_engine, select, func, desc, MetaData, Table
import pandas as pd

# DataCamp PostgreSQL on AWS does not acceppt remote connections. Permission denied
# Local MySQL or SQLite may be used instead
#engine = create_engine('postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')
#engine = create_engine('mysql://root:@localhost:3306/circle')
engine = create_engine('sqlite:///../datasets/census.sqlite')

connection = engine.connect()

metadata = MetaData()

census = Table('census', metadata, autoload=True, autoload_with=engine)

pop2008_sum = func.sum(census.columns.pop2008).label('population')

stmt = select([census.columns.state, pop2008_sum])
stmt = stmt.group_by(census.columns.state).order_by(desc('population')).limit(5)

results = connection.execute(stmt).fetchall()

'''
INSTRUCTIONS

*   Import matplotlib.pyplot as plt.
*   Create a DataFrame df using pd.DataFrame() on the provided results.
*   Set the columns of the DataFrame df.columns to be the columns from the first result object results[0].keys().
*   Print the DataFrame df.
*   Use the plot.bar() method on df to create a bar plot of the results.
*   Display the plot with plt.show().
'''

# Import Pyplot as plt from matplotlib
import matplotlib.pyplot as plt

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set Column names
df.columns = results[0].keys()

# Print the DataFrame
print(df)

# Plot the DataFrame
df.plot.bar()
plt.show()
