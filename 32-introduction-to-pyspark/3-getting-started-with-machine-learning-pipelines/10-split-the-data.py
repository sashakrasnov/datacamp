'''
Now that you've done all your manipulations, the last step before modeling is to split the data!
'''

from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StringIndexer, OneHotEncoder, StringIndexer, OneHotEncoder
from pyspark.ml import Pipeline

spark = SparkSession.builder.getOrCreate()

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

*   Use the DataFrame method .randomSplit() to split model_data into two pieces, training with 60% of the data, and test with 40% of the data by passing the list [.6, .4] to the .randomSplit() method.
'''

# Split the data into training and test sets
training, test = piped_data.randomSplit([.6, .4])