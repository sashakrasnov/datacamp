'''
Now you'll encode the dest column just like you did in the previous exercise.
'''

from pyspark.ml.feature import StringIndexer, OneHotEncoder
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

'''
INSTRUCTIONS

*   Create a StringIndexer called dest_indexer by calling StringIndexer() with inputCol="dest" and outputCol="dest_index".
*   Create a OneHotEncoder called dest_encoder by calling OneHotEncoder() with inputCol="dest_index" and outputCol="dest_fact".
'''

# Create a StringIndexer
dest_indexer = StringIndexer(inputCol='dest', outputCol='dest_index')

# Create a OneHotEncoder
dest_encoder = OneHotEncoder(inputCol='dest_index', outputCol='dest_fact')