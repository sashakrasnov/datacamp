'''
Making predictions

The trained network from your previous coding exercise is now stored as model. New data to make predictions is stored in a NumPy array as pred_data. Use model to make predictions on your new data.

In this exercise, your predictions will be probabilities, which is the most common way for data scientists to communicate their predictions to colleagues.
'''

import pandas as pd
import numpy as np
import keras

from keras.layers import Dense
from keras.models import Sequential
from keras.utils.np_utils import to_categorical

def relu(input):
    '''Define your relu activation function here
    '''

    # Calculate the value for the output of the relu function: output
    output = max(0, input)
    
    # Return the value just calculated
    return output


split = 800

df = pd.read_csv('../datasets/titanic_all_numeric.csv')

predictors = df.drop('survived', axis=1).values[:split]
pred_data = df.drop('survived', axis=1).values[split:]

n_cols = predictors.shape[1]

target = to_categorical(df.survived[:split])

'''
INSTRUCTIONS

*   Create your predictions using the model's .predict() method on pred_data.
*   Use NumPy indexing to find the column corresponding to predicted probabilities of survival being True. This is the second column (index 1) of predictions. Store the result in predicted_prob_true and print it.
'''

# Specify, compile, and fit the model
model = Sequential()

model.add(Dense(32, activation='relu', input_shape = (n_cols,)))
model.add(Dense(2, activation='softmax'))

model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(predictors, target, epochs=10)

# Calculate predictions: predictions
predictions = model.predict(pred_data)

# Calculate predicted probability of survival: predicted_prob_true
predicted_prob_true = predictions[:,1]

# print predicted_prob_true
print(predicted_prob_true)
