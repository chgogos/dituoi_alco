import logging
from collections import defaultdict
from typing import Dict, List, Tuple, Optional


def bellman_ford(
    graph: defaultdict, start: str
) -> Tuple[Optional[Dict[str, int]], Optional[Dict[str, List[str]]]]:
    """
    Υλοποίηση του αλγορίθμου Bellman-Ford για εύρεση συντομότερων διαδρομών από την κορυφή startπρος όλες τις άλλες κορυφές.
    Μπορεί να αναιχνεύει αρνητικούς κύκλους και να λειτουργεί σωστά με αρνητικά βάρη ακμών.

    Ορίσματα:
        graph: Ένα defaultdict που αναπαριστά έναν γράφο όπου κάθε τιμή είναι μια λίστα από (distance, destination)
        start: Κορυφή αφετηρίας

    Returns:
        Μια πλειάδα που περιέχει:
        - Ένα λεξικό με τις συντομότερες αποστάσεις προς κάθε κορυφή (ή None αν υπάρχει αρνητικός κύκλος)
        - Ένα λεξικό διαδρομών προς κάθε κορυφή (ή None αν υπάρχει αρνητικός κύκλος)
        Επιστρέφει (None, None) αν ανιχνευθεί αρνητικός κύκλος
    """
    nodes = list(graph.keys())

    # Αρχικοποίηση αποστάσεων και διαδρομών
    distances = {node: float("infinity") for node in nodes}
    distances[start] = 0
    paths = {node: [] for node in nodes}
    paths[start] = [start]

    # Δημιουργία λίστα ακμών της μορφής (αφετηρία, προορισμός, βάρος)
    edges = []
    for source in graph:
        for weight, dest in graph[source]:
            edges.append((source, dest, weight))

    # Χαλάρωση (relax) όλων των ακμών το πολύ |V| - 1 φορές
    for iteration in range(len(nodes) - 1):
        relax = False
        for source, dest, weight in edges:
            if (
                distances[source] != float("infinity")
                and distances[source] + weight < distances[dest]
            ):
                logging.debug(
                    f"Iteration = {iteration+1}, node = {dest}, distance = {distances[dest]} ->  {distances[source] + weight}"
                )
                distances[dest] = distances[source] + weight
                paths[dest] = paths[source] + [dest]
                relax = True
        if not relax:
            break

    # Έλεγχος για αρνητικούς κύκλους
    # Αν μπορεί να γίνει χαλάρωση με μια ακμή, τότε έχουμε αρνητικό κύκλο
    for source, dest, weight in edges:
        if (
            distances[source] != float("infinity")
            and distances[source] + weight < distances[dest]
        ):
            # Ανιχνεύθηκε αρνητικός κύκλος
            return None, None

    return distances, paths


def format_path_distances(
    distances: Optional[Dict[str, int]], paths: Optional[Dict[str, List[str]]]
) -> str:
    """Βοηθητική συνάρτηση για μορφοποίηση αποτελεσμάτων"""
    if distances is None or paths is None:
        return "Negative cycle detected in the graph!"

    result = []
    for node in sorted(distances.keys()):
        if distances[node] != float("infinity"):
            path_str = " -> ".join(paths[node])
            result.append(
                f"To {node}: Distance = {distances[node]:2}, Path = {path_str}"
            )
        else:
            result.append(f"To {node}: No path found")
    return "\n".join(result)


# Μη κατευθυνόμενο γράφημα (Παράδειγμα βιβλίου Goodrich & Tamassia)
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
    distances, paths = bellman_ford(G, "PVD")
    print(format_path_distances(distances, paths))


# Μη κατευθυνόμενο γράφημα με αρνητικό κύκλο βαρών
def example2():
    G = defaultdict(
        list,
        {
            "A": [(5, "B"), (7, "C")],
            "B": [(5, "A"), (-4, "C")],
            "C": [(-4, "B"), (7, "A")],
        },
    )

    distances, paths = bellman_ford(G, "A")
    print(format_path_distances(distances, paths))


# Κατευθυνόμενο γράφημα με αρνητικό βάρος ακμής
def example3():
    G = defaultdict(
        list,
        {
            "A": [(5, "B"), (7, "C")],
            "B": [],
            "C": [(-4, "B")],
        },
    )

    distances, paths = bellman_ford(G, "A")
    print(format_path_distances(distances, paths))


# Κατευθυνόμενο γράφημα (Παράδειγμα βιβλίου Goodrich & Tamassia, κεφάλαιο 14, διαφάνεια 15 - Bellman Ford)
def example4():
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
    distances, paths = bellman_ford(G, "A")
    print(format_path_distances(distances, paths))


# Κατευθυνόμενο γράφημα (Παράδειγμα βιβλίου Goodrich & Tamassia, κεφάλαιο 14, διαφάνεια 18)
def example5():
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
    distances, paths = bellman_ford(G, "A")
    print(format_path_distances(distances, paths))


if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    logging.basicConfig(level=logging.INFO)
    # example1()
    # example2()
    # example3()
    example4()
    # example5()
