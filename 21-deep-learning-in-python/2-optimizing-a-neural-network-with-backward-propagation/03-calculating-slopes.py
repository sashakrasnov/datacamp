'''
Calculating slopes

You're now going to practice calculating slopes. When plotting the mean-squared error loss function against predictions, the slope is 2 * x * (y-xb), or 2 * input_data * error. Note that x and b may have multiple numbers (x is a vector for each data point, and b is a vector). In this case, the output will also be a vector, which is exactly what you want.

You're ready to write the code to calculate this slope while using a single data point. You'll use pre-defined weights called weights as well as data for a single point called input_data. The actual value of the target you want to predict is stored in target.
'''

import numpy as np

input_data = np.array([1, 2, 3])

weights = np.array([0, 2, 1])

target = 0

'''
INSTRUCTIONS

*   Calculate the predictions, preds, by multiplying weights by the input_data and computing their sum.
*   Calculate the error, which is the difference between target and preds. Notice that this error corresponds to y-xb in the gradient expression.
*   Calculate the slope of the loss function with respect to the prediction. To do this, you need to take the product of input_data and error and multiply that by 2.
'''

# Calculate the predictions: preds
preds = (weights * input_data).sum()

# Calculate the error: error
error = target - preds

# Calculate the slope: slope
slope = input_data * error * 2

# Print the slope
print(slope)
