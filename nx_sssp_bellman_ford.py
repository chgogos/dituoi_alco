import networkx as nx
from collections import defaultdict

G = defaultdict(
    list,
    {
        "A": [(8, "B"), (-2, "C"), (4, "D")],
        "B": [(-2, "E")],
        "C": [(7, "B"), (3, "E"), (1, "D")],
        "D": [(5, "F")],
        "E": [],
        "F": [(9, "C")],
    },
)

# Μετατροπή γραφήματος σε ένα γράφημα NetworkX
graph = nx.DiGraph()
for u, edges in G.items():
    for weight, v in edges:
        graph.add_edge(u, v, weight=weight)

# Bellman-Ford 
try:
    bellman_ford_lengths = nx.single_source_bellman_ford_path_length(graph, source="A")
    bellman_ford_paths = nx.single_source_bellman_ford_path(graph, source="A")
    
    print("Bellman-Ford, μήκη συντομότερων διαδρομών με αφετηρία το A:")
    for node, length in bellman_ford_lengths.items():
        print(f"  προς {node}: {length}")
    
    print("\nBellman-Ford, συντομότερες διαδρομές με αφετηρία το A:")
    for node, path in bellman_ford_paths.items():
        print(f"  προς {node}: {' -> '.join(path)}")

except nx.NetworkXUnbounded:
    print("Αρνητικός κύκλος")
