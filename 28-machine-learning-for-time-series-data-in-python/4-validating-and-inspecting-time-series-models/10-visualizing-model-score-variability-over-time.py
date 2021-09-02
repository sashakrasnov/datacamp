'''
Visualizing model score variability over time

Now that you've assessed the variability of each coefficient, let's do the same for the performance (scores) of the model. Recall that the TimeSeriesSplit object will use successively-later indices for each test set. This means that you can treat the scores of your validation as a time series. You can visualize this over time in order to see how the model's performance changes over time.

An instance of the Linear regression model object is stored in model, a cross-validation object in cv, and data in X and y.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from functools import partial
from sklearn.utils import resample
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import TimeSeriesSplit

def bootstrap_interval(data, percentiles=(2.5, 97.5), n_boots=100):
    """Bootstrap a confidence interval for the mean of columns of a 2-D dataset."""
    # Create our empty array to fill the results
    bootstrap_means = np.zeros([n_boots, data.shape[-1]])
    for ii in range(n_boots):
        # Generate random indices for our data *with* replacement, then take the sample mean
        random_sample = resample(data)
        bootstrap_means[ii] = random_sample.mean(axis=0)
        
    # Compute the percentiles of choice for the bootstrapped means
    percentiles = np.percentile(bootstrap_means, percentiles, axis=0)
    return percentiles


def my_pearsonr(est, X, y):
    return np.corrcoef(est.predict(X).squeeze(), y.squeeze())[1, 0]


X = np.loadtxt('../datasets/X.csv', delimiter=',')
y = np.loadtxt('../datasets/y.csv', delimiter=',')

feature_names = ['AAPL_lag_1_day', 'YHOO_lag_1_day', 'NVDA_lag_1_day', 'AAPL_lag_2_day',
                 'YHOO_lag_2_day', 'NVDA_lag_2_day', 'AAPL_lag_3_day', 'YHOO_lag_3_day',
                 'NVDA_lag_3_day', 'AAPL_lag_4_day']

times_scores = pd.Index(['2010-04-05', '2010-04-28', '2010-05-21', '2010-06-16',
                '2010-07-12', '2010-08-04', '2010-08-27', '2010-09-22',
                '2010-10-15', '2010-11-09', '2010-12-03', '2010-12-29',
                '2011-01-24', '2011-02-16', '2011-03-14', '2011-04-06',
                '2011-05-02', '2011-05-25', '2011-06-20', '2011-07-14',
                '2011-08-08', '2011-08-31', '2011-09-26', '2011-10-19',
                '2011-11-11', '2011-12-07', '2012-01-03', '2012-01-27',
                '2012-02-22', '2012-03-16', '2012-04-11', '2012-05-04',
                '2012-05-30', '2012-06-22', '2012-07-18', '2012-08-10',
                '2012-09-05', '2012-09-28', '2012-10-23', '2012-11-19',
                '2012-12-13', '2013-01-09', '2013-02-04', '2013-02-28',
                '2013-03-25', '2013-04-18', '2013-05-13', '2013-06-06',
                '2013-07-01', '2013-07-25', '2013-08-19', '2013-09-12',
                '2013-10-07', '2013-10-30', '2013-11-22', '2013-12-18',
                '2014-01-14', '2014-02-07', '2014-03-05', '2014-03-28',
                '2014-04-23', '2014-05-16', '2014-06-11', '2014-07-07',
                '2014-07-30', '2014-08-22', '2014-09-17', '2014-10-10',
                '2014-11-04', '2014-11-28', '2014-12-23', '2015-01-20',
                '2015-02-12', '2015-03-10', '2015-04-02', '2015-04-28',
                '2015-05-21', '2015-06-16', '2015-07-10', '2015-08-04',
                '2015-08-27', '2015-09-22', '2015-10-15', '2015-11-09',
                '2015-12-03', '2015-12-29', '2016-01-25', '2016-02-18',
                '2016-03-14', '2016-04-07', '2016-05-02', '2016-05-25',
                '2016-06-20', '2016-07-14', '2016-08-08', '2016-08-31',
                '2016-09-26', '2016-10-19', '2016-11-11', '2016-12-07'])

model = LinearRegression()

# Iterate through CV splits
n_splits = 100
cv = TimeSeriesSplit(n_splits=n_splits)

# Create empty array to collect coefficients
coefficients = np.zeros([n_splits, X.shape[1]])

for ii, (tr, tt) in enumerate(cv.split(X, y)):
    # Fit the model on training data and collect the coefficients
    model.fit(X[tr], y[tr])
    coefficients[ii] = model.coef_

'''
INSTRUCTIONS 1/2

*   Calculate the cross-validated scores of the model on the data (using a custom scorer we defined for you, my_pearsonr along with cross_val_score).
*   Convert the output scores into a pandas Series so that you can treat it as a time series.
*   Bootstrap a rolling confidence interval for the mean score using bootstrap_interval().
'''

from sklearn.model_selection import cross_val_score

# Generate scores for each split to see how the model performs over time
scores = cross_val_score(model, X, y, cv=cv, scoring=my_pearsonr)

# Convert to a Pandas Series object
scores_series = pd.Series(scores, index=times_scores, name='score')

# Bootstrap a rolling confidence interval for the mean score
scores_lo = scores_series.rolling(20).aggregate(partial(bootstrap_interval, percentiles=2.5))
#scores_lo = scores_series.rolling(20).min()
scores_hi = scores_series.rolling(20).aggregate(partial(bootstrap_interval, percentiles=97.5))
#scores_hi = scores_series.rolling(20).max()

'''
INSTRUCTIONS 2/2

*   Run the given code to plot the results.
'''

# Plot the results
fig, ax = plt.subplots()
scores_lo.plot(ax=ax, label="Lower confidence interval")
scores_hi.plot(ax=ax, label="Upper confidence interval")
ax.legend()
plt.show()