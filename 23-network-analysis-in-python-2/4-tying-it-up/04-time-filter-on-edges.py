'''
Time filter on edges

You're now going to practice filtering the graph using a conditional as applied to the edges. This will help you gain practice and become comfortable with list comprehensions that contain conditionals.

To help you with the exercises, remember that you can import datetime objects from the datetime module. On the graph, the metadata has a date key that is paired with a datetime object as a value.
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

*   Instantiate a new graph called G_sub.
*   Add nodes from the original graph (including the node metadata), using the .add_nodes_from() method.
*   Add edges using a list comprehension with one conditional on the edge dates, that the date of the edge is earlier than 2004-05-16. To do this:
    *   Use the .add_edges_from() method with a list comprehension as the argument.
    *   The output expression of the list comprehension is (u, v, d). Iterate over all the edges of G and check whether d['date'] is less than datetime(2004, 5, 16).
'''

from datetime import datetime

# Instantiate a new graph: G_sub
G_sub = nx.Graph()

# Add nodes from the original graph
G_sub.add_nodes_from(G.nodes(data=True))

# Add edges using a list comprehension with one conditional on the edge dates, that the date of the edge is earlier than 2004-05-16.
G_sub.add_edges_from([(u, v, d) for u, v, d in G.edges(data=True) if d['date'] < datetime(2004, 5, 16)])