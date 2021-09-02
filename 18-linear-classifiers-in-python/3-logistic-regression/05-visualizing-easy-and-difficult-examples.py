'''
Visualizing easy and difficult examples

In this exercise, you'll visualize the examples that the logistic regression model is most, and least, confident about by looking at the largest, and smallest, predicted probabilities. The handwritten digits dataset is already loaded into the variables X and y. The show_digit function takes in an integer index and plots the corresponding image, with some extra information displayed above the image.
'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LogisticRegression

def show_digit(i, lr=None):
    plt.imshow(np.reshape(X[i], (8,8)), cmap='gray', vmin = 0, vmax = 16, interpolation=None)
    plt.xticks(())
    plt.yticks(())

    if lr is None:
        plt.title("class label = %d" % y[i])
    else:
        pred = lr.predict(X[i][None])
        pred_prob = lr.predict_proba(X[i][None])[0,pred]
        plt.title("label=%d, prediction=%d, proba=%.2f" % (y[i], pred, pred_prob))
    
    plt.show()


digits = datasets.load_digits()

X, y = digits.data, digits.target

'''
INSTRUCTIONS

*   Fill in the first blank with the index of the digit that the model is most confident about.
*   Fill in the second blank with the index of the digit that the model is least confident about.
*   Observe the images: do you agree that the first one is more ambiguous than the second?
'''

lr = LogisticRegression()
lr.fit(X,y)

# Get predicted probabilities
proba = lr.predict_proba(X)

# Sort the example indices by their maximum probability
proba_inds = np.argsort(np.max(proba,axis=1))

# Show the most confident (least ambiguous) digit
show_digit(proba_inds[-1], lr)

# Show the least confident (most ambiguous) digit
show_digit(proba_inds[0], lr)