'''
Find similar users

You're now going to build upon what you've learned so far to write a function called most_similar_users() that finds the users most similar to another given user.

The beginnings of this function have been written for you. A list of nodes, user_nodes has been created, which contains all of the users except the given user that has been passed into the function. Your task is to complete the function such that it finds the users most similar to this given user. You'll make use of your user_similarity() function from the previous exercise to help do this.

A dictionary called similarities has been setup, in which the keys are the scores and the list of values are the nodes. If you've never seen a defaultdict before, don't worry - you'll learn more about it in Chapter 3! It functions exactly like a regular Python dictionary.
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


def user_similarity(G, user1, user2, proj_nodes):
    # Check that the nodes belong to the 'users' partition
    assert G.node[user1]['bipartite'] == 'users'
    assert G.node[user2]['bipartite'] == 'users'

    # Get the set of nodes shared between the two users
    shared_nodes = shared_partition_nodes(G, user1, user2)

    # Return the fraction of nodes in the projects partition
    return len(shared_nodes) / len(proj_nodes)

'''
INSTRUCTIONS

*   Iterate over user_nodes and compute the similarity between user and each user_node (n) using your user_similarity() function. Store the result as similarity.
*   Append the score and node to the similarities dictionary. The key is the score - similarity - and the value is the node - n.
*   Compute the maximum similarity score. To do this, first access the keys (which contain the scores) of similarities using the .keys() method and then use the max() function. Store the result as max_similarity.
*   Return the list of users that share maximal similarity. This list of users is the value of the max_similarity key of similarities.
*   Use your most_similar_users() function to print the list of users most similar to the user 'u4560'.
'''

from collections import defaultdict

def most_similar_users(G, user, user_nodes, proj_nodes):
    # Data checks
    assert G.node[user]['bipartite'] == 'users'

    # Get other nodes from user partition
    user_nodes = set(user_nodes)
    user_nodes.remove(user)

    # Create the dictionary: similarities
    similarities = defaultdict(list)
    for n in user_nodes:
        similarity = user_similarity(G, user, n, proj_nodes)
        similarities[similarity].append(n)

    # Compute maximum similarity score: max_similarity
    max_similarity = max(similarities.keys())

    # Return list of users that share maximal similarity
    return similarities[max_similarity]

user_nodes = get_nodes_from_partition(G, 'users')
project_nodes = get_nodes_from_partition(G, 'projects')

print(most_similar_users(G, 'u4560', user_nodes, project_nodes))
