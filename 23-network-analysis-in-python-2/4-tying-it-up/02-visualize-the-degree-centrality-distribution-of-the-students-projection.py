'''
Visualize the degree centrality distribution of the students projection

In this exercise, you will visualize the degree centrality distribution of the students projection. This is a recap of two previous concepts you've learned: degree centralities, and projections.
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

*   Get the nodes of the 'student' partition into a list called student_nodes.
    *   Use a list comprehension to do this, iterating over all the nodes of G (including the metadata), and checking to see if the 'bipartite' keyword of d equals 'student'.
*   Create the students nodes projection as a graph called G_students. Use the nx.bipartite.projected_graph() function to do this. Be sure to specify the keyword argument nodes=student_nodes.
*   Calculate the degree centrality of G_students using nx.degree_centrality(). Store the result as dcs.
*   Plot the histogram of degree centrality values.
'''

# Import necessary modules
import matplotlib.pyplot as plt

# Get the student partition's nodes: student_nodes
student_nodes = [n for n, d in G.nodes(data=True) if d['bipartite'] == 'student']

# Create the students nodes projection as a graph: G_students
G_students = nx.bipartite.projected_graph(G, nodes=student_nodes)

# Calculate the degree centrality using nx.degree_centrality: dcs
dcs = nx.degree_centrality(G_students)

# Plot the histogram of degree centrality values
plt.hist(list(dcs.values()))
plt.yscale('log')
plt.show()