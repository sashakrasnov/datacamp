'''
Additional Customizations

If you have another look at the script, under # Additional Customizations, you'll see that there are two plt.text() functions now. They add the words "India" and "China" in the plot.
'''

import csv

gdp_cap = []
life_exp = []
pop = []

with open('../datasets/gapminder.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        gdp_cap.append(float(row['gdp_cap']))
        life_exp.append(float(row['life_exp']))
        pop.append(float(row['population']) / 1E6)

col = ['red', 'green']

'''
Instructions

*   Add plt.grid(True) after the plt.text() calls so that gridlines are drawn on the plot.
'''

import matplotlib.pyplot as plt
import numpy as np

# Scatter plot
plt.scatter(x=gdp_cap, y=life_exp, s=2*np.array(pop), c=col, alpha=0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()
