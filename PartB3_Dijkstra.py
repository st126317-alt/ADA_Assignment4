import pandas as pd
from collections import defaultdict
import math

# ── Load graph from CSV ───────────────────────────────────────────────
df = pd.read_csv("roads.csv")
df.columns = df.columns.str.strip()   # strip whitespace from headers

graph = defaultdict(list)
for _, row in df.iterrows():
    graph[row['source']].append((row['destination'], row['weight']))

print("Graph (adjacency list):")
for node, neighbors in sorted(graph.items()):
    print(f"  {node} -> {neighbors}")
print()

# ── Dijkstra’s Algorithm 
def dijkstra(graph, start):
    # Check for negative weights
    for u in graph:
        for v, w in graph[u]:
            if w < 0:
                raise ValueError("Graph contains negative edge weights. Use Bellman–Ford instead.")

    # Initialize distances and parent pointers
    dist = {node: math.inf for node in graph}
    for u in graph:
        for v, _ in graph[u]:
            if v not in dist:
                dist[v] = math.inf

    dist[start] = 0
    parent = {node: None for node in dist}
    visited = set()

    while len(visited) < len(dist):
        # Pick the unvisited node with smallest distance
        current = None
        current_dist = math.inf
        for node in dist:
            if node not in visited and dist[node] < current_dist:
                current = node
                current_dist = dist[node]

        if current is None:
            break

        visited.add(current)

        # Relax edges
        for neighbor, weight in graph.get(current, []):
            if dist[current] + weight < dist[neighbor]:
                dist[neighbor] = dist[current] + weight
                parent[neighbor] = current

    return dist, parent

# ── Run Dijkstra from 'A' 
start_node = 'A'
distances, parents = dijkstra(graph, start_node)

print(f"=== Dijkstra Shortest paths from '{start_node}' ===")
for node in sorted(distances):
    path = []
    cur = node
    while cur is not None:
        path.append(cur)
        cur = parents[cur]
    path.reverse()
    print(f"  {start_node} → {node}: distance = {distances[node]}, path = {' -> '.join(path)}")


