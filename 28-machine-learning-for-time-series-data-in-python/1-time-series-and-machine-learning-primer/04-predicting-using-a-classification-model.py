'''
Predicting using a classification model

Now that you have fit your classifier, let's use it to predict the type of flower (or class) for some newly-collected flowers.

Information about petal width and length for several new flowers is stored in the variable targets. Using the classifier you fit, you'll predict the type of each flower.
'''

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.svm import LinearSVC
from random import choices

iris = load_iris()

data = pd.DataFrame(data=iris.data, columns=iris.feature_names)[50:]
data['target'] = iris['target'][50:]

# Construct data for the model
X = data[["petal length (cm)", "petal width (cm)"]]
y = data['target']

# Fit the model
model = LinearSVC()
model.fit(X, y)

targets = data.loc[choices(data.index.tolist(), k=20)]

'''
INSTRUCTIONS

*   Predict the flower type using the array X_predict.
*   Run the given code to visualize the predictions.
'''

# Create input array
X_predict = targets[['petal length (cm)', 'petal width (cm)']]

# Predict with the model
predictions = model.predict(X_predict)
print(predictions)

# Visualize predictions and actual values
plt.scatter(X_predict['petal length (cm)'], X_predict['petal width (cm)'],
            c=predictions, cmap=plt.cm.coolwarm)
plt.title("Predicted class values")
plt.show()