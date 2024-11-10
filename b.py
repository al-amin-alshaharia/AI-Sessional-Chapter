import random

def calculate_attacks(state):
    """Calculate the number of pairs of queens that are attacking each other."""
    attacks = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks

def get_neighbors(state):
    """Generate neighboring states by moving each queen in the column."""
    neighbors = []
    n = len(state)
    for col in range(n):
        for row in range(n):
            if state[col] != row:
                new_state = state[:]
                new_state[col] = row
                neighbors.append(new_state)
    return neighbors

def hill_climbing(initial_state):
    """Solve the N-Queens problem using the Hill Climbing algorithm."""
    current_state = initial_state
    current_attacks = calculate_attacks(current_state)

    while True:
        neighbors = get_neighbors(current_state)
        next_state = current_state
        next_attacks = current_attacks

        for neighbor in neighbors:
            attacks = calculate_attacks(neighbor)
            if attacks < next_attacks:
                next_state = neighbor
                next_attacks = attacks

        if next_attacks == current_attacks:
            break  # No better neighbors found

        current_state = next_state
        current_attacks = next_attacks

    return current_state, current_attacks

# Initial state from the image (Figure 2.1)
# Here, each index represents a column, and the value at each index represents the row position of the queen in that column.
initial_state = [0, 4, 7, 5, 2, 6, 1, 3]  # This is a sample initial state, replace with the exact state from Figure 2.1 if different.

# Run the hill climbing algorithm
solution, attacks = hill_climbing(initial_state)

# Output the result
print("Final state (solution):", solution)
print("Number of attacking pairs:", attacks)
