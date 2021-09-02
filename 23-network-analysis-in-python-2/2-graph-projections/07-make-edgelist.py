'''
Make edgelist

Now, you're going to apply the same ideas to making an edge list. Go forth and give it a shot!

As with the previous exercise, run G.edges(data=True)[0] in the IPython Shell to get a feel for the edge list data structure before proceeding.
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

*   Initialize a list called edgelist to store each edge as a record.
*   Use a for loop to iterate over the edges of G_people. Inside the loop:
    *   Initialize a dictionary called edgeinfo that shows edge information.
    *   Update the edgeinfo dictionary with the metadata dictionary d.
    *   Append the edgeinfo dictionary to edgelist.
*   Create a pandas DataFrame of the edgelist called edge_df.
'''

# Initialize a list to store each edge as a record: edgelist
edgelist = []

for n1, n2, d in G_people.edges(data=True):
    # Initialize a dictionary that shows edge information: edgeinfo
    edgeinfo = {'node1':n1, 'node2':n2}
    
    # Update the edgeinfo data with the edge metadata
    edgeinfo.update(d)
    
    # Append the edgeinfo to the edgelist
    edgelist.append(edgeinfo)
    
# Create a pandas DataFrame of the edgelist: edge_df
edge_df = pd.DataFrame(edgelist)

print(edge_df.head())
