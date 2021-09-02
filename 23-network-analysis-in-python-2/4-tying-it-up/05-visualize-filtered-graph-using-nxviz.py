'''
Visualize filtered graph using nxviz

Here, you'll visualize the filtered graph using a CircosPlot. The CircosPlot is a natural choice for this visualization, as you can use node grouping and coloring to visualize the partitions, while the circular layout preserves the aesthetics of the visualization.
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

# Get the forums partition's nodes: forum_nodes
forum_nodes = [n for n, d in G.nodes(data=True) if d['bipartite'] == 'forum']

from datetime import datetime

# Instantiate a new graph: G_sub
G_sub = nx.Graph()

# Add nodes from the original graph
G_sub.add_nodes_from(G.nodes(data=True))

# Add edges using a list comprehension with one conditional on the edge dates, that the date of the edge is earlier than 2004-05-16.
G_sub.add_edges_from([(u, v, d) for u, v, d in G.edges(data=True) if d['date'] < datetime(2004, 5, 16)])

'''
INSTRUCTIONS

*   Compute degree centrality scores of each node using the bipartite module degree centralities, but based on the degree centrality in the original graph.
    *   Use the nx.bipartite.degree_centrality() function for this, with the arguments G and nodes=forum_nodes.
*   Create a new CircosPlot object with nodes colored and grouped (parameters node_color and node_grouping) by their partition label ('bipartite'), and ordered (parameter node_order) by their degree centrality ('dc')
*   Plot the CircosPlot to screen.
'''

# Import necessary modules
from nxviz import CircosPlot
import matplotlib.pyplot as plt

# Compute degree centrality scores of each node
dcs = nx.bipartite.degree_centrality(G, nodes=forum_nodes)
for n, d in G_sub.nodes(data=True):
    G_sub.node[n]['dc'] = dcs[n]

# Create the CircosPlot object: c
c = CircosPlot(graph=G_sub, node_color='bipartite', node_grouping='bipartite', node_order='dc')

# Draw c to screen
c.draw()

# Display the plot
plt.show() 

