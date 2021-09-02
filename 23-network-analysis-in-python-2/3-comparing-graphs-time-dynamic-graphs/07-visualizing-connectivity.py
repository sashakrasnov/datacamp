'''
Visualizing connectivity

Here, you're going to visualize how the connectivity of the top connected nodes changes over time. The list of top connected values, top_connected, from the previous exercise has been loaded.

Remember the defaultdict you used in Chapter 1? You'll use another defaultdict in this exercise! As Eric mentioned in the video, a defaultdict is preferred here as a regular Python dictionary would throw a KeyError if you try to get an item with a key that is not currently in the dictionary.

This exercise will make use of nested for loops. That is, you'll use one for loop inside another.
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

# Get the top 5 unique degree centrality scores: top_dcs
top_dcs = sorted(set(nx.degree_centrality(G).values()), reverse=True)[:5]

# Create list of nodes that have the top 5 highest overall degree centralities
top_connected = []
for n, dc in nx.degree_centrality(G).items():
    if dc in top_dcs:
        top_connected.append(n)

'''
INSTRUCTIONS

*   Initialize a defaultdict of empty lists called connectivity.
*   Iterate over top_connected using a for loop, and in the body of this outer for loop, once again iterate over Gs. Inside this nested loop:
    *   The keys of connectivity should be the nodes n in top_connected, and the values should be the list of connectivity scores. Therefore, you have to append len(g.neighbors(n)) to connectivity[n].
*   Iterate over connectivity using .items() and plot the connectivity of each node by passing in conn to plt.plot().
'''

# Import necessary modules
import matplotlib.pyplot as plt
from collections import defaultdict

# Create a defaultdict in which the keys are nodes and the values are a list of connectivity scores over time
connectivity = defaultdict(list)
for n in top_connected:
    for g in Gs:
        connectivity[n].append(len(g.neighbors(n)))

# Plot the connectivity for each node
fig = plt.figure() 
for n, conn in connectivity.items(): 
    plt.plot(conn, label=n) 
plt.legend()  
plt.show()
