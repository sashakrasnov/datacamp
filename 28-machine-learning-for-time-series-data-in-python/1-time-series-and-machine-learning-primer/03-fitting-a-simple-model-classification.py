'''
Fitting a simple model: classification

In this exercise, you'll use the iris dataset (representing petal characteristics of a number of flowers) to practice using the scikit-learn API to fit a classification model.
'''

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()

data = pd.DataFrame(data=iris.data, columns=iris.feature_names)[50:]
data['target'] = iris['target'][50:]

'''
INSTRUCTIONS 1/2

*   Print the first five rows of data.
'''

# Print the first 5 rows for inspection
print(data.head())

'''
INSTRUCTIONS 2/2

*   Print the first five rows of data.
'''

from sklearn.svm import LinearSVC

# Construct data for the model
X = data[["petal length (cm)", "petal width (cm)"]]
y = data['target']

# Fit the model
model = LinearSVC()
model.fit(X, y)