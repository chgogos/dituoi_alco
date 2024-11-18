""" 
Υλοποίηση DFS αναδρομικά

Τροποποιημένος κώδικας από το: 
Data Structures and Algorithms in Python by Goodrich, Tamassia
"""

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


def dfs(g, u, discovered):
    """Δημιουργία του λεξικού discovered που αντιστοιχεί
    κάθε όνομα κορυφής (key) με την ακμή που χρησιμοποιήθηκε
    για τον εντοπισμό της (value)"""
    for e in incident_edges(g, u):
        v = e[1]  # ο προορισμός της ακμής e
        if v not in discovered:
            discovered[v] = e
            dfs(g, v, discovered)


def construct_path(u, v, discovered):
    """Διαδρομή από την κορυφή u στην κορυφή v"""
    path = []
    if v in discovered:
        path.append(v)
        current = v
        while current is not u:
            e = discovered[current]
            parent = e[0]
            path.append(parent)
            current = parent
        path.reverse()
    return path


result = {"A": None}
dfs(G, "A", result)
print(result)

# εμφάνιση όλων των διαδρομών από την κορυφή Α προς όλες τις άλλες κορυφές
for v in "BCDE":
    print(construct_path("A", v, result))
