#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Graph:
    def __init__(self):
        self.graph = {}
        self.edges = []

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v, weight):
        if u in self.graph and v in self.graph:  # Ensure vertices exist
            self.graph[u].append((v, weight))
            self.edges.append((u, v, weight))
        else:
            print(f"Error: One or both vertices '{u}' or '{v}' do not exist.")

    def display(self):
        print("Graph representation (Adjacency List):")
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

    def find_negative_cycle(self, parent, start):
        # Start from any vertex that was relaxed in the last iteration
        cycle = []
        current = start
        visited = set()

        while current not in visited:
            visited.add(current)
            current = parent[current]

        # To find the cycle, keep track of the cycle vertices
        cycle_start = current
        cycle.append(cycle_start)

        current = parent[cycle_start]
        while current != cycle_start:
            cycle.append(current)
            current = parent[current]

        cycle.append(cycle_start)
        cycle.reverse()  # Reverse to get the correct order
        return cycle

    def bellman_ford(self, start):
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0
        parent = {vertex: None for vertex in self.graph}

        for _ in range(len(self.graph) - 1):
            for u, v, weight in self.edges:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    parent[v] = u

        # Check for negative-weight cycles
        for u, v, weight in self.edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                print("Graph contains a negative-weight cycle:")
                cycle = self.find_negative_cycle(parent, v)
                print("Negative Cycle:", " -> ".join(cycle))
                return None

        return distances


def main():
    g = Graph()
    num_vertices = int(input("Enter the number of vertices: "))
    print("Enter the vertices:")
    for _ in range(num_vertices):
        vertex = input("Vertex name: ").strip()
        g.add_vertex(vertex)

    num_edges = int(input("Enter the number of edges: "))
    print("Enter the edges (vertex1 vertex2 weight):")
    for _ in range(num_edges):
        try:
            u, v, weight = input().split()
            g.add_edge(u, v, int(weight))
        except ValueError:
            print("Invalid input. Please enter edge details in the format: vertex1 vertex2 weight")

    g.display()

    start_vertex = input("Enter the starting vertex for shortest path calculations: ").strip()
    if start_vertex not in g.graph:
        print(f"Error: Vertex '{start_vertex}' does not exist.")
        return

    distances = g.bellman_ford(start_vertex)

    if distances:
        print(f"Shortest distances from vertex {start_vertex}:")
        for vertex, distance in distances.items():
            print(f"Distance to {vertex}: {distance}")

if __name__ == "__main__":
    main()


# In[ ]:




