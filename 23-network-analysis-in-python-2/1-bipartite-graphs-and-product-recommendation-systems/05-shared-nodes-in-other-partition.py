'''
Shared nodes in other partition

In order to build up your concept of recommendation systems, we are going to start with the fundamentals. The focus here is on computing user similarity in bipartite graphs.

Your job is to write a function that takes in two nodes, and returns the set of repository nodes that are shared between the two user nodes.

You'll find the following methods and functions helpful in this exercise - .neighbors(), set(), and .intersection() - besides, of course, the shared_partition_nodes function that you will define!
'''

import pickle
import networkx as nx

from networkx import Graph

# Reading Graph v1 pickle data
with open('../datasets/github_subgraph.p', 'rb') as f:
    G = pickle.load(f)

# Reading Graph v2 pickle data
#with open('../datasets/github_subgraph.p2', 'rb') as f:
#    nodes, edges = pickle.load(f)
#    G = Graph()
#    G.add_nodes_from(nodes)
#    G.add_edges_from(edges)

'''
INSTRUCTIONS

*   Write a function called shared_partition_nodes() that takes in 3 arguments - a graph G, node1, and node2 - and returns the set of nodes that are shared between node1 and node2.
    *   Check that node1 and node2 belong to the same partition using an assert statement and the 'bipartite' keyword.
    *   Obtain the neighbors of node1 and store them as nbrs1.
    *   Obtain the neighbors of node2 and store them as nbrs2.
*   Compute the overlap between nbrs1 and nbrs2 using the set .intersection() method.
*   Print the number of shared repositories between users 'u7909' and 'u2148' using your shared_partition_nodes() function together with the len() function.
'''

def shared_partition_nodes(G, node1, node2):
    # Check that the nodes belong to the same partition
    assert G.node[node1]['bipartite'] == G.node[node2]['bipartite']

    # Get neighbors of node 1: nbrs1
    nbrs1 = G.neighbors(node1)
    # Get neighbors of node 2: nbrs2
    nbrs2 = G.neighbors(node2)

    # Compute the overlap using set intersections
    overlap = set(nbrs1).intersection(nbrs2)
    return overlap

# Print the number of shared repositories between users 'u7909' and 'u2148'
print(len(shared_partition_nodes(G, 'u7909', 'u2148')))

