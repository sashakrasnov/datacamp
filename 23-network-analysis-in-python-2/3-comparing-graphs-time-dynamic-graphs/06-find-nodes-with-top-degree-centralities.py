'''
Find nodes with top degree centralities

In this exercise, you'll take a deeper dive to see whether there's anything interesting about the most connected students in the network. First off, you'll find the cluster of students that have the highest degree centralities. This result will be saved for the next plotting exercise.
'''

import pandas as pd
import networkx as nx
import numpy as np

def ECDF(vals):
    n = len(vals)
    x = sorted(vals)
    y = np.arange(1, n+1) / n
    
    return x, y


data = pd.read_csv('../datasets/college_msg_preprocessed.csv')

months = range(4, 11)

# Initialize an empty list: Gs
Gs = [] 
for month in months:
    # Instantiate a new undirected graph: G
    G = nx.Graph()
    
    # Add in all nodes that have ever shown up to the graph
    G.add_nodes_from(data['sender'])
    G.add_nodes_from(data['recipient'])
    
    # Filter the DataFrame so that there's only the given month
    df_filtered = data[data['month'] == month]
    
    # Add edges from filtered DataFrame
    G.add_edges_from(zip(df_filtered['sender'],df_filtered['recipient']))
    
    # Append G to the list of graphs
    Gs.append(G)

G = Gs[1]

'''
INSTRUCTIONS

*   Get the top 5 unique degree centrality scores. To do this, use the sorted() function, in which the first argument is the set of degree centrality values of G (because you want unique degree centralities), and the second argument is reverse=True, to ensure that it is sorted in descending order. To limit the results to the top 5 scores, add in appropriate slicing to the end of the statement. Also, remember to use .values() on the returned degree centrality results!
*   Create list of nodes that have the top 5 highest overall degree centralities. To do this:
    *   Iterate over the dictionary of degree centrality scores using the .items() method on nx.degree_centrality(G).
    *   If dc is in top_dcs, then append the node n to the top_connected list.
*   Print the number of nodes that share the top 5 degree centrality scores (top_connected) using len().
'''

# Get the top 5 unique degree centrality scores: top_dcs
top_dcs = sorted(set(nx.degree_centrality(G).values()), reverse=True)[:5]

# Create list of nodes that have the top 5 highest overall degree centralities
top_connected = []
for n, dc in nx.degree_centrality(G).items():
    if dc in top_dcs:
        top_connected.append(n)
        
# Print the number of nodes that share the top 5 degree centrality scores
print(len(top_connected))
