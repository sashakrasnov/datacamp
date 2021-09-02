'''
Characterizing the network (II)

The last exercise was on degree centrality; this time round, let's recall betweenness centrality!

A small note: if executed correctly, this exercise may need about 5 seconds to execute.
'''

import pickle

from networkx import Graph

# Reading Graph v1 pickle data
#with open('../datasets/github_users_subsampled.p', 'rb') as f:
#    G = pickle.load(f)

# Reading Graph v2 pickle data
with open('../datasets/github_users_subsampled.p2', 'rb') as f:
    nodes, edges = pickle.load(f)
    G = Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

'''
INSTRUCTIONS

*   Plot the betweenness centrality distribution of the GitHub collaboration network. You have to follow exactly the same four steps as in the previous exercise, substituting nx.betweenness_centrality() in place of nx.degree_centrality().
'''

# Import necessary modules
import matplotlib.pyplot as plt
import networkx as nx

# Plot the degree distribution of the GitHub collaboration network
plt.hist(list(nx.betweenness_centrality(G).values()))
plt.show()
