from collections import defaultdict
import heapq
from typing import Dict, List, Tuple


def dijkstra(
    graph: defaultdict, start: str
) -> Tuple[Dict[str, int], Dict[str, List[str]]]:
    """
    Υλοποίηση του αλγορίθμου του Dijkstra για την εύρεση των συντομότερων διαδρομών από μια κορυφή αφετηρία προς όλες τις άλλες κορυφές

     Ορίσματα:
        graph: Ένα defaultdict που αναπαριστά έναν γράφο όπου κάθε τιμή είναι μια λίστα μια λίστα από πλειάδες της μορφής (απόσταση, προορισμός)
        start: Κορυφή εκκίνησης

    Επιστρέφει:
        Μια πλειάδα που περιέχει:
        - Ένα λεξικό με τις συντομότερες αποστάσεις προς κάθε κορυφή
        - Ένα λεξικό με τις διαδρομές προς κάθε κορυφή
    """
    # Αρχικοποίηση αποστάσεων και διαδρομών
    distances = {node: float("infinity") for node in graph}
    distances[start] = 0

    # Αρχικοποίηση διαδρομών
    paths = {node: [] for node in graph}
    paths[start] = [start]

    # Ουρά προτεραιότητας για αποθήκευση ζευγών (απόσταση, κόμβος)
    pq = [(0, start)]

    # Ένα σύνολο για καταγραφή των κορυφών που έχουν επισκεφτεί
    visited = set()

    while pq:
        # Λήψη της κορυφής με τη μικρότερη απόσταση
        current_distance, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue

        visited.add(current_node)

        # Έλεγχος όλων των γειτονικών κορυφών της τρέχουσας κορυφής
        for weight, neighbor in graph[current_node]:
            if neighbor in visited: continue
            # Υπολογισμός της απόσταση της γειτονικής κορυφής (neighbor) μέσω της τρέχουσας κορυφής
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_node] + [neighbor]
                heapq.heappush(pq, (distance, neighbor))

    return distances, paths


def format_path_distances(
    distances: Dict[str, int], paths: Dict[str, List[str]]
) -> str:
    """Βοηθητική συνάρτηση για τη μορφοποίηση των αποτελεσμάτων σε εύκολα κατανοητή μορφή"""
    result = []
    for node in sorted(distances.keys()):
        if distances[node] != float("infinity"):
            path_str = " -> ".join(paths[node])
            result.append(f"To {node}: Distance = {distances[node]}, Path = {path_str}")
        else:
            result.append(f"To {node}: No path found")
    return "\n".join(result)


def example1():
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

    distances, paths = dijkstra(G, "PVD")
    print(format_path_distances(distances, paths))


# Μη κατευθυνόμενο γράφημα με αρνητικό βάρος ακμής (λάθος αποτελέσματα)
def example2():
    G = defaultdict(
        list,
        {
            "A": [(5, "B"), (7, "C")],
            "B": [(5, "A"), (-4, "C")],
            "C": [(-4, "B"), (7, "A")],
        },
    )

    distances, paths = dijkstra(G, "A")
    print(format_path_distances(distances, paths))

# Κατευθυνόμενο γράφημα με αρνητικό βάρος ακμής (λάθος αποτελέσματα)
def example3():
    G = defaultdict(
        list,
        {
            "A": [(5, "B"), (7, "C")],
            "B": [],
            "C": [(-4, "B")],
        },
    )

    distances, paths = dijkstra(G, "A")
    print(format_path_distances(distances, paths))

if __name__ == "__main__":
    example1()
    # example2()
    # example3()
