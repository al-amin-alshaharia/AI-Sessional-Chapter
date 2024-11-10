import heapq

# Define the graph as an adjacency list with edge costs
graph = {
    'A': [('B', 2), ('E', 3)],
    'B': [('A', 2), ('C', 6)],
    'C': [('B', 6), ('G', 99)],
    'E': [('A', 3), ('D', 6)],
    'D': [('E', 6), ('G', 1)],
    'G': []  # Goal node has no outgoing edges
}

# Heuristic values for each node
heuristics = {
    'A': 11,
    'B': 6,
    'C': 99,
    'E': 7,
    'D': 1,
    'G': 0
}


def a_star_search(start, goal):
    """Performs the A* search algorithm from start to goal."""
    # Priority queue to store nodes to be explored with their f(n) value
    open_list = []
    heapq.heappush(open_list, (heuristics[start], start))

    # Track visited nodes and the actual cost to reach each node
    g_costs = {start: 0}
    came_from = {}

    while open_list:
        # Get the node with the lowest f(n) value
        current_f, current_node = heapq.heappop(open_list)

        # If we reached the goal, reconstruct the path
        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            return path[::-1], g_costs[goal]  # Path and total cost

        # Explore neighbors
        for neighbor, cost in graph[current_node]:
            # Calculate tentative g cost
            tentative_g_cost = g_costs[current_node] + cost

            # Only proceed if we find a cheaper path to the neighbor
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristics[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))
                came_from[neighbor] = current_node

    return None, float('inf')  # Return None if no path found


# Run the A* search from A to G
path, total_cost = a_star_search('A', 'G')

# Output the result
print("Path:", path)
print("Total cost:", total_cost)
