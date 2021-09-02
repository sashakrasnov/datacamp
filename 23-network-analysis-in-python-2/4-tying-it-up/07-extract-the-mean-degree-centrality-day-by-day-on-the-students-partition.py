'''
Extract the mean degree centrality day-by-day on the students partition

Here, you're going to see if the mean degree centrality over all nodes is correlated with the number of edges that are plotted over time. There might not necessarily be a strong correlation, and you'll take a look to see if that's the case.
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

# Get the student partition's nodes: student_nodes
student_nodes = [n for n, d in G.nodes(data=True) if d['bipartite'] == 'student']

'''
INSTRUCTIONS

*   Instantiate a new graph called G_sub containing a subset of edges.
*   Add nodes from G, including the node metadata.
*   Add in edges that fulfill the criteria, using the .add_edges_from() method.
*   Get the students projection G_student_sub using the nx.bipartite.projected_graph() function.
*   Compute the degree centrality of the students projection using nx.degree_centrality() (don't use the bipartite version).
*   Append the mean degree centrality to the list mean_dcs. Be sure to convert dc.values() to a list first.
*   Hit 'Submit Answer' to view the plot!
'''

from datetime import timedelta
import numpy as np
import matplotlib.pyplot as plt

# Initialize a new list: mean_dcs
mean_dcs = []
curr_day = dayone
td = timedelta(days=2)

while curr_day < lastday:
    if curr_day.day == 1:
        print(curr_day)  
    # Instantiate a new graph containing a subset of edges: G_sub
    G_sub = nx.Graph()
    # Add nodes from G
    G_sub.add_nodes_from(G.nodes(data=True))
    # Add in edges that fulfill the criteria
    G_sub.add_edges_from([(u, v, d) for u, v, d in G.edges(data=True) if d['date'] >= curr_day and d['date'] < curr_day + td])
    
    # Get the students projection
    G_student_sub = nx.bipartite.projected_graph(G_sub, nodes=student_nodes)
    # Compute the degree centrality of the students projection
    dc = nx.degree_centrality(G_student_sub)
    # Append mean degree centrality to the list mean_dcs
    mean_dcs.append(np.mean(list(dc.values())))
    # Increment the time
    curr_day += td
    
plt.plot(mean_dcs)
plt.xlabel('Time elapsed')
plt.ylabel('Degree centrality.')
plt.show()