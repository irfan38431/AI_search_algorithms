from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

    def bms(self, start, target):
        queue = deque([(start, [start])])
        visited = set()

        while queue:
            node, path = queue.popleft()

            if node == target:
                return path

            visited.add(node)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

        return None  # Target not reachable from start node

# Example usage
graph = Graph()
graph.add_edge('A', ['B', 'C'])
graph.add_edge('B', ['D', 'E'])
graph.add_edge('C', ['F'])
graph.add_edge('D', [])
graph.add_edge('E', ['F'])
graph.add_edge('F', [])

print("Shortest Path using British Museum Search:")
result = graph.bms('A', 'F')

if result:
    print(" -> ".join(result))
else:
    print("No path found from 'A' to 'F'")
