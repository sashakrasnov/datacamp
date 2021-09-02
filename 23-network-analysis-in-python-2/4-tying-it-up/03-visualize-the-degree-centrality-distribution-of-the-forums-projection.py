'''
Visualize the degree centrality distribution of the forums projection

This exercise is also to reinforce the concepts of degree centrality and projections. This time round, you'll plot the degree centrality distribution for the 'forum' projection. Follow the same steps as in the previous exercise!
'''

import pandas as pd
import networkx as nx

data = pd.read_csv('../datasets/student-forum-subsampled.csv', index_col=[0], parse_dates=[3])

# Instantiate a new Graph: G
G = nx.Graph()

# Add nodes from each of the partitions
G.add_nodes_from(data['student'], bipartite='student')
G.add_nodes_from(data['forum'], bipartite='forum')

# Add in each edge along with the date the edge was created
for r, d in data.iterrows():
    G.add_edge(d['student'], d['forum'], date=d['date'])

'''
INSTRUCTIONS

*   Get the nodes of the 'forum' partition into a list called forum_nodes.
*   Create the forums nodes projection as a graph called G_forum.
*   Calculate the degree centrality of G_forum using nx.degree_centrality(). Store the result as dcs.
*   Plot the histogram of degree centrality values.
'''

# Import necessary modules
import matplotlib.pyplot as plt 

# Get the forums partition's nodes: forum_nodes
forum_nodes = [n for n, d in G.nodes(data=True) if d['bipartite'] == 'forum']

# Create the forum nodes projection as a graph: G_forum
G_forum = nx.bipartite.projected_graph(G, nodes=forum_nodes)

# Calculate the degree centrality using nx.degree_centrality: dcs
dcs = nx.degree_centrality(G_forum)

# Plot the histogram of degree centrality values
plt.hist(list(dcs.values()))
plt.yscale('log')
plt.show()