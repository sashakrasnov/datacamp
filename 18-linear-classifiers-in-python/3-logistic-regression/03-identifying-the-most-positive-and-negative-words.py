'''
Identifying the most positive and negative words

In this exercise we'll try to interpret the coefficients of a logistic regression fit on the movie review sentiment data set. The model object is already instantiated and fit for you in the variable lr.

In addition, the words corresponding to the different features are loaded into the variable vocab. For example, since vocab[100] is "think", that means feature 100 corresponds to the number of times the word "think" appeared in that movie review.
'''

import scipy.sparse as sps
import numpy as np
from scipy.sparse import hstack, vstack
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

with open('../datasets/imdb.vocab') as f:
    vocab = [f.readline().strip() for _ in range(2500)]

X_train = vstack((sps.load_npz('../datasets/X_train.csr.npz'),
                  sps.load_npz('../datasets/X_test.csr.npz')))

y_train = hstack((sps.load_npz('../datasets/y_train.csr.npz'),
                  sps.load_npz('../datasets/y_test.csr.npz'))).data

lr = LogisticRegression(penalty='l1')
lr.fit(X_train, y_train)

#searcher = GridSearchCV(LogisticRegression(penalty='l1'), {'C':[0.001, 0.01, 0.1, 1, 10]})
#searcher.fit(X_train, y_train)

#lr = searcher.best_estimator_

'''
INSTRUCTIONS

*   Find the words corresponding to the 5 largest coefficients.
*   Find the words corresponding to the 5 smallest coefficients.
'''

# Get the indices of the sorted cofficients
inds_ascending = np.argsort(lr.coef_.flatten()) 
inds_descending = inds_ascending[::-1]

# Print the most positive words
print("Most positive words: ", end="")
for i in range(5):
    print(vocab[inds_descending[i]], end=", ")
print("\n")

# Print most negative words
print("Most negative words: ", end="")
for i in range(5):
    print(vocab[inds_ascending[i]], end=", ")
print("\n")