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

# Μετατροπή του γραφήματος σε γράφημα NetworkX
graph = nx.DiGraph()
for u, edges in G.items():
    for weight, v in edges:
        graph.add_edge(u, v, weight=weight)

# Floyd-Warshall algorithm
try:
    # Μήκη συντομότερων διαδρομών για όλα τα ζεύγη κορυφών
    floyd_warshall_lengths = nx.floyd_warshall(graph)
    # Συντομότερες διαδρομές για όλα τα ζεύγη
    floyd_warshall_paths = nx.floyd_warshall_predecessor_and_distance(graph)[0]

    print("Floyd-Warshall αποστάσεις συντομότερων διαδρομών:")
    for u, distances in floyd_warshall_lengths.items():
        for v, distance in distances.items():
            print(f"  From {u} to {v}: {distance}")

    print("\nFloyd-Warshall συντομότερες διαδρομές:")
    for u, preds in floyd_warshall_paths.items():
        for v, pred in preds.items():
            # Επαναδημιουργία της διαδρομής
            path = []
            current = v
            while current is not None:
                path.append(current)
                current = floyd_warshall_paths[u].get(current)
            path.reverse()
            print(f"  Από {u} προς {v}: {' -> '.join(path)}")

except nx.NetworkXError as e:
    print("Σφάλμα:", e)
