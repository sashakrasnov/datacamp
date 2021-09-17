'''
Hooray, now you're finally ready to pass your data through the Pipeline you created!
'''

from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StringIndexer, OneHotEncoder, StringIndexer, OneHotEncoder
from pyspark.ml import Pipeline

spark = SparkSession.builder.getOrCreate()

flights = spark.table('flights')
planes = planes.table('planes')

model_data = flights.join(planes, on='tailnum', how='leftouter')


vec_assembler = VectorAssembler(inputCols=['month', 'air_time', 'carrier_fact', 'dest_fact', 'plane_age'], outputCol='features')
dest_indexer = StringIndexer(inputCol='dest', outputCol='dest_index')
dest_encoder = OneHotEncoder(inputCol='dest_index', outputCol='dest_fact')
carr_indexer = StringIndexer(inputCol='carrier', outputCol='carrier_index')
carr_encoder = OneHotEncoder(inputCol='carrier_index', outputCol='carrier_fact')

flights_pipe = Pipeline(
    stages = [
        dest_indexer,
        dest_encoder,
        carr_indexer,
        carr_encoder,
        vec_assembler
    ]
)

'''
INSTRUCTIONS

*   Create the DataFrame piped_data by calling the Pipeline methods .fit() and .transform() in a chain. Both of these methods take model_data as their only argument.
'''

# Fit and transform the data
piped_data = flights_pipe.fit(model_data).transform(model_data)