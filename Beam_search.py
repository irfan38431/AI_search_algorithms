from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def beam_search(self, start, target, beam_size):
        priority_queue = PriorityQueue()
        priority_queue.put((0, [start]))
        beam = []

        while not priority_queue.empty() and len(beam) < beam_size:
            _, path = priority_queue.get()
            node = path[-1]

            if node == target:
                return path, len(beam) + 1

            if node in self.graph:
                for neighbor, weight in self.graph[node]:
                    new_path = path + [neighbor]
                    priority_queue.put((weight, new_path))

            beam.append(path)

        return None, len(beam)

# Example usage
graph = Graph()
graph.add_edge(0, 1, 2)
graph.add_edge(0, 2, 5)
graph.add_edge(1, 3, 4)
graph.add_edge(1, 4, 2)
graph.add_edge(2, 5, 1)
graph.add_edge(2, 6, 7)

start_node = 0
target_node = 4

# Get beam size from user
beam_size = int(input("Enter the beam size: "))

shortest_path, beam_size_used = graph.beam_search(start_node, target_node, beam_size)

if shortest_path:
    print(f"Shortest path from {start_node} to {target_node}: {shortest_path}")
    print(f"Beam size used: {beam_size_used}")
else:
    print(f"No path found from {start_node} to {target_node}")
    print(f"Beam size used: {beam_size_used}")
