import csv
import heapq

def load_graph(filename):
    graph = {}
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for u, v, w in reader:
            w = int(w)
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append((v, w))
            graph[v].append((u, w))  # undirected
    return graph

def prim(graph, start):
    mst_edges = []
    visited = set([start])
    edges = [(w, start, v) for v, w in graph[start]]
    heapq.heapify(edges)

    while edges:
        w, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst_edges.append((u, v, w))
            for to, weight in graph[v]:
                if to not in visited:
                    heapq.heappush(edges, (weight, v, to))
    return mst_edges

# Example usage
graph = load_graph("infra.csv")
mst = prim(graph, "A")
print("MST edges:", mst)
