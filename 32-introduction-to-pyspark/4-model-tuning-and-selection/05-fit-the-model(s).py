'''
You're finally ready to fit the models and select the best one!

Unfortunately, cross validation is a very computationally intensive procedure. Fitting all the models would take too long on DataCamp.

To do this locally you would use the code

# Fit cross validation models
models = cv.fit(training)

# Extract the best model
best_lr = models.bestModel
Remember, the training data is called training and you're using lr to fit a logistic regression model. Cross validation selected the parameter values regParam=0 and elasticNetParam=0 as being the best. These are the default values, so you don't need to do anything else with lr before fitting the model.
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

'''
INSTRUCTIONS

*   Create best_lr by calling lr.fit() on the training data.
*   Print best_lr to verify that it's an object of the LogisticRegressionModel class.
'''

# Call lr.fit()
best_lr = lr.fit(training)

# Print best_lr
print(best_lr)