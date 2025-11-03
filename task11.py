from queue import PriorityQueue

# Define the map as a graph
graph = {
    'A': {'B': 5, 'C': 9, 'D': 2},
    'B': {'E': 2},
    'C': {'F': 3},
    'D': {'G': 6},
    'E': {'H': 3},
    'F': {'I': 1},
    'G': {'J': 2},
    'H': {'Goal': 5},
    'I': {'Goal': 2},
    'J': {'Goal': 1},
    'Goal': {}
}

# Heuristic values (estimated cost to reach Goal)
heuristic = {
    'A': 10, 'B': 8, 'C': 5, 'D': 7,
    'E': 4, 'F': 3, 'G': 4,
    'H': 2, 'I': 1, 'J': 1, 'Goal': 0
}

def a_star_search(start, goal):
    open_list = PriorityQueue()
    open_list.put((0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while not open_list.empty():
        _, current = open_list.get()

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, g_score[goal]

        for neighbor, cost in graph[current].items():
            temp_g = g_score[current] + cost
            if temp_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g
                f = temp_g + heuristic[neighbor]
                open_list.put((f, neighbor))

    return None, float('inf')

# Run the A* Search
start_node = 'A'
goal_node = 'Goal'
path, cost = a_star_search(start_node, goal_node)

print("Optimal Path:", path)
print("Total Cost:", cost)

##Output:
# Optimal Path: ['A', 'D', 'G', 'J', 'Goal']
# Total Cost: 11