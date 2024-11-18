from collections import defaultdict


def edge_exists(graph, u, v):
    for weight, neighbor in graph[u]:
        if neighbor == v:
            return True, weight
    return False, None


def floydwarshall(graph):
    nodes = graph.keys()
    M = [[float("infinity") for x in range(len(nodes))] for y in range(len(nodes))]
    for i, u in enumerate(nodes):
        for j, v in enumerate(nodes):
            if i == j:
                M[i][j] = 0
                continue
            exists, weight = edge_exists(graph, u, v)
            if exists:
                M[i][j] = weight
    for k in range(len(M)):
        for i in range(len(M)):
            for j in range(len(M)):
                newDistance = M[i][k] + M[k][j]
                if newDistance < M[i][j]:
                    M[i][j] = newDistance
    return M


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

    distances_matrix = floydwarshall(G)
    nodes = G.keys()
    for i, u in enumerate(nodes):
        for j, v in enumerate(nodes):
            if i == j:
                continue
            print(f"{u}->{v} disrance = {distances_matrix[i][j]}")


if __name__ == "__main__":
    example1()
