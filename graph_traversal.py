from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "E"],
    "C": ["A", "B", "D"],
    "D": ["C", "E"],
    "E": ["B", "D"],
}


def bfs(s, e):
    """Αναζήτηση κατά πλάτος από το s στο  e"""
    frontier = deque()  # μέτωπο αναζήτησης
    frontier.append(s)
    visited = set()  # κορυφές που έχουν επισκεφτεί
    visited.add(s)
    prev = {s: None}  # για κάθε κορυφή, η προηγούμενη κορυφή
    while frontier:  # όσο το μέτωπο αναζήτησης δεν είναι κενό
        current_node = frontier.popleft()
        for next_node in graph[current_node]:
            if not next_node in visited:
                frontier.append(next_node)
                visited.add(next_node)
                prev[next_node] = current_node

    # κατασκευή του μονοπατιού από το e στο s
    path = []
    at = e
    while at != None:
        path.append(at)
        at = prev[at]

    # αντιστροφή του μονοπατιού για να προκύψει το μονoπάτι από το s στο e
    path = path[::-1]

    # αν τα s και e είναι συνδεδεμένα επιστροφή του μονοπατιού
    if path[0] == s:
        return path
    return []


def dfs(s, e):
    """Αναζήτηση κατά βάθος από το s στο  e"""
    frontier = deque()  # μέτωπο αναζήτησης
    frontier.append(s)
    visited = set()  # κορυφές που έχουν επισκεφτεί
    visited.add(s)
    prev = {s: None}  # για κάθε κορυφή, η προηγούμενη κορυφή
    while frontier:  # όσο το μέτωπο αναζήτησης δεν είναι κενό
        current_node = frontier.pop()
        for next_node in graph[current_node]:
            if not next_node in visited:
                frontier.append(next_node)
                visited.add(next_node)
                prev[next_node] = current_node

    # κατασκευή του μονοπατιού από το e στο s
    path = []
    at = e
    while at != None:
        path.append(at)
        at = prev[at]

    # αντιστροφή του μονοπατιού για να προκύψει το μονoπάτι από το s στο e
    path = path[::-1]

    # αν τα s και e είναι συνδεδεμένα επιστροφή του μονοπατιού
    if path[0] == s:
        return path
    return []


path = bfs("A", "E")
print("BFS: ", path)

path = dfs("A", "E")
print("DFS:", path)
