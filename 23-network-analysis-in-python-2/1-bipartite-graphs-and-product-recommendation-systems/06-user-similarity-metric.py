'''
User similarity metric

Having written a function to calculate the set of nodes that are shared between two nodes, you're now going to write a function to compute a metric of similarity between two users: the number of projects shared between two users divided by the total number of nodes in the other partition. This can then be used to find users that are similar to one another.
'''

import pickle
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

'''
INSTRUCTIONS

*   Complete the user_similarity() function to calculate the similarity between user1 and user2.
    *   Use assert statements to check that user1 and user2 belong to the 'users' partition.
    *   Use your shared_partition_nodes() function from the previous exercise to get the set of nodes shared between the two users user1 and user2.
    *   Return the fraction of nodes in the projects partition. That is, divide the number of shared_nodes by the total number of nodes in the 'projects' partition.
*   Compute the similarity score between users 'u4560' and 'u1880'. To do this:
    *   First obtain the nodes in the 'projects' partition using your get_nodes_from_partition() function.
    *   Then use your user_similarity() function to compute the score.
'''

def user_similarity(G, user1, user2, proj_nodes):
    # Check that the nodes belong to the 'users' partition
    assert G.node[user1]['bipartite'] == 'users'
    assert G.node[user2]['bipartite'] == 'users'

    # Get the set of nodes shared between the two users
    shared_nodes = shared_partition_nodes(G, user1, user2)

    # Return the fraction of nodes in the projects partition
    return len(shared_nodes) / len(proj_nodes)

# Compute the similarity score between users 'u4560' and 'u1880'
project_nodes = get_nodes_from_partition(G, 'projects')
similarity_score = user_similarity(G, 'u4560', 'u1880', project_nodes)

print(similarity_score)
