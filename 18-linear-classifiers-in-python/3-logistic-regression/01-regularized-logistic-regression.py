'''
Regularized logistic regression

In Chapter 1 you used logistic regression on the handwritten digits data set. Here, we'll explore the effect of L2 regularization. The handwritten digits dataset is already loaded, split, and stored in the variables X_train, y_train, X_valid, and y_valid. The variables train_errs and valid_errs are already initialized as empty lists.
'''

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

digits = datasets.load_digits()

X_train, X_valid, y_train, y_valid = train_test_split(digits.data, digits.target)

train_errs = []
valid_errs = []

C_values = [0.001, 0.01, 0.1, 1, 10, 100, 1000]

'''
INSTRUCTIONS

*   Loop over the different values of C_value, fitting a model each time. Save the error on the training set and the validation set for each model.
*   Create a plot of the training and testing error as a function of the regularization parameter, C.
*   Looking at the plot, what's the best value of C?
'''

# Loop over values of C
for C_value in C_values:
    # Create LogisticRegression object and fit
    lr = LogisticRegression(C=C_value)
    lr.fit(X_train, y_train)
    
    # Evaluate error rates and append to lists
    train_errs.append( 1.0 - lr.score(X_train, y_train) )
    valid_errs.append( 1.0 - lr.score(X_valid, y_valid) )
    
# Plot results
plt.semilogx(C_values, train_errs, C_values, valid_errs)
plt.legend(("train", "validation"))
plt.show()