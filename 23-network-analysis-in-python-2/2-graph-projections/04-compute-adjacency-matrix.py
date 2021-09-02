'''
Compute adjacency matrix

Now, you'll get some practice using matrices and sparse matrix multiplication to compute projections! In this exercise, you'll use the matrix multiplication operator @ that was introduced in Python 3.5.

You'll continue working with the American Revolution graph. The two partitions of interest here are 'people' and 'clubs'.
'''

import pickle
import networkx as nx

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


# Reading Graph v1 pickle data
with open('../datasets/american-revolution.p', 'rb') as f:
    G = pickle.load(f)

# Reading Graph v2 pickle data
#with open('../datasets/american-revolution.p2', 'rb') as f:
#    nodes, edges = pickle.load(f)
#    G = nx.Graph()
#    G.add_nodes_from(nodes)
#    G.add_edges_from(edges)

'''
INSTRUCTIONS

*   Get the list of people and list of clubs from the graph G using the get_nodes_from_partition() function that you defined in the previous chapter. This function accepts two parameters: A graph, and a partition.
*   Compute the biadjacency matrix using nx.bipartite.biadjacency_matrix(), setting the row_order parameter to people_nodes and the column_order parameter to clubs_nodes. Remember to also pass in the graph G.
*   Compute the user-user projection by multiplying (with the @ operator) the biadjacency matrix bi_matrix by its transposition, bi_matrix.T.
'''

# Get the list of people and list of clubs from the graph: people_nodes, clubs_nodes
people_nodes = get_nodes_from_partition(G, 'people')
clubs_nodes = get_nodes_from_partition(G, 'clubs')

# Compute the biadjacency matrix: bi_matrix
bi_matrix = nx.bipartite.biadjacency_matrix(G, row_order=people_nodes, column_order=clubs_nodes)

# Compute the user-user projection: user_matrix
user_matrix = bi_matrix @ bi_matrix.T

print(user_matrix)