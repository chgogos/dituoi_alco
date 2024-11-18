from collections import defaultdict
from collections import deque


def topological_sort_kahns_weighted(graph):
    """
    Υλοποίηση τοπολογικής ταξινόμησης με τον αλγόριθμο του Kahn.
    Επιστρέφει μια λίστα κορυφών τοπολογικά διατεταγμένη.
    """
    # Υπολογισμός in-degree για κάθε κορυφή
    in_degree = defaultdict(int)
    for node in graph:
        for w, neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Αρχικοποίηση ουράς με κορυφές που δεν έχουν εξαρτήσεις
    queue = deque([node for node in graph if in_degree[node] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        # Μείωση in-degree γειτόνων και προσθήκη της γειτονικής κορυφής στην ουρά αν το in-degree της γίνει 0
        for w, neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Έλεγχος για κύκλους
    if len(result) != len(graph):
        raise ValueError("Graph contains a cycle")

    return result


def sssp_dag(graph, start):
    topo_order = topological_sort_kahns_weighted(graph)
    D = defaultdict(int)
    paths = {node: [] for node in graph}
    paths[start] = [start]
    for v in graph:
        if v == start:
            D[v] = 0
        else:
            D[v] = float("infinity")
    for v_i in topo_order:
        for w, u in graph[v_i]:
            if D[v_i] + w < D[u]:
                D[u] = D[v_i] + w
                paths[u] = paths[v_i] + [u]
    return D, paths

# Παράδειγμα βιβλίου Goodrich & Tamassia)
def example1():
    G = defaultdict(
        list,
        {
            "A": [(8, "B"), (-2, "C"), (4, "D")],
            "B": [(-5, "E")],
            "C": [(7, "B"), (3, "E"), (9, "F"), (1, "D")],
            "D": [(5, "F")],
            "E": [],
            "F": [],
        },
    )
    start = "A"
    distances, paths = sssp_dag(G, start)
    print(f"Start: {start}")
    for v in G:
        print(f"To: {v} distances: {distances[v]:2} path: {" -> ".join(paths[v])}")

#  Μη έγκυρο DAG (με κύκλο)
def example2():
    G = defaultdict(
        list,
        {
            "A": [(8, "B"), (-2, "C"), (4, "D")],
            "B": [(-5, "E")],
            "C": [(7, "B"), (3, "E"), (9, "F"), (1, "D")],
            "D": [(5, "F")],
            "E": [],
            "F": [(-1, "A")], # cycle
        },
    )
    start = "A"
    distances, paths = sssp_dag(G, start)
    print(f"Start: {start}")
    for v in G:
        print(f"To: {v} distances: {distances[v]:2} path: {" -> ".join(paths[v])}")


if __name__ == "__main__":
    example1()
    # example2()
