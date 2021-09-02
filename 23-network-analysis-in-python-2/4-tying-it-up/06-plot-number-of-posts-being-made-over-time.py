'''
Plot number of posts being made over time

Let's recap how you can plot evolving graph statistics from the graph data. First off, you will use the graph data to quantify the number of edges that show up within a chunking time window of td days, which is 2 days in the exercise below.

The datetime variables dayone and lastday have been provided for you.
'''

import pandas as pd
import networkx as nx
from datetime import datetime

data = pd.read_csv('../datasets/student-forum-subsampled.csv', index_col=[0], parse_dates=[3])

# Instantiate a new Graph: G
G = nx.Graph()

# Add nodes from each of the partitions
G.add_nodes_from(data['student'], bipartite='student')
G.add_nodes_from(data['forum'], bipartite='forum')

# Add in each edge along with the date the edge was created
for r, d in data.iterrows():
    G.add_edge(d['student'], d['forum'], date=d['date'])

dayone  = datetime(2004,  5, 14)
lastday = datetime(2004, 10, 26)

'''
INSTRUCTIONS

*   Define a timedelta of 2 days using the timedelta() function and specifying an argument for the days parameter.
*   Inside the while loop:
    *   Filter edges such that they are within the sliding time window. Use a list comprehension to do this, where the output expression is (u, v, d), the iterable is G.edges(data=True), and there are two conditions: if d['date'] is >= curr_day and < than curr_day + td.
    *   Append the number of edges (use the len() function to help you calculate this) to n_posts.
    *   Increment curr_day by the time delta td.
*   Make a plot of n_posts using plt.plot().
'''

# Import necessary modules
from datetime import timedelta  
import matplotlib.pyplot as plt

# Define current day and timedelta of 2 days
curr_day = dayone
td = timedelta(days=2)

# Initialize an empty list of posts by day
n_posts = []
while curr_day < lastday:
    if curr_day.day == 1:
        print(curr_day) 
    # Filter edges such that they are within the sliding time window: edges
    edges = [(u, v, d) for u, v, d in G.edges(data=True) if d['date'] >= curr_day and d['date'] < curr_day + td]
    
    # Append number of edges to the n_posts list
    n_posts.append(len(edges))
    
    # Increment the curr_day by the time delta
    curr_day += td
    
# Create the plot
plt.plot(n_posts)
plt.xlabel('Days elapsed')
plt.ylabel('Number of posts')
plt.show()