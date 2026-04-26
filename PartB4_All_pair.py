import math
import csv

def load_graph(filename):
    nodes = set()
    edges = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            u, v, w = row['source'].strip(), row['destination'].strip(), int(row['weight'])
            nodes.add(u)
            nodes.add(v)
            edges.append((u, v, w))
    nodes = sorted(nodes)
    return nodes, edges

def floyd_warshall(nodes, edges):
    index = {node: i for i, node in enumerate(nodes)}
    n = len(nodes)

    # Initialize distance matrix
    dist = [[math.inf] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    # Insert edge weights
    for u, v, w in edges:
        dist[index[u]][index[v]] = w

    # Core Floyd–Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

def detect_negative_cycle(dist, nodes):
    for i, node in enumerate(nodes):
        if dist[i][i] < 0:
            print(f"Negative cycle detected involving node {node}")
            return True
    print("No negative cycle detected.")
    return False

# Example usage
nodes, edges = load_graph("roads.csv")
shortest_paths = floyd_warshall(nodes, edges)

print("All-pairs shortest path matrix:")
for i, u in enumerate(nodes):
    for j, v in enumerate(nodes):
        print(f"{u} → {v}: {shortest_paths[i][j]}")
