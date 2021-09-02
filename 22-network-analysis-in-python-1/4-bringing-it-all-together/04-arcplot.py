'''
ArcPlot

Next up, let's use the ArcPlot to visualize the network. You're going to practice sorting the nodes in the graph as well.

Note: this exercise may take about 4-7 seconds to execute if done correctly.
'''

import pickle
import networkx as nx

# Reading Graph v1 pickle data
#with open('../datasets/github_users_subsampled.p', 'rb') as f:
#    G = pickle.load(f)

# Reading Graph v2 pickle data
with open('../datasets/github_users_subsampled.p2', 'rb') as f:
    nodes, edges = pickle.load(f)
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

'''
Instructions

*   Make an ArcPlot of the GitHub collaboration network, with authors sorted by degree. To do this:
    *   Iterate over all the nodes in G, including the metadata (by specifying data=True).
    *   In each iteration of the loop, calculate the degree of each node n with nx.degree() and set its 'degree' attribute. nx.degree() accepts two arguments: A graph and a node.
    *   Create the ArcPlot object a by specifying two parameters: the graph, which is G, and the node_order, which is 'degree', so that the nodes are sorted.
    *   Draw the ArcPlot object to the screen.
'''

# Import necessary modules
from nxviz.plots import ArcPlot
import matplotlib.pyplot as plt

# Iterate over all the nodes in G, including the metadata
for n, d in G.nodes(data=True):

    # Calculate the degree of each node: G.node[n]['degree']
    G.node[n]['degree'] = nx.degree(G, n)
    
# Create the ArcPlot object: a
a = ArcPlot(graph=G, node_order='degree')

# Draw the ArcPlot to the screen
a.draw()
plt.show()