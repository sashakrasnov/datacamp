'''
Load Data from a list into the Table

Using the multiple insert pattern, in this exercise, you will load the data from values_list into the table.
'''

from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer
import csv

engine = create_engine('sqlite:///../datasets/chapter5.sqlite')

metadata = MetaData()

census = Table('census', metadata,
               Column('state', String(30)),
               Column('sex', String(1)),
               Column('age', Integer()),
               Column('pop2000', Integer()),
               Column('pop2008', Integer()))

metadata.create_all(engine)

csv_file = open('../datasets/census.csv', newline='')
csv_reader = csv.reader(csv_file)

values_list = []

for row in csv_reader:
    data = {'state': row[0], 'sex': row[1], 'age': row[2], 'pop2000': row[3], 'pop2008': row[4]}
    values_list.append(data)

csv_file.close()

connection = engine.connect()

'''
INSTRUCTIONS

*   Import insert from sqlalchemy.
*   Build an insert statement for the census table.
*   Execute the statement stmt along with values_list. You will need to pass them both as arguments to connection.execute().
*   Print the rowcount attribute of results.
'''

# Import insert
from sqlalchemy import insert

# Build insert statement: stmt
stmt = insert(census)

# Use values_list to insert data: results
results = connection.execute(stmt, values_list)

# Print rowcount
print(results.rowcount)
