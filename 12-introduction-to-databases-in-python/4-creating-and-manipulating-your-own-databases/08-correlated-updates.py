'''
Correlated Updates
You can also update records with data from a select statement. This is called a correlated update. It works by defining a select statement that returns the value you want to update the record with and assigning that as the value in an update statement.

You'll be using a flat_census in this exercise as the target of your correlated update. The flat_census table is a summarized copy of your census table.
'''

from sqlalchemy import create_engine, select, update, MetaData, Table

engine = create_engine('sqlite:///../datasets/flat_census.sqlite')

metadata = MetaData()

state_fact  = Table('state_fact',  metadata, autoload=True, autoload_with=engine)
flat_census = Table('flat_census', metadata, autoload=True, autoload_with=engine)

connection = engine.connect()

'''
INSTRUCTIONS

*   Build a statement to select the name column from state_fact. Save the statement as fips_stmt.
*   Append a where clause to fips_stmt that matches fips_state from the state_fact table with fips_code in the flat_census table.
*   Build an update statement to set the state_name in flat_census to fips_stmt. Save the statement as update_stmt.
*   Hit 'Submit Answer' to execute update_stmt, store the results and print the rowcount of results.
'''

# Build a statement to select name from state_fact: stmt
fips_stmt = select([state_fact.columns.name])

# Append a where clause to Match the fips_state to flat_census fips_code
fips_stmt = fips_stmt.where(
    state_fact.columns.fips_state == flat_census.columns.fips_code)

# Build an update statement to set the name to fips_stmt: update_stmt
update_stmt = update(flat_census).values(state_name=fips_stmt)

# Execute update_stmt: results
results = connection.execute(update_stmt)

# Print rowcount
print(results.rowcount)
