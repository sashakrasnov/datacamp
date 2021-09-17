'''
The submodule pyspark.ml.tuning also has a class called CrossValidator for performing cross validation. This Estimator takes the modeler you want to fit, the grid of hyperparameters you created, and the evaluator you want to use to compare your models.

The submodule pyspark.ml.tune has already been imported as tune. You'll create the CrossValidator by passing it the logistic regression Estimator lr, the parameter grid, and the evaluator you created in the previous exercises.
'''

from pyspark.ml.classification import LogisticRegression

import pyspark.ml.tuning as tune
import pyspark.ml.evaluation as evals

lr = LogisticRegression()

grid = tune.ParamGridBuilder()
grid = grid.addGrid(lr.regParam, np.arange(0, .1, .01))
grid = grid.addGrid(lr.elasticNetParam, [0, 1])

grid = grid.build()

evaluator = evals.BinaryClassificationEvaluator(metricName='areaUnderROC')

'''
INSTRUCTIONS

*   Create a CrossValidator by calling tune.CrossValidator() with the arguments:
    - estimator=lr
    - estimatorParamMaps=grid
    - evaluator=evaluator
*   Name this object cv.
'''

# Create the CrossValidator
cv = tune.CrossValidator(estimator=lr, estimatorParamMaps=grid, evaluator=evaluator)
