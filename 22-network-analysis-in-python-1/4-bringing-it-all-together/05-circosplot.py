'''
CircosPlot

Finally, you're going to make a CircosPlot of the network!
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

*   Make a CircosPlot of the network, again, with GitHub users sorted by their degree, and grouped and coloured by their 'grouping' key. To do this:
    *   Iterate over all the nodes in G, including the metadata (by specifying data=True).
    *   In each iteration of the loop, calculate the degree of each node n with nx.degree() and set its 'degree' attribute.
    *   Create the CircosPlot object c by specifying three parameters in addition to the graph G: the node_order, which is 'degree', the node_grouping and the node_color, which are both 'grouping'.
    *   Draw the CircosPlot object to the screen.
'''

# Import necessary modules
from nxviz import CircosPlot
import matplotlib.pyplot as plt 
 
# Iterate over all the nodes, including the metadata
for n, d in G.nodes(data=True):

    # Calculate the degree of each node: G.node[n]['degree']
    G.node[n]['degree'] = nx.degree(G, n)

# Create the CircosPlot object: c
c = CircosPlot(graph=G, node_order='degree', node_grouping='grouping', node_color='grouping')

# Draw the CircosPlot object to the screen
c.draw()
plt.show()