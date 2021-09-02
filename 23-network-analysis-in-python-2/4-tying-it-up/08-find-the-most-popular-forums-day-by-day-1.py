'''
Find the most popular forums day-by-day: I

Great stuff! You're onto the final two exercises - which are really just one long exercise. These will be a good memory workout for your Python programming skills!

We're going to see how many forums took the title of "the most popular forum" on any given time window.
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

# Get the forums partition's nodes: forum_nodes
forum_nodes = [n for n, d in G.nodes(data=True) if d['bipartite'] == 'forum']

dayone  = datetime(2004,  5, 14)
lastday = datetime(2004, 10, 26)

'''
INSTRUCTIONS

*   Instantiate a list to hold the list of most popular forums by day called most_popular_forums.
*   Instantiate a list to hold the degree centrality scores of the most popular forums called highest_dcs.
*   Instantiate new graph called G_sub and add in the nodes from the original graph G using the .add_nodes_from() method.
*   Add in edges from the original graph G that fulfill the criteria (which are exactly the same as in the previous exercise).
'''

from datetime import timedelta
import numpy as np

# Instantiate a list to hold the list of most popular forums by day: most_popular_forums
most_popular_forums = []

# Instantiate a list to hold the degree centrality scores of the most popular forums: highest_dcs
highest_dcs = []
curr_day = dayone  
td = timedelta(days=1)  

while curr_day < lastday:  
    if curr_day.day == 1: 
        print(curr_day) 
    # Instantiate new graph: G_sub
    G_sub = nx.Graph()
    
    # Add in nodes from original graph G
    G_sub.add_nodes_from(G.nodes(data=True))
    
    # Add in edges from the original graph G that fulfill the criteria
    G_sub.add_edges_from([(u, v, d) for u, v, d in G.edges(data=True) if d['date'] >= curr_day and d['date'] < curr_day + td])
    
    # CODE CONTINUES ON NEXT EXERCISE
    curr_day += td
