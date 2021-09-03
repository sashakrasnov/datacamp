'''
Build a histogram (1)

life_exp, the list containing data on the life expectancy for different countries in 2007, is available in your Python shell.

To see how life expectancy in different countries is distributed, let's create a histogram of life_exp.
'''

import csv

life_exp = []

with open('../datasets/gapminder.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        life_exp.append(float(row['life_exp']))

'''
Instructions

*   Use plt.hist() to create a histogram of the values in life_exp. Do not specify the number of bins; Python will set the number of bins to 10 by default for you.
*   Add plt.show() to actually display the histogram. Can you tell which bin contains the most observations?
'''

import matplotlib.pyplot as plt

# Create histogram of life_exp data
plt.hist(life_exp)

# Display histogram
plt.show()
