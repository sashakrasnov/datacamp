'''
Now that you've done all your manipulations, the last step before modeling is to split the data!

INSTRUCTIONS
100 XP
Use the DataFrame method .randomSplit() to split model_data into two pieces, training with 60% of the data, and test with 40% of the data by passing the list [.6, .4] to the .randomSplit() method.
'''

# Import LogisticRegression
from pyspark.ml.classification import LogisticRegression

# Create a LogisticRegression Estimator
lr = LogisticRegression()