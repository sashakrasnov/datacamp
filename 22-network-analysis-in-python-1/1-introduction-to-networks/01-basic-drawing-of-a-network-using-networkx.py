'''
Basic drawing of a network using NetworkX

NetworkX provides some basic drawing functionality that works for small graphs. We have selected a subset of nodes from the graph for you to practice using NetworkX's drawing facilities. It has been pre-loaded as T_sub.
'''

from pickle import load
from networkx import Graph

# Reading Graph v1 pickle data
#with open('../datasets/ego-twitter-subsampled.p', 'rb') as f:
#    T_sub = load(f)

# Reading Graph v2 pickle data
with open('../datasets/ego-twitter-subsampled.p2', 'rb') as f:
    nodes, edges = load(f)
    T_sub = Graph()
    T_sub.add_nodes_from(nodes)
    T_sub.add_edges_from(edges)

'''
INSTRUCTIONS

*   Import matplotlib.pyplot as plt and networkx as nx.
*   Draw T_sub to the screen by using the nx.draw() function, and don't forget to also use plt.show() to display it.
'''

# Import necessary modules
import networkx as nx
import matplotlib.pyplot as plt

# Draw the graph to screen
nx.draw(T_sub)
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