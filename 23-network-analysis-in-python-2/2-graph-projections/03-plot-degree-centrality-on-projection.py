'''
Plot degree centrality on projection

Here, you're going to compare the degree centrality distributions for each of the following graphs: the original graph G, the people graph projection peopleG, and the clubs graph projection clubsG. This will reinforce the difference in degree centrality score computation between bipartite and unipartite versions of degree centrality metrics. The node lists people and clubs have been pre-loaded for you.

Recall from the video that the bipartite functions require passing in a container of nodes, but will return all degree centrality scores nonetheless.
'''

import pickle
import networkx as nx

# Reading Graph v1 pickle data
with open('../datasets/american-revolution.p', 'rb') as f:
    G = pickle.load(f)

# Reading Graph v2 pickle data
#with open('../datasets/american-revolution.p2', 'rb') as f:
#    nodes, edges = pickle.load(f)
#    G = nx.Graph()
#    G.add_nodes_from(nodes)
#    G.add_edges_from(edges)

# Prepare the nodelists needed for computing projections: people, clubs
people = [n for n in G.nodes() if G.node[n]['bipartite'] == 'people']
clubs = [n for n, d in G.nodes(data=True) if d['bipartite'] == 'clubs']

# Compute the people and clubs projections: peopleG, clubsG
peopleG = nx.bipartite.projected_graph(G, people)
clubsG = nx.bipartite.projected_graph(G, clubs)

'''
INSTRUCTIONS

*   Plot the degree centrality distribution of the original graph G, using the degree_centrality function from the bipartite module: nx.bipartite.degree_centrality(). It takes in two arguments: The graph G, and one of the node lists (people or clubs).
*   Plot the degree centrality distribution of the peopleG graph, using the normal/non-bipartite degree_centrality function from NetworkX: nx.degree_centrality().
*   Plot the degree centrality distribution of the clubsG graph, using the normal/non-bipartite degree_centrality function from NetworkX: nx.degree_centrality().
*   In your calls to plt.hist(), remember to first use the .values() method on computed degree centralities and convert them into a list.
'''

import matplotlib.pyplot as plt 

# Plot the degree centrality distribution of both node partitions from the original graph
plt.figure()
original_dc = nx.bipartite.degree_centrality(G, people)
plt.hist(list(original_dc.values()), alpha=0.5)
plt.yscale('log')
plt.title('Bipartite degree centrality')
plt.show()

# Plot the degree centrality distribution of the peopleG graph
plt.figure()  
people_dc = nx.degree_centrality(peopleG)
plt.hist(list(people_dc.values()))
plt.yscale('log')
plt.title('Degree centrality of people partition')
plt.show()

# Plot the degree centrality distribution of the clubsG graph
plt.figure() 
clubs_dc = nx.degree_centrality(clubsG)
plt.hist(list(clubs_dc.values()))
plt.yscale('log')
plt.title('Degree centrality of clubs partition')
plt.show()
