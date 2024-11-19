from collections import defaultdict
from collections import deque


def topological_sort_kahns(graph):
    """
    Υλοποίηση τοπολογικής ταξινόμησης με τον αλγόριθμο του Kahn.
    Επιστρέφει μια λίστα κορυφών τοπολογικά διατεταγμένη.
    """
    # Υπολογισμός in-degree για κάθε κορυφή
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Αρχικοποίηση ουράς με κορυφές που δεν έχεουν εξαρτήσεις
    queue = deque([node for node in graph if in_degree[node] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        # Μείωση in-degree γειτόνων και προσθήκη της γειτονικής κορυφής στην ουρά αν το in-degree της γίνει 0
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Έλεγχος για κύκλους
    if len(result) != len(graph):
        raise ValueError("Graph contains a cycle")

    return result


def topological_sort_dfs(graph):
    explored = defaultdict(bool)
    order = []
    for v in graph:
        explored[v] = False
    for v in graph:
        if not explored[v]:
            dfs(graph, v, explored, order)
    return order[::-1]

def dfs(graph, u, explored, order):
    explored[u]= True
    for v in graph[u]:
        if not explored[v]:
            dfs(graph, v, explored, order)
    order.append(u)


if __name__ == "__main__":
    graph = defaultdict(
        list,
        {
            "a": ["b", "c", "f"],
            "b": ["c", "d", "e"],
            "c": ["d"],
            "d": [],
            "e": ["d"],
            "f": ["b", "e"],
        },
    )

    # print("Τοπολογική ταξινόμηση:", topological_sort_kahns(graph))
    print("Τοπολογική ταξινόμηση:", topological_sort_dfs(graph))
