'''
Plotting distributions pairwise (2)

In this exercise, you will generate pairwise joint distributions again. This time, you will make two particular additions:

You will display regressions as well as scatter plots in the off-diagonal subplots. You will do this with the argument kind='reg' (where 'reg' means 'regression'). Another option for kind is 'scatter' (the default) that plots scatter plots in the off-diagonal subplots.
You will also visualize the joint distributions separated by continent of origin. You will do this with the keyword argument hue specifying the 'origin'.
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

auto = pd.read_csv('../datasets/auto-mpg.csv', usecols=['mpg','hp','origin'])

'''
INSTRUCTIONS

*   Plot the pairwise joint distributions separated by continent of origin and display the regressions.
'''

# Print the first 5 rows of the DataFrame
print(auto.head())

# Plot the pairwise joint distributions grouped by 'origin' along with regression lines
sns.pairplot(data=auto, kind='reg', hue='origin')

# Display the plot
plt.show()
