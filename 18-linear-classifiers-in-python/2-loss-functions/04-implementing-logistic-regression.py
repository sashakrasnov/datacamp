'''
Implementing logistic regression

This is very similar to the earlier exercise where you implemented linear regression "from scratch" using scipy.optimize.minimize. However, this time we'll minimize the logistic loss and compare with scikit-learn's LogisticRegression (we've set C to a large value to disable regularization; more on this in Chapter 3!). The log_loss function from the previous exercise is already defined in your environment, and the sklearn breast cancer prediction dataset (first 10 features, standardized) is loaded into the variables X and y.
'''

from scipy.optimize import minimize
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn import preprocessing
import numpy as np

def log_loss(raw_model_output):
   return np.log(1+np.exp(-raw_model_output))


bc = datasets.load_breast_cancer()

X = preprocessing.StandardScaler().fit_transform(bc.data[:,:10])
y = bc.target

y[y==0] = -1

'''
INSTRUCTIONS

*   Fill in the loss function for logistic regression.
*   Compare the coefficients to sklearn's LogisticRegression.
'''

# The logistic loss, summed over training examples
def my_loss(w):
    s = 0
    for i in range(y.size):
        raw_model_output = w@X[i]
        s = s + log_loss(raw_model_output * y[i])
    return s

# Returns the w that makes my_loss(w) smallest
w_fit = minimize(my_loss, X[0]).x
print(w_fit)

# Compare with scikit-learn's LogisticRegression
lr = LogisticRegression(fit_intercept=False, C=1000000).fit(X,y)
print(lr.coef_)