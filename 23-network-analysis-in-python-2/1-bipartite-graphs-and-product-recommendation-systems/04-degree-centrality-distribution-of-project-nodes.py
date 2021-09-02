'''
Degree centrality distribution of project nodes

Now it's time to plot the degree cenrality distribution for the 'projects' partition of G. The steps to do this are exactly the same as in the previous exercise. For your convenience, matplotlib.pyplot has been pre-imported as plt.

Go for it!
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

*   Obtain a list called project_nodes corresponding to the 'projects' nodes of G.
*   Using the nx.degree_centrality() function, compute the degree centralities for each node in G. Store the result as dcs.
*   Use a list comprehension to compute the degree centralities for each node in project_nodes. Store the result as project_dcs.
*   Plot a histogram of the degree distribution of projects, using plt.hist() and project_dcs.
'''

# Get the 'projects' nodes: project_nodes
project_nodes = get_nodes_from_partition(G, 'projects')

# Compute the degree centralities: dcs
dcs = nx.degree_centrality(G)

# Get the degree centralities for project_nodes: project_dcs
project_dcs = [dcs[n] for n in project_nodes]

# Plot the degree distribution of project_dcs
plt.yscale('log')
plt.hist(project_dcs, bins=20)
plt.show()
