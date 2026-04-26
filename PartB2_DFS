import pandas as pd
from collections import defaultdict

# Load the graph from CSV
df = pd.read_csv('roads.csv')
df.columns = df.columns.str.strip()   # strip any whitespace from headers

# Build adjacency list (directed graph)
graph = defaultdict(list)
for _, row in df.iterrows():
    graph[row['source']].append((row['destination'], row['weight']))

print("Graph (adjacency list):")
for node, neighbors in sorted(graph.items()):
    print(f"  {node} -> {neighbors}")
print()

# ── Iterative DFS ─
def dfs_iterative(graph, start):
    """Return nodes in DFS visit order (iterative, using an explicit stack)."""
    visited = set()
    order   = []
    stack   = [start]

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        # Push neighbors in reverse order so leftmost is processed first
        for neighbor, weight in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)

    return order

# ── Recursive DFS 
def dfs_recursive(graph, node, visited=None, order=None):
    """Return nodes in DFS visit order (recursive)."""
    if visited is None:
        visited = set()
        order   = []

    visited.add(node)
    order.append(node)

    for neighbor, weight in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, order)

    return order

# ── Run & display results 
start_node = 'A'

print(f"=== Iterative DFS from '{start_node}' ===")
result = dfs_iterative(graph, start_node)
print(f"  Visit order: {' -> '.join(result)}\n")

print(f"=== Recursive DFS from '{start_node}' ===")
result = dfs_recursive(graph, start_node)
print(f"  Visit order: {' -> '.join(result)}\n")

# ── DFS with timestamps 
time = 0
discovery, finishing, parent = {}, {}, {}

def dfs_with_times(graph):
    global time, discovery, finishing, parent
    time = 0
    discovery, finishing, parent = {}, {}, {}
    visited = set()

    for node in graph.keys():
        if node not in visited:
            dfs_visit(graph, node, visited)

def dfs_visit(graph, u, visited):
    global time, discovery, finishing, parent
    visited.add(u)
    time += 1
    discovery[u] = time

    for v, _ in graph[u]:
        if v not in visited:
            parent[v] = u
            dfs_visit(graph, v, visited)

    time += 1
    finishing[u] = time

# ── Edge classification 
def classify_edges(graph):
    classifications = []
    for u in graph:
        for v, _ in graph[u]:
            if parent.get(v) == u:
                edge_type = "Tree"
            elif discovery[v] < discovery[u] and finishing[v] > finishing[u]:
                edge_type = "Back"
            elif discovery[u] < discovery[v] and finishing[u] > finishing[v]:
                edge_type = "Forward"
            else:
                edge_type = "Cross"
            classifications.append((u, v, edge_type))
    return classifications

# ── Run DFS and classify 
dfs_with_times(graph)
edges = classify_edges(graph)

print("Edge  | Type")
for u, v, t in edges:
    print(f"{u} -> {v} : {t}")