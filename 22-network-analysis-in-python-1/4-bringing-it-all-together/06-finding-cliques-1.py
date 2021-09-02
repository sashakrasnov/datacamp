'''
Finding cliques (I)

You're now going to practice finding cliques in G. Recall that cliques are "groups of nodes that are fully connected to one another", while a maximal clique is a clique that cannot be extended by adding another node in the graph.
'''

import pickle
import networkx as nx

# Reading Graph v1 pickle data
#with open('../datasets/github_users_subsampled.p', 'rb') as f:
#    G = pickle.load(f)

# Reading Graph v2 pickle data
with open('../datasets/github_users_subsampled.p2', 'rb') as f:
    nodes, edges = pickle.load(f)
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

'''
INSTRUCTIONS

*   Count the number of maximal cliques present in the graph and print it.
*   Use the nx.find_cliques() function of G to find the maximal cliques.
*   The nx.find_cliques() function returns a generator object. To count the number of maximal cliques, you need to first convert it to a list with list() and then use the len() function. Place this inside a print() function to print it.
'''

# Calculate the maximal cliques in G: cliques
cliques = nx.find_cliques(G)

# Count and print the number of maximal cliques in G
print(len(list(cliques)))