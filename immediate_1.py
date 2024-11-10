from collections import deque
import time

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B', 'F'],
    'E': ['B', 'G', 'H'],
    'F': ['D'],
    'G': ['E', 'I', 'J'],
    'H': ['E', 'K'],
    'I': ['G', 'L'],
    'J': ['G', 'L'],
    'K': ['H'],
    'L': ['I', 'J']
}

# BFS implementation with running time measurement
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# DFS implementation with running time measurement
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Measure and display BFS running time
print("BFS traversal:")
start_time = time.time()
bfs(graph, 'A')
end_time = time.time()
print(f"\nBFS Running Time: {end_time - start_time} seconds")

# Measure and display DFS running time
print("\nDFS traversal:")
start_time = time.time()
dfs(graph, 'A')
end_time = time.time()
print(f"\nDFS Running Time: {end_time - start_time} seconds")
