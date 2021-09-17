'''
Remember the test data that you set aside waaaaaay back in chapter 3? It's finally time to test your model on it! You can use the same evaluator you made to fit the model.
'''

from pyspark.ml.classification import LogisticRegression
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StringIndexer, OneHotEncoder, StringIndexer, OneHotEncoder
from pyspark.ml import Pipeline

import pyspark.ml.tuning as tune
import pyspark.ml.evaluation as evals


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

piped_data = flights_pipe.fit(model_data).transform(model_data)

training, test = piped_data.randomSplit([.6, .4])

lr = LogisticRegression()

grid = tune.ParamGridBuilder()
grid = grid.addGrid(lr.regParam, np.arange(0, .1, .01))
grid = grid.addGrid(lr.elasticNetParam, [0, 1])

grid = grid.build()

evaluator = evals.BinaryClassificationEvaluator(metricName='areaUnderROC')

cv = tune.CrossValidator(estimator=lr, estimatorParamMaps=grid, evaluator=evaluator)

best_lr = lr.fit(training)

'''
INSTRUCTIONS

*   Use your model to generate predictions by applying best_lr.transform() to the test data.
*  Save this as test_results.
*   Call evaluator.evaluate() on test_results to compute the AUC. Print the output.
'''

# Use the model to predict the test set
test_results = best_lr.transform(test)

# Evaluate the predictions
print(evaluator.evaluate(test_results))
