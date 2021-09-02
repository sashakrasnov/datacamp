'''
Plotting using nxviz

Now, you're going to practice creating a CircosPlot using nxviz! As a bonus preview of what's coming up in the next video, there's a little segment on the bipartite keyword in this exercise!

Here, the degree centrality score of each node has been added to their metadata dictionary for you using the following code:

# Add the degree centrality score of each node to their metadata dictionary
|   dcs = nx.degree_centrality(G)
|   for n in G.nodes():
|       G.node[n]['centrality'] = dcs[n]

If you want a refresher on degree centrality, check out the relevant video from the previous course - it is a way of computing the importance of a node!

CircosPlot has been pre-imported for you from nxviz, along with NetworkX (as nx) and matplotlib.pyplot (as plt).
'''

import pickle
import matplotlib.pyplot as plt
import networkx as nx

from networkx import Graph
from nxviz import CircosPlot

# Reading Graph v1 pickle data
with open('../datasets/github_subgraph.p', 'rb') as f:
    G = pickle.load(f)

# Reading Graph v2 pickle data
#with open('../datasets/github_subgraph.p2', 'rb') as f:
#    nodes, edges = pickle.load(f)
#    G = Graph()
#    G.add_nodes_from(nodes)
#    G.add_edges_from(edges)

dcs = nx.degree_centrality(G)

for n in G.nodes():
    G.node[n]['centrality'] = dcs[n]

'''
INSTRUCTIONS

*   Plot the network G using a circos plot. To do this:
    *   Create a CircosPlot object called c using the CircosPlot() function.
    *   Use the node_color and node_grouping parameters of CircosPlot() to color and group the nodes by the keyword 'bipartite'
    *   Use the node_order parameter of CircosPlot() to order the nodes by 'centrality'.
*   Draw c to the screen and display it.
'''

# Create the CircosPlot object: c
c = CircosPlot(graph=G, node_color='bipartite', node_grouping='bipartite', node_order='centrality')

# Draw c to the screen
c.draw()

# Display the plot
plt.show()

'''
Migrating from networkx v1 to v2
>>> # in v1.x
>>> pickle.dump([G.nodes(data=True), G.edges(data=True)], file)  # doctest: +SKIP
>>> # then in v2.x
>>> nodes, edges = pickle.load(file)  # doctest: +SKIP
>>> G = nx.Graph()  # doctest: +SKIP
>>> G.add_nodes_from(nodes)  # doctest: +SKIP
>>> G.add_edges_from(edges)  # doctest: +SKIP
'''