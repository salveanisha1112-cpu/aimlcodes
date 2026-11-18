
import time

# Graph representing routes
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

# Breadth First Search
def BFS(start, goal):
    queue = [[start]]
    visited = []
    nodes = 0

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            visited.append(node)
            nodes += 1

            if node == goal:
                return path, nodes

            for neighbour in graph[node]:
                new_path = path + [neighbour]
                queue.append(new_path)

    return None, nodes


# Depth First Search
def DFS(start, goal):
    stack = [[start]]
    visited = []
    nodes = 0

    while stack:
        path = stack.pop()
        node = path[-1]

        if node not in visited:
            visited.append(node)
            nodes += 1

            if node == goal:
                return path, nodes

            for neighbour in reversed(graph[node]):
                new_path = path + [neighbour]
                stack.append(new_path)

    return None, nodes


# Main Program
start = 'A'
goal = 'G'

# BFS Execution
t1 = time.time()
bfs_path, bfs_nodes = BFS(start, goal)
bfs_time = time.time() - t1

# DFS Execution
t1 = time.time()
dfs_path, dfs_nodes = DFS(start, goal)
dfs_time = time.time() - t1

# Display Results
print("BFS Result")
print("Path:", bfs_path)
print("Path Length:", len(bfs_path) - 1)
print("Nodes Explored:", bfs_nodes)
print("Execution Time:", bfs_time)

print("\nDFS Result")
print("Path:", dfs_path)
print("Path Length:", len(dfs_path) - 1)
print("Nodes Explored:", dfs_nodes)
print("Execution Time:", dfs_time)

print("\nPerformance Comparison")
print("BFS Path Length:", len(bfs_path) - 1)
print("DFS Path Length:", len(dfs_path) - 1)
print("BFS Nodes Explored:", bfs_nodes)
print("DFS Nodes Explored:", dfs_nodes)
