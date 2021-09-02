'''
EDA of beak depths of Darwin's finches

For your first foray into the Darwin finch data, you will study how the beak depth (the distance, top to bottom, of a closed beak) of the finch species Geospiza scandens has changed over time. The Grants have noticed some changes of beak geometry depending on the types of seeds available on the island, and they also noticed that there was some interbreeding with another major species on Daphne Major, Geospiza fortis. These effects can lead to changes in the species over time.

In the next few problems, you will look at the beak depth of G. scandens on Daphne Major in 1975 and in 2012. To start with, let's plot all of the beak depth measurements in 1975 and 2012 in a bee swarm plot.

The data are stored in a pandas DataFrame called df with columns 'year' and 'beak_depth'. The units of beak depth are millimeters (mm).
'''

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

frames = []

for y in [1975, 2012]:
    dfy = pd.read_csv('../datasets/finch_beaks_{}.csv'.format(y), skiprows=1, header=None)
    dfy[4] = y

    scns = (dfy[1] == 'scandens')

    frames.append(dfy[scns][[3,4]])

df = pd.concat(frames).reset_index(drop=True)
df.columns = ['beak_depth', 'year']

'''
INSTRUCTIONS

*   Create the beeswarm plot.
*   Label the axes.
*   Show the plot.
'''

# Create bee swarm plot
_ = sns.swarmplot(x='year', y='beak_depth', data=df)

# Label the axes
_ = plt.xlabel('year')
_ = plt.ylabel('beak depth (mm)')

# Show the plot
plt.show()