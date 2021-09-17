'''
You're finally ready to create a Pipeline!

Pipeline is a class in the pyspark.ml module that combines all the Estimators and Transformers that you've already created. This lets you reuse the same modeling process over and over again by wrapping it up in one simple object. Neat, right?
'''

from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StringIndexer, OneHotEncoder, StringIndexer, OneHotEncoder

spark = SparkSession.builder.getOrCreate()

vec_assembler = VectorAssembler(inputCols=['month', 'air_time', 'carrier_fact', 'dest_fact', 'plane_age'], outputCol='features')
dest_indexer = StringIndexer(inputCol='dest', outputCol='dest_index')
dest_encoder = OneHotEncoder(inputCol='dest_index', outputCol='dest_fact')
carr_indexer = StringIndexer(inputCol='carrier', outputCol='carrier_index')
carr_encoder = OneHotEncoder(inputCol='carrier_index', outputCol='carrier_fact')

'''
INSTRUCTIONS

*   Import Pipeline from pyspark.ml.
*   Call the Pipeline() constructor with the keyword argument stages to create a Pipeline called flights_pipe.
stages should be a list holding all the stages you want your data to go through in the pipeline. *  Here this is just [dest_indexer, dest_encoder, carr_indexer, carr_encoder, vec_assembler]
'''

# Import Pipeline
from pyspark.ml import Pipeline

# Make the pipeline
flights_pipe = Pipeline(
    stages = [
        dest_indexer,
        dest_encoder,
        carr_indexer,
        carr_encoder,
        vec_assembler
    ]
)