'''
Visualizing USA Medal Counts by Edition: Line Plot

Your job in this exercise is to visualize the medal counts by 'Edition' for the USA. The DataFrame has been pre-loaded for you as medals.

INSTRUCTIONS

*   Create a DataFrame usa with data only for the USA.
*   Group usa such that ['Edition', 'Medal'] is the index. Aggregate the count over 'Athlete'.
*   Use .unstack() with level='Medal' to reshape the DataFrame usa_medals_by_year.
*   Construct a line plot from the final DataFrame usa_medals_by_year. This has been done for you, so hit 'Submit Answer' to see the plot!
'''

import pandas as pd
import matplotlib.pyplot as plt

medals = pd.read_csv('../datasets/all_medalists.csv')

# ---

# Create the DataFrame: usa
usa = medals[medals.NOC == 'USA']

# Group usa by ['Edition', 'Medal'] and aggregate over 'Athlete'
usa_medals_by_year = usa.groupby(['Edition', 'Medal'])['Athlete'].count()

# Reshape usa_medals_by_year by unstacking
usa_medals_by_year = usa_medals_by_year.unstack(level='Medal')

# Plot the DataFrame usa_medals_by_year
usa_medals_by_year.plot()
plt.show()

