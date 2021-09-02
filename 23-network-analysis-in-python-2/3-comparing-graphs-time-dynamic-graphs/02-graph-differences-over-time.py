'''
Graph differences over time

Now, you'll compute the graph differences over time! To look at the simplest case, here you'll use a window of (month, month + 1), and then keep track of the edges gained or lost over time. This exercise is preparation for the next exercise, in which you will visualize the changes over time.
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

*   Inside the for loop:
    *   Assign Gs[i] to g1 and Gs[i + window] to g2.
    *   Using nx.difference() compute the difference between g2 and g1. Append the result to added.
    *   Append the difference between g1 and g2 to removed.
*   Print fractional_changes.
'''

import networkx as nx  
# Instantiate a list of graphs that show edges added: added
added = []
# Instantiate a list of graphs that show edges removed: removed
removed = []
# Here's the fractional change over time
fractional_changes = []
window = 1  
i = 0      

for i in range(len(Gs) - window):
    g1 = Gs[i]
    g2 = Gs[i + window]
        
    # Compute graph difference here
    added.append(nx.difference(g2 ,g1))   
    removed.append(nx.difference(g1 ,g2))
    
    # Compute change in graph size over time
    fractional_changes.append((len(g2.edges()) - len(g1.edges())) / len(g1.edges()))
    
# Print the fractional change
print(fractional_changes)