'''
List of graphs

In this set of exercises, you'll use a college messaging dataset to learn how to filter graphs for time series analysis. In this dataset, nodes are students, and edges denote messages being sent from one student to another. The graph as it stands right now captures all communications at all time points.

Let's start by analyzing the graphs in which only the edges change over time.

The dataset has been loaded into a DataFrame called data. Feel free to explore it in the IPython Shell. Specifically, check out the output of data['sender'] and data['recipient'].
'''

import pandas as pd

data = pd.read_csv('../datasets/college_msg_preprocessed.csv')

'''
INSTRUCTIONS

*   Initialize an empty list called Gs.
*   Use a for loop to iterate over months. Inside the loop:
    *   Instantiate a new undirected graph called G, using the nx.Graph() function.
    *   Add in all nodes that have ever shown up to the graph. To do this, use the .add_nodes_from() method on G two times, first with data['sender'] as argument, and then with data['recipient'].
    *   Filter the DataFrame so there's only the given month. This has been done for you.
    *   Add edges from the filtered DataFrame. To do this, use the .add_edges_from() method with df_filtered['sender'] and df_filtered['recipient'] passed into zip().
    *   Append G to the list of graphs Gs.
'''

import networkx as nx 

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
    
print(len(Gs))