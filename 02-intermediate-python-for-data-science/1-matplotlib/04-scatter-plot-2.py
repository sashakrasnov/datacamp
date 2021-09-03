'''
Scatter plot (2)

In the previous exercise, you saw that that the higher GDP usually corresponds to a higher life expectancy. In other words, there is a positive correlation.

Do you think there's a relationship between population and life expectancy of a country? The list life_exp from the previous exercise is already available. In addition, now also pop is available, listing the corresponding populations for the countries in 2007. The populations are in millions of people.
'''

import csv

pop = []
life_exp = []

with open('../datasets/gapminder.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        pop.append(float(row['population']))
        life_exp.append(float(row['life_exp']))

'''
Instructions

*   Start from scratch: import matplotlib.pyplot as plt.
*   Build a scatter plot, where pop is mapped on the horizontal axis, and life_exp is mapped on the vertical axis.
*   Finish the script with plt.show() to actually display the plot. Do you see a correlation?
'''

# Import package
import matplotlib.pyplot as plt

# Build Scatter plot
plt.scatter(pop, life_exp)

# Show plot
plt.show()

# Nice! There's no clear relationship between population and life expectancy, which makes perfect sense.