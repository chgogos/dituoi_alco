from collections import defaultdict
import graphviz

# directed weighted graph (Κεφάλαιο 14, διαφάνεια 18)
G1 = defaultdict(
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


# directed graph
G2 = defaultdict(
    list,
    {
        "a": ["b", "c", "f"],
        "b": ["c", "d", "e"],
        "c": ["d"],
        "e": ["d"],
        "f": ["b", "e"],
    },
)

# undirected weighted graph
G3 = defaultdict(
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

# directed weighted graph (Κεφάλαιο 14, διαφάνεια 15)
G4 = defaultdict(
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


def export_graph_to_dot(graph, export_filename, directed=True, weighted=True):
    if directed:
        dot = graphviz.Digraph()
        for v in graph:
            dot.node(v, v)
        if weighted:
            for u in graph:
                for w, v in graph[u]:
                    dot.edge(u, v, str(w))
        else:
            for u in graph:
                for v in graph[u]:
                    dot.edge(u, v)
    else:
        dot = graphviz.Graph()
        for v in graph:
            dot.node(v, v)
        if weighted:
            for u in graph:
                for w, v in graph[u]:
                    if u < v:
                        dot.edge(u, v, str(w))
        else:
            for u in graph:
                for v in graph[u]:
                    if u < v:
                        dot.edge(u, v)

    dot.render(export_filename, view=True)


# export_graph_to_dot(G1, "graph_ch14_page18.dot", directed=True, weighted=True)
# export_graph_to_dot(G2, "graph2.dot", directed=True, weighted=False)
# export_graph_to_dot(G3, "graph3.dot", directed=False, weighted=True)
# export_graph_to_dot(G4, "graph_ch14_page15.dot", directed=True, weighted=True)
