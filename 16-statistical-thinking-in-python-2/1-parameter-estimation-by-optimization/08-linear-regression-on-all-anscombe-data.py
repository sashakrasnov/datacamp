'''
Linear regression on all Anscombe data

Now, to verify that all four of the Anscombe data sets have the same slope and intercept from a 
linear regression, you will compute the slope and intercept for each set. The data are stored in 
lists; anscombe_x = [x1, x2, x3, x4] and anscombe_y = [y1, y2, y3, y4], where, for example, x2 and y2 
are the x and y values for the second Anscombe data set.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../datasets/anscombe.csv', header=[0,1])

x = df.loc[:, (slice(None),'x')].values
y = df.loc[:, (slice(None),'y')].values

anscombe_x = np.transpose(x)
anscombe_y = np.transpose(y)

'''
INSTRUCTIONS

*   Write a for loop to do the following for each Anscombe data set.
    *   Compute the slope and intercept.
    *   Print the slope and intercept.
'''

# Iterate through x,y pairs
for x, y in zip(anscombe_x, anscombe_y):
    # Compute the slope and intercept: a, b
    a, b = np.polyfit(x, y, 1)

    # Print the result
    print('slope:', a, 'intercept:', b)
