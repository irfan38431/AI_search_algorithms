from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs_shortest_path(self, start, target):
        queue = deque([(start, [start])])
        visited = set()

        while queue:
            node, path = queue.popleft()
            visited.add(node)

            if node == target:
                return path

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

        return None

# Example usage
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 5)
graph.add_edge(2, 6)

start_node = 0
target_node = 4
result = graph.bfs_shortest_path(start_node, target_node)

if result:
    print(f"Shortest path from {start_node} to {target_node}: {result}")
else:
    print(f"No path found from {start_node} to {target_node}")
