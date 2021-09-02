'''
Recommend repositories

You're close to the end! Here, the task is to practice using set differences, and you'll apply it to recommending repositories from a second user that the first user should contribute to.
'''

import pickle
import networkx as nx

from networkx import Graph

# Reading Graph v1 pickle data
with open('../datasets/github.p', 'rb') as f:
    G = pickle.load(f)

# Reading Graph v2 pickle data
#with open('../datasets/github.p2', 'rb') as f:
#    nodes, edges = pickle.load(f)
#    G = Graph()
#    G.add_nodes_from(nodes)
#    G.add_edges_from(edges)

'''
INSTRUCTIONS

*   Write a function called recommend_repositories() that accepts 3 arguments - G, from_user, and to_user - and returns the repositories that the from_user is connected to that the to_user is not connected to.
    *   Get the set of repositories the from_user has contributed to and store it as from_repos. To do this, first obtain the neighbors of from_user and use the set() function on this.
    *   Get the set of repositories the to_user has contributed to and store it as to_repos.
    *   Using the .difference() method, return the repositories that the from_user is connected to that the to_user is not connected to.
*   Print the repositories to be recommended from 'u7909' to 'u2148'.
'''

def recommend_repositories(G, from_user, to_user):
    # Get the set of repositories that from_user has contributed to
    from_repos = set(G.neighbors(from_user))
    # Get the set of repositories that to_user has contributed to
    to_repos = set(G.neighbors(to_user))

    # Identify repositories that the from_user is connected to that the to_user is not connected to
    return from_repos.difference(to_repos)

# Print the repositories to be recommended
print(recommend_repositories(G, 'u7909', 'u2148'))
