'''
Number of edges over time

You're now going to get some practice plotting other evolving graph statistics. We'll start with a simpler exercise to kick things off. First off, plot the number of edges over time.

To do this, you'll create a list of the number of edges per month. The index of this list will correspond to the months elapsed since the first month.
'''

import pandas as pd
import networkx as nx 

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

*   Import matplotlib.pyplot as plt.
*   Create a list of the number of edges per month called edge_sizes. Use a list comprehension to do this, where you iterate over Gs using an iterator variable called g, and your output expression is len(g.edges()).
*   Plot edge sizes over time.
'''

# Import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure()

# Create a list of the number of edges per month
edge_sizes = [len(g.edges()) for g in Gs]

# Plot edge sizes over time
plt.plot(edge_sizes)
plt.xlabel('Time elapsed from first month (in months).') 
plt.ylabel('Number of edges')                           
plt.show() 
