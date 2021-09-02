'''
Find shared membership: Transposition

As you may have observed, you lose the metadata from a graph when you go to a sparse matrix representation. You're now going to learn how to impute the metadata back so that you can learn more about shared membership.

The user_matrix you computed in the previous exercise has been preloaded into your workspace.

Here, the np.where() function will prove useful. This is what it does: given an array, say, a = [1, 5, 9, 5], if you want to get the indices where the value is equal to 5, you can use idxs = np.where(a == 5). This gives you back an array in a tuple, (array([1, 3]),). To access those indices, you would want to index into the tuple as idxs[0].
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

# Get the list of people and list of clubs from the graph: people_nodes, clubs_nodes
people_nodes = get_nodes_from_partition(G, 'people')
clubs_nodes = get_nodes_from_partition(G, 'clubs')

# Compute the biadjacency matrix: bi_matrix
bi_matrix = nx.bipartite.biadjacency_matrix(G, row_order=people_nodes, column_order=clubs_nodes)

# Compute the user-user projection: user_matrix
user_matrix = bi_matrix @ bi_matrix.T

'''
INSTRUCTIONS

*   Find out the names of people who were members of the most number of clubs.
    *   To do this, first compute diag by using the .diagonal() method on user_matrix.
    *   Then, using np.where(), select those indices where diag equals diag.max(). This returns a tuple: Make sure you access the relevant indices by indexing into the tuple with [0].
    *   Iterate over indices and print out each index i of people_nodes using the provided print() function.
*   Set the diagonal to zero and convert it to a coordinate matrix format. This has been done for you.
*   Find pairs of users who shared membership in the most number of clubs.
    *   Using np.where(), access the indices where users_coo.data equals users_coo.data.max().
    *   Iterate over indices and print out each index idx of people_node's users_coo.row and users_coo.col.
'''

import numpy as np

# Find out the names of people who were members of the most number of clubs
diag = user_matrix.diagonal()
indices = np.where(diag == diag.max())[0]  
print('Number of clubs: {0}'.format(diag.max()))
print('People with the most number of memberships:')
for i in indices:
    print('- {0}'.format(people_nodes[i]))

# Set the diagonal to zero and convert it to a coordinate matrix format
user_matrix.setdiag(0)
users_coo = user_matrix.tocoo()

# Find pairs of users who shared membership in the most number of clubs
indices = np.where(users_coo.data == users_coo.data.max())[0]
print('People with most number of shared memberships:')
for idx in indices:
    print('- {0}, {1}'.format(people_nodes[users_coo.row[idx]], people_nodes[users_coo.col[idx]]))  
