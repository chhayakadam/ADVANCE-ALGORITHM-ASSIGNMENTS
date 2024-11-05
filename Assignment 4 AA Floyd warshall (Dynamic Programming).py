#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time

class Graph:
    def __init__(self):
        self.vertices = []
        self.index_map = {}  # Maps vertex names to their indices
        self.inf = float('inf')

    def add_vertex(self, vertex):
        if vertex not in self.index_map:
            self.index_map[vertex] = len(self.vertices)
            self.vertices.append(vertex)

    def add_edge(self, u, v, weight):
        u_index = self.index_map[u]
        v_index = self.index_map[v]
        self.dist[u_index][v_index] = weight

    def floyd_warshall(self):
        # Initialize the distance matrix
        for k in range(len(self.vertices)):
            for i in range(len(self.vertices)):
                for j in range(len(self.vertices)):
                    if self.dist[i][j] > self.dist[i][k] + self.dist[k][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]

    def display_shortest_paths(self):
        print("Shortest path distances between vertices:")
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if self.dist[i][j] == self.inf:
                    print(f"Distance from {self.vertices[i]} to {self.vertices[j]}: ∞")
                else:
                    print(f"Distance from {self.vertices[i]} to {self.vertices[j]}: {self.dist[i][j]}")

    def initialize_distance_matrix(self):
        size = len(self.vertices)
        self.dist = [[self.inf] * size for _ in range(size)]
        for i in range(size):
            self.dist[i][i] = 0  # Distance to itself is zero


def main():
    g = Graph()

    # Get user input for the graph
    num_vertices = int(input("Enter the number of vertices (minimum 10): "))
    if num_vertices < 10:
        print("You need to enter at least 10 vertices.")
        return

    print("Enter the vertices:")
    for _ in range(num_vertices):
        vertex = input("Vertex name: ").strip()
        g.add_vertex(vertex)

    g.initialize_distance_matrix()

    num_edges = int(input("Enter the number of edges: "))
    print("Enter the edges (vertex1 vertex2 weight):")
    for _ in range(num_edges):
        u, v, weight = input().split()
        g.add_edge(u, v, int(weight))

    # Start timing the Floyd-Warshall algorithm
    start_time = time.time()
    g.floyd_warshall()
    end_time = time.time()

    # Display the shortest paths
    g.display_shortest_paths()
    
    # Display the time taken to compute the solution
    print(f"Time taken to compute shortest paths: {end_time - start_time:.6f} seconds")


# Run the program
if __name__ == "__main__":
    main()

