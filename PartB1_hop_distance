# Build an unweighted graph
import csv
 
def build_unweighted_graph(filepath):
    graph = {}
 
    with open(filepath, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        reader.fieldnames = [h.strip() for h in reader.fieldnames]
 
        for row in reader:
            src = row['source'].strip()
            dst = row['destination'].strip()
            # Weight column is read but intentionally ignored
 
            graph.setdefault(src, set()).add(dst)
            graph.setdefault(dst, set()).add(src)  # Remove for directed graph
 
    return graph
"""
Unweighted Graph (adjacency list):
  A: ['B', 'C']
  B: ['A', 'C', 'D']
  C: ['A', 'B', 'D']
  D: ['B', 'C']
"""
# BFS implementation
def bfs_min_hops(graph, source):
    """BFS from source. Returns (distances, predecessors) for all reachable nodes."""
    if source not in graph:
        raise ValueError(f"Source vertex '{source}' not found in graph.")
 
    distances = {source: 0}
    predecessors = {source: None}
    queue = [source]
    head = 0
 
    while head < len(queue):
        node = queue[head]
        head += 1
 
        for neighbor in graph[node]:
            if neighbor not in distances:
                distances[neighbor] = distances[node] + 1
                predecessors[neighbor] = node
                queue.append(neighbor)
 
    return distances, predecessors
"""
BFS results from source A:
A -> B: 1 hop(s)
A -> C: 1 hop(s)
A -> D: 2 hop(s)*/
"""
# Reconstruct the path
def reconstruct_path(predecessors, source, target):
    """Walk the predecessor map from target back to source to rebuild the path."""
    if target not in predecessors:
        return None
 
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = predecessors[node]
 
    path.reverse()
 
    if path[0] != source:
        return None
 
    return path
"""
Reconstructed paths from source A:
A -> B: A -> B
A -> C: A -> C
A -> D: A -> C -> D
"""
def print_results(source, distances, predecessors):
    """Print a formatted table of hop count and path for every reachable target."""
    targets = sorted(t for t in distances if t != source)
 
    # Column widths
    col_target = max(len("Target"), max(len(t) for t in targets))
    col_hops   = max(len("Hops"), max(len(str(distances[t])) for t in targets))
 
    paths = {t: reconstruct_path(predecessors, source, t) for t in targets}
    col_path = max(len("Path"), max(len(" -> ".join(p)) if p else len("unreachable") for p in paths.values()))
 
    header = (f"{'Target':<{col_target}}  {'Hops':>{col_hops}}  {'Path':<{col_path}}")
    divider = "-" * len(header)
 
    print(f"BFS results from source '{source}':")
    print(divider)
    print(header)
    print(divider)
 
    for t in targets:
        hops = distances[t]
        path_str = " -> ".join(paths[t]) if paths[t] else "unreachable"
        print(f"{t:<{col_target}}  {hops:>{col_hops}}  {path_str:<{col_path}}")
 
    print(divider)
"""
Output for source A:
BFS results from source 'A':
-------------------------
Target  Hops  Path
-------------------------
B          1  A -> B
C          1  A -> C
D          2  A -> B -> D
-------------------------
"""
if __name__ == "__main__":
    graph = build_unweighted_graph('roads.csv')
 
    print("Unweighted Graph (adjacency list):")
    for node, neighbors in sorted(graph.items()):
        print(f"  {node}: {sorted(neighbors)}")
    print()
 
    source = 'A'
    distances, predecessors = bfs_min_hops(graph, source)
    print_results(source, distances, predecessors)