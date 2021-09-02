'''
Fitting a simple model: regression

In this exercise, you'll practice fitting a regression model using data from the Boston housing market. A DataFrame called boston is available in your workspace. It contains many variables of data (stored as columns). Can you find a relationship between the following two variables?

"AGE": proportion of owner-occupied units built prior to 1940
"RM" : average number of rooms per dwelling
'''

import pandas as pd

from sklearn.datasets import load_boston

bst = load_boston()

boston = pd.DataFrame(data=bst.data, columns=bst.feature_names)

'''
INSTRUCTIONS

*   Prepare X and y DataFrames using the data in boston.
    *   X should be the proportion of houses built prior to 1940, y average number of rooms per dwelling.
*   Fit a regression model that uses these variables (remember to shape the variables correctly!).
*   Don't forget that each variable must be the correct shape for scikit-learn to use it!
'''

from sklearn import linear_model

# Prepare input and output DataFrames
X = boston[['AGE']]
y = boston[['RM']]

# Fit the model
model = linear_model.LinearRegression()
model.fit(X, y)