'''
NetworkX betweenness centrality on a social network

Betweenness centrality is a node importance metric that uses information about the shortest paths in a network. It is defined as the fraction of all possible shortest paths between any pair of nodes that pass through the node.

NetworkX provides the nx.betweenness_centrality(G) function for computing the betweenness centrality of every node in a graph, and it returns a dictionary where the keys are the nodes and the values are their betweenness centrality measures.
'''

import pickle
import networkx as nx
import matplotlib.pyplot as plt

# Reading Graph v1 pickle data
#with open('../datasets/ego-twitter-subsampled.p', 'rb') as f:
#    T = pickle.load(f)

# Reading Graph v2 pickle data
with open('../datasets/ego-twitter-subsampled.p2', 'rb') as f:
    nodes, edges = pickle.load(f)
    T = nx.Graph()
    T.add_nodes_from(nodes)
    T.add_edges_from(edges)

'''
INSTRUCTIONS

*   Compute the betweenness centrality bet_cen of the nodes in the graph T.
*   Compute the degree centrality deg_cen of the nodes in the graph T.
*   Compare betweenness centrality to degree centrality by creating a scatterplot of the two, with list(bet_cen.values()) on the x-axis and list(deg_cen.values()) on the y-axis.
'''

# Compute the betweenness centrality of T: bet_cen
bet_cen = nx.betweenness_centrality(T)

# Compute the degree centrality of T: deg_cen
deg_cen = nx.degree_centrality(T)

# Create a scatter plot of betweenness centrality and degree centrality
plt.scatter(list(bet_cen.values()), list(deg_cen.values()))

# Display the plot
plt.show()