import numpy as np

# Define the initial and goal states
initial_state = np.array([[3, 8, 5],
                          [7, 1, None],
                          [2, 6, 4]], dtype=object)  # Use dtype=object for None values

goal_state = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, None]], dtype=object)

# Calculate Manhattan distance for heuristic
def manhattan_distance(state, goal):
    distance = 0
    for num in range(1, 9):  # Tiles 1 to 8
        x1, y1 = np.where(state == num)
        x2, y2 = np.where(goal == num)
        # Extract single integer values from arrays
        x1, y1, x2, y2 = int(x1[0]), int(y1[0]), int(x2[0]), int(y2[0])
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

# Find possible moves
def get_neighbors(state):
    neighbors = []
    x, y = np.where(state == None)  # Find the empty tile
    x, y = int(x[0]), int(y[0])  # Extract single integer values

    # Possible moves of the empty tile (up, down, left, right)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:  # Stay within bounds
            new_state = state.copy()
            # Swap empty tile with the neighboring tile
            new_state[x, y], new_state[nx, ny] = new_state[nx, ny], new_state[x, y]
            neighbors.append(new_state)
    return neighbors

# Hill Climbing algorithm
def hill_climbing(initial, goal):
    current_state = initial
    current_distance = manhattan_distance(current_state, goal)

    while True:
        neighbors = get_neighbors(current_state)
        next_state = current_state
        next_distance = current_distance

        for neighbor in neighbors:
            distance = manhattan_distance(neighbor, goal)
            if distance < next_distance:
                next_state = neighbor
                next_distance = distance

        # If no improvement, stop
        if next_distance == current_distance:
            break

        current_state = next_state
        current_distance = next_distance

    return current_state

# Run the algorithm
solution = hill_climbing(initial_state, goal_state)

# Output the final state
print("Final state reached by Hill Climbing:")
print(solution)
