'''
Fitting a simple regression model

Now we'll look at a larger number of companies. Recall that we have historical price values for many companies. Let's use data from several companies to predict the value of a test company. You'll attempt to predict the value of the Apple stock price using the values of NVidia, Ebay, and Yahoo. Each of these is stored as a column in the prices DataFrame. Below is a mapping from company name to column name:

|   ebay: "EBAY"
|   nvidia: "NVDA"
|   yahoo: "YHOO"
|   apple: "AAPL"

We'll use these columns to define the input/output arrays in our model.
'''

import pandas as pd

all_prices = pd.read_csv('../datasets/all_prices.csv', index_col=0, parse_dates=True).iloc[:1278]

'''
INSTRUCTIONS

*   Create the X and y arrays by using the column names provided.
*   The input values should be from the companies "ebay", "nvidia", and "yahoo"
*   The output values should be from the company "apple"
*   Use the data to train and score the model with cross-validation.
'''

from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

# Use stock symbols to extract training data
X = all_prices[["EBAY", "NVDA", "YHOO"]]
y = all_prices[["AAPL"]]

# Fit and score the model with cross-validation
scores = cross_val_score(Ridge(), X, y, cv=3)
print(scores)