from collections import deque

# Adjacency list
adj_list = {
    'A':['B','D'],
    'B':['C','F'],
    'C':['E','G','H'],
    'G':['E','H'],
    'E':['B','F'],
    'F':['A'],
    'D':['F'],
    'H':['A']
}

def shortest_path_bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])  # store (node, path_so_far)

    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None

# ---- Input ----
source = input("Enter source node: ")
destination = input("Enter destination node: ")

path = shortest_path_bfs(adj_list, source, destination)
if path:
    print("Shortest path:", " -> ".join(path))
else:
    print("No path exists between", source, "and", destination)
