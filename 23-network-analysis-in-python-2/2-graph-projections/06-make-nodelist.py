'''
Make nodelist

You're now going to practice converting graphs to pandas representation. If you have taken any of DataCamp's pandas courses, you will know that there is a DataFrame.to_csv('filename.csv') method that lets you save it as a CSV file, which is a human-readable version. The main concept we hope you take away from here is the process of converting a graph to a list of records.

Start by re-familiarizing yourself with the graph data structure by calling G.nodes(data=True)[0] in the IPython Shell to examine one node in the graph.
'''

import pickle
import networkx as nx
import pandas as pd

def get_nodes_from_partition(G, partition):
    return [n for n in G.nodes() if G.node[n]['bipartite'] == partition]


# Reading Graph v1 pickle data
with open('../datasets/american-revolution.p', 'rb') as f:
    G = pickle.load(f)

# Reading Graph v2 pickle data
#with open('../datasets/american-revolution.p2', 'rb') as f:
#    nodes, edges = pickle.load(f)
#    G = nx.Graph()
#    G.add_nodes_from(nodes)
#    G.add_edges_from(edges)

# Get the list of people and list of clubs from the graph: people_nodes, clubs_nodes
people = get_nodes_from_partition(G, 'people')
clubs = get_nodes_from_partition(G, 'clubs')

# Compute the people and clubs projections: G_people, G_clubs
G_people = nx.bipartite.projected_graph(G, people)
G_clubs = nx.bipartite.projected_graph(G, clubs)

'''
INSTRUCTIONS

*   Initialize an empty node list called nodelist.
*   Use a for loop to iterate over the nodes of the G_people. Inside the loop:
    *   Update the nodeinfo dictionary using the .update() method with d as the argument.
    *   Append the nodeinfo dictionary to nodelist.
*   Create a pandas DataFrame of the nodelist called node_df using the pd.DataFrame() function.
'''

# Initialize a list to store each edge as a record: nodelist
nodelist = []

for n, d in G_people.nodes(data=True):
    # nodeinfo stores one "record" of data as a dict
    nodeinfo = {'person': n} 
    
    # Update the nodeinfo dictionary 
    nodeinfo.update(d)
    
    # Append the nodeinfo to the node list
    nodelist.append(nodeinfo)
    
# Create a pandas DataFrame of the nodelist: node_df
node_df = pd.DataFrame(nodelist)

print(node_df.head())
