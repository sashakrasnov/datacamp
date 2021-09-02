'''
Degree centrality distribution of user nodes

In this exercise and the next one, you're going to do a final recap of material from the previous course. Your task is to plot the degree centrality distributions for each node partition in the bipartite version of the GitHub collaboration network. Here, you'll do this for the 'users' partition. In the next exercise, you'll do this for the 'projects' partition.

The function you wrote before, get_nodes_from_partition(), has been loaded for you. Just to remind you, the "degree centrality" is a measure of node importance, and the "degree centrality distribution" is the list of degree centrality scores for all nodes in the graph. A few exercises ago, when you made the circos plot, we computed the degree centralities for you. You'll now practice doing this yourself!
'''

import pickle
import matplotlib.pyplot as plt
import networkx as nx

from networkx import Graph

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

*   Import matplotlib.pyplot as plt.
*   Use your get_nodes_from_partition() function from the previous exercise to get a list called user_nodes corresponding to the 'users' nodes of G.
*   Using the nx.degree_centrality() function, compute the degree centralities for each node in G. Store the result as dcs.
*   Use a list comprehension to compute the degree centralities for each node in user_nodes. Store the result as user_dcs.
    *   Remember, dcs is a dictionary, in which the keys are the nodes. The relevant nodes here are contained in user_nodes. How can you use this information to obtain the degree centralities of the user nodes? Use n as your iterator variable.
*   Plot a histogram of the degree distribution of users, using plt.hist() and user_dcs.
'''

# Import matplotlib
import matplotlib.pyplot as plt

# Get the 'users' nodes: user_nodes
user_nodes = get_nodes_from_partition(G, 'users')

# Compute the degree centralities: dcs
dcs = nx.degree_centrality(G)

# Get the degree centralities for user_nodes: user_dcs
user_dcs = [dcs[n] for n in user_nodes]

# Plot the degree distribution of users_dcs
plt.yscale('log')
plt.hist(user_dcs, bins=20)
plt.show()
