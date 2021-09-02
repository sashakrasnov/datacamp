'''
Find the most popular forums day-by-day: II

Great work with the previous exercise - you had written code that created the time-series graph list. Now, you're going to finish that exercise - that is, you'll find out how many forums had the most popular forum score on a per-day basis!

One of the things you will be doing here is a "dictionary comprehension" to filter a dictionary. It is very similar to a list comprehension to filter a list, except the syntax looks like: {key: val for key, val in dict.items() if ...}. Keep that in mind!
'''

import pandas as pd
import networkx as nx
import numpy as np

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

from datetime import datetime

dayone  = datetime(2004,  5, 14)
lastday = datetime(2004, 10, 26)

'''
INSTRUCTIONS

*   Get the degree centrality using nx.bipartite.degree_centrality(), with G_sub and forum_nodes as arguments.
*   Filter the dictionary such that there's only forum degree centralities. The key: val pair in the output expression should be n, dc. Iterate over dc.items() and check if n is in forum_nodes.
*   Identify the most popular forum(s) - should be of highest degree centrality (max(forum_dcs.values())) and its DC value should not be zero.
*   Append the highest dc values to highest_dcs.
*   Create the plots!
    *   Use a list comprehension for the first plot, in which you iterate over most_popular_forums (which is a list of lists) using forums as your iterator variable. The output expression should be the number of most popular forums, calculated using len().
    *   For the second plot, use highest_dcs and plt.plot() to visualize the top degree centrality score.
'''

# Import necessary modules
from datetime import timedelta
import matplotlib.pyplot as plt

most_popular_forums = []
highest_dcs = []
curr_day = dayone 
td = timedelta(days=1)  

while curr_day < lastday:  
    if curr_day.day == 1:  
        print(curr_day)  
    G_sub = nx.Graph()
    G_sub.add_nodes_from(G.nodes(data=True))   
    G_sub.add_edges_from([(u, v, d) for u, v, d in G.edges(data=True) if d['date'] >= curr_day and d['date'] < curr_day + td])
    
    # Get the degree centrality 
    dc = nx.bipartite.degree_centrality(G_sub, nodes=forum_nodes)
    # Filter the dictionary such that there's only forum degree centralities
    forum_dcs = {n:dc for n, dc in dc.items() if n in forum_nodes}
    # Identify the most popular forum(s) 
    most_popular_forum = [n for n, dc in forum_dcs.items() if dc == max(forum_dcs.values()) and dc != 0] 
    most_popular_forums.append(most_popular_forum) 
    # Store the highest dc values in highest_dcs
    highest_dcs.append(max(forum_dcs.values()))
    
    curr_day += td  
    
plt.figure(1) 
plt.plot([len(forums) for forums in most_popular_forums], color='blue', label='Forums')
plt.ylabel('Number of Most Popular Forums')
plt.show()

plt.figure(2)
plt.plot(highest_dcs, color='orange', label='DC Score')
plt.ylabel('Top Degree Centrality Score')
plt.show()
