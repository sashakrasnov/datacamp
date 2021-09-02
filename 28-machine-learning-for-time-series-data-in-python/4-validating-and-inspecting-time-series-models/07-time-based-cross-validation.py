'''
Time-based cross-validation

Finally, let's visualize the behavior of the time series cross-validation iterator in scikit-learn. Use this object to iterate through your data one last time, visualizing the training data used to fit the model on each iteration.

An instance of the Linear regression model object is available in your workpsace. Also, the arrays X and y (training data) are available too.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

X = np.loadtxt('../datasets/X.csv', delimiter=',')
y = np.loadtxt('../datasets/y.csv', delimiter=',')

'''
INSTRUCTIONS

*   Import TimeSeriesSplit from sklearn.model_selection.
*   Instantiate a time series cross-validation iterator with 10 splits.
*   Iterate through CV splits. On each iteration, visualize the values of the input data that would be used to train the model for that iteration.
'''

# Import TimeSeriesSplit
from sklearn.model_selection import TimeSeriesSplit

# Create time-series cross-validation object
cv = TimeSeriesSplit(n_splits=10)

# Iterate through CV splits
fig, ax = plt.subplots()
for ii, (tr, tt) in enumerate(cv.split(X, y)):
    # Plot the training data on each iteration, to see the behavior of the CV
    ax.plot(tr, ii + y[tr])

ax.set(title='Training data on each CV iteration', ylabel='CV iteration')
plt.show()