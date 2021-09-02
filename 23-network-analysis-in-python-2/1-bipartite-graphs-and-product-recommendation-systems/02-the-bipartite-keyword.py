'''
The bipartite keyword

In the video, Eric introduced you to the 'bipartite' keyword. This keyword is part of a node's metadata dictionary, and can be assigned both when you add a node and after the node is added. Remember, though, that by definition, in a bipartite graph, a node cannot be connected to another node in the same partition.

Here, you're going to write a function that returns the nodes from a given partition in a bipartite graph. In this case, the relevant partitions of the Github bipartite graph you'll be working with are 'projects' and 'users'.
'''

import pickle
import matplotlib.pyplot as plt
import networkx as nx

from networkx import Graph

# Reading Graph v1 pickle data
with open('../datasets/github.p', 'rb') as f:
    G = pickle.load(f)

# Reading Graph v2 pickle data
#with open('../datasets/github.p2', 'rb') as f:
#    nodes, edges = pickle.load(f)
#    G = Graph()
#    G.add_nodes_from(nodes)
#    G.add_edges_from(edges)

'''
INSTRUCTIONS

*   Write a function called get_nodes_from_partition() which accepts two arguments - a bipartite graph G and a partition of G - and returns just the nodes from that partition.
    *   Iterate over all the nodes of G (not including the metadata) using a for loop.
    *   Access the 'bipartite' keyword of the current node's metadata dictionary. If it equals partition, append the current node to the list nodes.
*   Use your get_nodes_from_partition() function together with the len() function to:
    *   Print the number of nodes in the 'projects' partition of G.
    *   Print the number of nodes in the 'users' partition of G.
'''

# Define get_nodes_from_partition()
def get_nodes_from_partition(G, partition):
    # Initialize an empty list for nodes to be returned
    nodes = []
    # Iterate over each node in the graph G
    for n in G.nodes():
        # Check that the node belongs to the particular partition
        if G.node[n]['bipartite'] == partition:
            # If so, append it to the list of nodes
            nodes.append(n)
    return nodes

# Print the number of nodes in the 'projects' partition
print(len(get_nodes_from_partition(G, 'projects')))

# Print the number of nodes in the 'users' partition
print(len(get_nodes_from_partition(G, 'users')))