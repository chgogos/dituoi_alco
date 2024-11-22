import networkx as nx
from collections import defaultdict

G = defaultdict(
    list,
    {
        "DFW": [(802, "ORD"), (1120, "MIA"), (1233, "LAX"), (1387, "LGA")],
        "HNL": [(2555, "LAX")],
        "LAX": [(337, "SFO"), (1233, "DFW"), (1743, "ORD"), (2555, "HNL")],
        "LGA": [(142, "PVD"), (1099, "MIA"), (1387, "DFW")],
        "MIA": [(1099, "LGA"), (1120, "DFW"), (1205, "PVD")],
        "ORD": [(802, "DFW"), (849, "PVD"), (1743, "LAX"), (1843, "SFO")],
        "PVD": [(142, "LGA"), (849, "ORD"), (1205, "MIA")],
        "SFO": [(337, "LAX"), (1843, "ORD")],
    },
)

# Μετατροπή γραφήματος σε ένα γράφημα NetworkX
graph = nx.DiGraph()
for u, edges in G.items():
    for weight, v in edges:
        graph.add_edge(u, v, weight=weight)

try:
    source = "PVD"
    dijstra_lengths = nx.single_source_dijkstra_path_length(graph, source=source)
    dijkstra_paths = nx.single_source_dijkstra_path(graph, source=source)

    print(f"Dijkstra, μήκη συντομότερων διαδρομών με αφετηρία το {source}:")
    for node, length in dijstra_lengths.items():
        print(f"  προς {node}: {length}")

    print(f"\nDijkstra, συντομότερες διαδρομές με αφετηρία το {source}:")
    for node, path in dijkstra_paths.items():
        print(f"  προς {node}: {' -> '.join(path)}")

except nx.NetworkXUnbounded:
    print("Αρνητικό βάρος")
