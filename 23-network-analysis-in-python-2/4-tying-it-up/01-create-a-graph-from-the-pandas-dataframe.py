'''
Create a graph from the pandas DataFrame

Let's start by creating a graph from a pandas DataFrame. In this exercise, you'll create a new bipartite graph by looping over the edgelist (which is a DataFrame object).

For simplicity's sake, in this graph construction procedure, any edge between a student and a forum node will be the 'last' edge (in time) that a student posted to a forum over the entire time span of the dataset, though there are ways to get around this.

Additionally, to shorten the runtime of the exercise, we have provided a sub-sampled version of the edge list as data. Explore it in the IPython Shell to familiarize yourself with it.
'''

import pandas as pd

data = pd.read_csv('../datasets/student-forum-subsampled.csv', index_col=[0], parse_dates=[3])

'''
INSTRUCTIONS

*   Instantiate a new Graph called G.
*   Add nodes from each of the partitions. Use the .add_nodes_from() method to do this. The two partitions are 'student' and 'forum'. To add nodes from the 'student' partition, for example, the arguments to .add_nodes_from() would be data['student'] and bipartite='student'.
*   Add in each edge along with the date the edge was created. To do this, use the .add_edge() method inside the loop, with the arguments d['student'], d['forum'], and date=d['date'].
'''

import networkx as nx

# Instantiate a new Graph: G
G = nx.Graph()

# Add nodes from each of the partitions
G.add_nodes_from(data['student'], bipartite='student')
G.add_nodes_from(data['forum'], bipartite='forum')

# Add in each edge along with the date the edge was created
for r, d in data.iterrows():
    G.add_edge(d['student'], d['forum'], date=d['date'])