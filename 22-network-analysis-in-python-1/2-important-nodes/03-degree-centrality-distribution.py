'''
Degree centrality distribution

The degree of a node is the number of neighbors that it has. The degree centrality is the number of neighbors divided by all possible neighbors that it could have. Depending on whether self-loops are allowed, the set of possible neighbors a node could have could also include the node itself.

The nx.degree_centrality(G) function returns a dictionary, where the keys are the nodes and the values are their degree centrality values.

The degree distribution degrees you computed in the previous exercise using the list comprehension has been pre-loaded.
'''

import pickle
import networkx as nx

# Reading Graph v1 pickle data
#with open('../datasets/ego-twitter.p', 'rb') as f:
#    T = pickle.load(f)

# Reading Graph v2 pickle data
with open('../datasets/ego-twitter.p2', 'rb') as f:
    nodes, edges = pickle.load(f)
    T = nx.Graph()
    T.add_nodes_from(nodes)
    T.add_edges_from(edges)

# Compute the degree of every node: degrees
#degrees = [len(T.neighbors(n)) for n in T.nodes()]
degrees = [T.neighbors(n).__sizeof__() for n in T.nodes()]

'''
INSTRUCTIONS

*   Compute the degree centrality of the Twitter network T.
*   Using plt.hist(), plot a histogram of the degree centrality distribution of T. This can be accessed using list(deg_cent.values()).
*   Plot a histogram of the degree distribution degrees of T. This is the same list you computed in the last exercise.
*   Create a scatter plot with degrees on the x-axis and the degree centrality distribution list(deg_cent.values()) on the y-axis.
'''

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Compute the degree centrality of the Twitter network: deg_cent
deg_cent = nx.degree_centrality(T)

# Plot a histogram of the degree centrality distribution of the graph.
plt.figure()
plt.hist(list(deg_cent.values()))
plt.show()

# Plot a histogram of the degree distribution of the graph
plt.figure()
plt.hist(degrees)
plt.show()

# Plot a scatter plot of the centrality distribution and the degree distribution
plt.figure()
plt.scatter(degrees, list(deg_cent.values()))
plt.show()