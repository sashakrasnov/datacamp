'''
Compiling the model

You're now going to compile the model you specified earlier. To compile the model, you need to specify the optimizer and loss function to use. In the video, Dan mentioned that the Adam optimizer is an excellent choice. You can read more about it as well as other keras optimizers here (https://keras.io/optimizers/#adam), and if you are really curious to learn more, you can read the original paper (https://arxiv.org/abs/1412.6980v8) that introduced the Adam optimizer.

In this exercise, you'll use the Adam optimizer and the mean squared error loss function. Go for it!
'''

import numpy as np

def relu(input):
    '''Define your relu activation function here
    '''

    # Calculate the value for the output of the relu function: output
    output = max(0, input)
    
    # Return the value just calculated
    return output


predictors = np.loadtxt('../datasets/hourly_wages.csv', delimiter=',', skiprows=1, usecols=range(1,10))

'''
INSTRUCTIONS

*   Compile the model using model.compile(). Your optimizer should be 'adam' and the loss should be 'mean_squared_error'.
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

# Verify that model contains information from compiling
print('Loss function:', model.loss)
