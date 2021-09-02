'''
Visualizing predicted values

When dealing with time series data, it's useful to visualize model predictions on top of the "actual" values that are used to test the model.

In this exercise, after splitting the data (stored in the variables X and y) into training and test sets, you'll build a model and then visualize the model's predictions on top of the testing data in order to estimate the model's performance.
'''

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

all_prices = pd.read_csv('../datasets/all_prices.csv', index_col=0, parse_dates=True).iloc[:775]

X = all_prices[["EBAY", "NVDA", "YHOO"]]
y = all_prices[["AAPL"]]

'''
INSTRUCTIONS 1/2

*   Split the data (X and y) into training and test sets.
*   Use the training data to train the regression model.
*   Then use the testing data to generate predictions for the model.
'''

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Split our data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, shuffle=False, random_state=1)

# Fit our model and generate predictions
model = Ridge()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
score = r2_score(y_test, predictions)
print(score)

'''
INSTRUCTIONS 2/2

*   Plot a time series of the predicted and "actual" values of the testing data.
'''

# Visualize our predictions along with the "true" values, and print the score
fig, ax = plt.subplots(figsize=(15, 5))
ax.plot(y_test, color='k', lw=3)
ax.plot(list(y_test.index), predictions, color='r', lw=2)
plt.show()