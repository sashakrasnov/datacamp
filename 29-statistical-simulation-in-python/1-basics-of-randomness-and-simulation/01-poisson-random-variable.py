'''
Poisson random variable

The numpy.random module also has a number of useful probability distributions for both discrete and continuous random variables. In this exercise, you will learn how to draw samples from a probability distribution.

In particular, you will draw samples from a very important discrete probability distribution, the Poisson distribution, which is typically used for modeling the average rate at which events occur.

Following the exercise, you should be able to apply these steps to any of the probability distributions found in numpy.random. In addition, you will also see how the sample mean changes as we draw more samples from a distribution.
'''

import numpy as np

'''
INSTRUCTIONS

*   Using np.random.poisson() draw samples from a Poisson distribution using lam (lambda) and size_1.
*   Repeat the above step, but this time use size_2.
*   For each of the above samples, calculate the absolute difference between their mean and lambda using the np.mean() and abs().
'''

# Initialize seed and parameters
np.random.seed(123) 
lam, size_1, size_2 = 5, 3, 1000  

# Draw samples & calculate absolute difference between lambda and sample mean
samples_1 = np.random.poisson(lam, size_1)
samples_2 = np.random.poisson(lam, size_2)
answer_1 = abs(samples_1.mean()-lam)
answer_2 = abs(samples_2.mean()-lam) 

print("|Lambda - sample mean| with {} samples is {} and with {} samples is {}. ".format(size_1, answer_1, size_2, answer_2))