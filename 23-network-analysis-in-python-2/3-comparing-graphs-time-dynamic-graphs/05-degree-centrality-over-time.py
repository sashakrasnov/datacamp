'''
Degree centrality over time

Now, you're going to plot the degree centrality distribution over time. Remember that the ECDF function will be provided, so you won't have to implement it.
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

'''
INSTRUCTIONS

*   Create a list of degree centrality scores month-by-month. To do this:
    *   In each iteration of the first for loop, compute the degree centrality of G using the nx.degree_centrality() function. Save the result as cent.
    *   Append cent to the list cents.
*   Plot ECDFs over time. To do this:
    *   Iterate over range(len(cents)) using a for loop. Inside the loop, use the ECDF() function with cents[i].values() as the argument. Unpack the output of this into x and y.
    *   Pass x and y as arguments to plt.plot().
'''

# Import necessary modules
import matplotlib.pyplot as plt

# Create a list of degree centrality scores month-by-month
cents = []
for G in Gs:
    cent = nx.degree_centrality(G)
    cents.append(cent)

# Plot ECDFs over time
fig = plt.figure()
for i in range(len(cents)):
    x, y = ECDF(cents[i].values()) 
    plt.plot(x, y, label='Month {0}'.format(i+1)) 
plt.legend()   
plt.show()
