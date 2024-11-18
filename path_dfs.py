""" 
Υλοποίηση DFS αναδρομικά
"""

from collections import deque

G = {
    "A": ["B", "C", "D", "E"],
    "B": ["A", "C"],
    "C": ["B", "D", "E"],
    "D": ["A", "C"],
    "E": ["A", "C"],
}

def incident_edges(g, u):
    ie = []
    for v in g[u]:
        ie.append((u, v))
    return ie

vertex_labels = {}
for u in G:
    vertex_labels[u]= 'UNEXPLORED'

edge_labels = {}
for u, vs in G.items():
    for v in vs:
        edge_labels[(u,v)]= 'UNEXPLORED'

a_stack = deque()

def path_dfs(g, u, v):
    vertex_labels[u] = 'VISITED'
    a_stack.append(u)
    if u == v:
        print(a_stack)
        return
    for e in incident_edges(g, u):
        if edge_labels[e] == 'UNEXPLORED':
            w = e[1]
            if vertex_labels[w] == 'UNEXPLORED':
                edge_labels[e] = 'DISCOVERY'
                a_stack.append(e)
                path_dfs(g, w, v)
                a_stack.pop()
            else:
                edge_labels[e] = 'BACK'
    a_stack.pop()            


path_dfs(G, "A", "E")