'''
Computing projection

It's now time to to try your hand at computing the projection of a bipartite graph to the nodes on one of its partitions. This will help you gain practice with converting between a bipartite version of a graph and its unipartite projections. Remember from the video that the "projection" of a graph onto one of its partitions is the connectivity of the nodes in that partition conditioned on connections to nodes on the other partition. Made more concretely, you can think of the "connectivity of customers based on shared purchases".

To help you get started, here's a hint on list comprehensions. List comprehensions can include conditions, so if you want to filter a graph for a certain type of node, you can do: [n for n, d in G.nodes(data=True) if d['key'] == 'some_value'].
'''

import pickle
import networkx as nx

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

*   Prepare the people nodelist using a list comprehension. If the 'bipartite' keyword of a node n in G equals 'people', then that node should be part of the nodelist.
*   Prepare the clubs nodelist by iterating over the nodes of G, including the metadata. Here, note that you have to check if the 'bipartite' keyword of the metadata dictionary d equals 'clubs'. Note: This is simply an alternate way of creating the nodelist. You do not have to iterate over the metadata - you can follow the same approach you used to create the people nodelist, simply checking for 'clubs' instead. We're asking you to use the other approach here so you get practice with both.
*   Use nx.bipartite.projected_graph() to compute the people and clubs projections. Store the results as peopleG and clubsG.
    *   This function takes in two arguments: The graph G, and the nodelist.
'''

# Prepare the nodelists needed for computing projections: people, clubs
people = [n for n in G.nodes() if G.node[n]['bipartite'] == 'people']
clubs = [n for n, d in G.nodes(data=True) if d['bipartite'] == 'clubs']

# Compute the people and clubs projections: peopleG, clubsG
peopleG = nx.bipartite.projected_graph(G, people)
clubsG = nx.bipartite.projected_graph(G, clubs)