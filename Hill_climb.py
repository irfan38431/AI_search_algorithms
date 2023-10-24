from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

def hill_climbing_search(graph, start, goal):
    current_node = start
    path = [current_node]

    while current_node != goal:
        neighbors = graph.graph[current_node]
        if not neighbors:
            break

        # Find the neighbor with the best heuristic (closest to the goal)
        next_node = min(neighbors, key=lambda x: heuristic(x, goal))

        if heuristic(next_node, goal) >= heuristic(current_node, goal):
            # If no neighbor is closer to the goal, stop climbing
            break

        current_node = next_node
        path.append(current_node)

    if current_node == goal:
        return path
    else:
        return None

def heuristic(node, goal):
    # Example heuristic: distance between nodes (can be customized for specific use cases)
    return abs(node - goal)

# Example usage
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 5)
graph.add_edge(4, 6)
graph.add_edge(5, 6)

start_node = 1
goal_node = 6

result = hill_climbing_search(graph, start_node, goal_node)

if result:
    print(f"Path from {start_node} to {goal_node}: {result}")
else:
    print(f"No path found from {start_node} to {goal_node}")

