import pandas as pd
from collections import defaultdict
import math

# ── Load graph from CSV ───────────────────────────────────────────────
df = pd.read_csv("roads.csv")
df.columns = df.columns.str.strip()   # strip whitespace from headers

# Build edge list
edges = []
nodes = set()
for _, row in df.iterrows():
    u, v, w = row['source'], row['destination'], row['weight']
    edges.append((u, v, w))
    nodes.add(u)
    nodes.add(v)

# ── Bellman–Ford Algorithm ───────────────────────────────────────────
def bellman_ford(edges, nodes, start):
    dist = {node: math.inf for node in nodes}
    parent = {node: None for node in nodes}
    dist[start] = 0

    # Relax edges |V|-1 times
    for _ in range(len(nodes) - 1):
        for u, v, w in edges:
            if dist[u] != math.inf and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u

    # Detect negative-weight cycles
    for u, v, w in edges:
        if dist[u] != math.inf and dist[u] + w < dist[v]:
            raise ValueError("Graph contains a negative-weight cycle")

    return dist, parent

# ── Bellman–Ford with Negative Cycle Detection ───────────────────────
def bellman_ford_detect_cycle(edges, nodes, start):
    dist = {node: math.inf for node in nodes}
    parent = {node: None for node in nodes}
    dist[start] = 0

    # Relax edges |V|-1 times
    for _ in range(len(nodes) - 1):
        for u, v, w in edges:
            if dist[u] != math.inf and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u

    # Check for negative-weight cycles
    for u, v, w in edges:
        if dist[u] != math.inf and dist[u] + w < dist[v]:
            print("Negative-weight cycle detected!")
            return True, dist, parent

    print("No negative-weight cycle detected.")
    return False, dist, parent

def reconstruct_path(parents, start, end):
    """Reconstruct shortest path from start to end using parent pointers."""
    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = parents[cur]
    path.reverse()

    # If the path doesn't start at 'start', then 'end' is unreachable
    if path[0] != start:
        return None
    return path

# ── Run Bellman–Ford from 'A' ────────────────────────────────────────
has_cycle, distances, parents = bellman_ford_detect_cycle(edges, nodes, 'A')

if not has_cycle:
    print("=== Bellman–Ford Shortest paths from 'A' ===")
    for node in sorted(distances):
        path = []
        cur = node
        while cur is not None:
            path.append(cur)
            cur = parents[cur]
        path.reverse()
        print(f"  A → {node}: distance = {distances[node]}, path = {' -> '.join(path)}")
