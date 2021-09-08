'''
Imputing missing data in a ML Pipeline II

Having setup the steps of the pipeline in the previous exercise, you will now use it on the voting dataset to classify a Congressman's party affiliation. What makes pipelines so incredibly useful is the simple interface that they provide. You can use the .fit() and .predict() methods on pipelines just as you did with your classifiers and regressors!

Practice this for yourself now and generate a classification report of your predictions. The steps of the pipeline have been set up for you, and the feature array X and target variable array y have been pre-loaded. Additionally, train_test_split and classification_report have been imported from sklearn.model_selection and sklearn.metrics respectively.
'''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

df = pd.read_csv('../datasets/house-votes-84.csv', header=None).replace({'y': int(1), 'n': int(0), '?':np.nan})

# These lines of code is used to preproces and fill NaN values with column-mean values.
# But, in this example we use data pipelining to fill missing values
# I've left these lines to let you know on how it was solved in previous exercises
#   fills = (df.mean() > 0.5).astype('int') # fill values for NaN
#   df.fillna(value=fills, inplace=True)

df.columns = ['party', 'infants', 'water', 'budget', 'physician', 'salvador', 'religious', 'satellite', 'aid', 'missile', 'immigration', 'synfuels', 'education', 'superfund', 'crime', 'duty_free_exports', 'eaa_rsa']

df.loc[:, 'infants':'eaa_rsa'] = df.loc[:, 'infants':'eaa_rsa'].astype('float')

X = df.drop('party', axis=1)
y = df['party']

'''
INSTRUCTIONS

*   Import the following modules:
*   Imputer from sklearn.preprocessing and Pipeline from sklearn.pipeline.
*   SVC from sklearn.svm.
*   Create the pipeline using Pipeline() and steps.
*   Create training and test sets. Use 30% of the data for testing and a random state of 42.
*   Fit the pipeline to the training set and predict the labels of the test set.
*   Compute the classification report.
'''

# Import necessary modules
from sklearn.preprocessing import Imputer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

# Setup the pipeline steps: steps
steps = [
    ('imputation', Imputer(missing_values='NaN', strategy='most_frequent', axis=0)),
    ('SVM', SVC())
]

# Create the pipeline: pipeline
pipeline = Pipeline(steps)

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Fit the pipeline to the train set
pipeline.fit(X_train, y_train)

# Predict the labels of the test set
y_pred = pipeline.predict(X_test)

# Compute metrics
print(classification_report(y_test, y_pred))
