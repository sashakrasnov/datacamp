'''
Build a classification model

While eye-balling differences is a useful way to gain an intuition for the data, let's see if you can operationalize things with a model. In this exercise, you will use each repetition as a datapoint, and each moment in time as a feature to fit a classifier that attempts to predict abnormal vs. normal heartbeats using only the raw data.

We've split the two DataFrames (normal and abnormal) into X_train, X_test, y_train, and y_test.
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

normal = pd.read_csv('../datasets/heartbeats_normal_full.csv', index_col=0)
abnormal = pd.read_csv('../datasets/heartbeats_abnormal_full.csv', index_col=0)

X = np.hstack([normal, abnormal]).T
y = np.array(['normal'] * len(normal.columns) + ['abnormal'] * len(abnormal.columns))#.reshape([-1,1])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=40)

'''
INSTRUCTIONS

*   Create an instance of the Linear SVC model and fit the model using the training data.
*   Use the testing data to generate predictions with the model.
*   Score the model using the provided code.
'''

from sklearn.svm import LinearSVC

# Initialize and fit the model
model = LinearSVC()
model.fit(X_train, y_train)

# Generate predictions and score them manually
predictions = model.predict(X_test)
print(sum(predictions == y_test.squeeze()) / len(y_test))