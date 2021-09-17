'''
Fitting the model

You're at the most fun part. You'll now fit the model. Recall that the data to be used as predictive features is loaded in a NumPy matrix called predictors and the data to be predicted is stored in a NumPy matrix called target. Your model is pre-written and it has been compiled with the code from the previous exercise.
'''

import numpy as np

def relu(input):
    '''Define your relu activation function here
    '''

    # Calculate the value for the output of the relu function: output
    output = max(0, input)
    
    # Return the value just calculated
    return output


data = np.loadtxt('../datasets/hourly_wages.csv', delimiter=',', skiprows=1)

predictors = data[:, 1:]
target = data[:, 0]

'''
INSTRUCTIONS

*   Fit the model. Remember that the first argument is the predictive features (predictors), and the data to be predicted (target) is the second argument.
'''

# Import necessary modules
import keras
from keras.layers import Dense
from keras.models import Sequential

# Specify the model
n_cols = predictors.shape[1]
model = Sequential()
model.add(Dense(50, activation='relu', input_shape = (n_cols,)))
model.add(Dense(32, activation='relu'))
model.add(Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Fit the model
model.fit(predictors, target, epochs=10)
