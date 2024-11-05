#!/usr/bin/env python
# coding: utf-8

# In[6]:


from collections import deque, defaultdict

class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)  # Adjacency list representation
        self.directed = directed

    # Add a vertex to the graph
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    # Add an edge to the graph
    def add_edge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)
        if not self.directed:
            self.graph[vertex2].append(vertex1)

    # Perform BFS traversal from a given start vertex
    def bfs(self, start_vertex):
        visited = set()  # Set to keep track of visited vertices
        queue = deque([start_vertex])  # Queue for BFS traversal
        visited.add(start_vertex)
        
        bfs_order = []  # List to store BFS traversal order

        while queue:
            vertex = queue.popleft()  # Pop the first vertex in the queue
            bfs_order.append(vertex)  # Add the current vertex to BFS order

            # Explore all the adjacent vertices
            for adjacent_vertex in self.graph[vertex]:
                if adjacent_vertex not in visited:
                    queue.append(adjacent_vertex)
                    visited.add(adjacent_vertex)
        
        return bfs_order

    # Display the graph structure
    def display_graph(self):
        print("\nGraph Representation (Adjacency List):")
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {', '.join(edges)}")

# Main function to demonstrate BFS on a graph
def main():
    # Create a directed or undirected graph (choose True/False)
    is_directed = input("Is the graph directed? (yes/no): ").lower() == 'yes'
    
    # Create a graph object (directed or undirected based on input)
    g = Graph(directed=is_directed)

    # Add vertices and edges
    num_vertices = int(input("\nEnter the number of vertices: "))
    print("Enter the vertices:")
    for _ in range(num_vertices):
        vertex = input("Vertex name: ")
        g.add_vertex(vertex)
    
    num_edges = int(input("\nEnter the number of edges: "))
    print("Enter the edges (vertex1 vertex2):")
    for _ in range(num_edges):
        v1, v2 = input().split()
        g.add_edge(v1, v2)
    
    # Display the graph structure
    g.display_graph()

    # Perform BFS traversal
    start_vertex = input("\nEnter the start vertex for BFS traversal: ")
    bfs_result = g.bfs(start_vertex)
    
    # Display BFS traversal order
    print("\nBFS Traversal Order:")
    print(" -> ".join(bfs_result))

# Run the program
if __name__ == "__main__":
    main()


# In[7]:


class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, v1, v2):
        # Add edge for directed graph
        self.graph[v1].append(v2)

    def dfs_util(self, vertex, visited):
        # Mark the current vertex as visited
        visited.add(vertex)
        print(vertex, end=' ')

        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start_vertex):
        # Set to keep track of visited vertices
        visited = set()

        # Call the recursive helper function to perform DFS
        print(f"DFS starting from vertex {start_vertex}:")
        self.dfs_util(start_vertex, visited)
        print()

# Main function to run the program
def main():
    # Create a graph object
    g = Graph()

    # Get user input
    is_directed = input("Is the graph directed? (yes/no): ").lower() == 'yes'

    num_vertices = int(input("Enter the number of vertices: "))
    print("Enter the vertices:")
    for _ in range(num_vertices):
        vertex = input("Vertex name: ").strip()
        g.add_vertex(vertex)

    num_edges = int(input("Enter the number of edges: "))
    print("Enter the edges (vertex1 vertex2):")
    for _ in range(num_edges):
        v1, v2 = input().split()
        g.add_edge(v1, v2)
        if not is_directed:
            g.add_edge(v2, v1)

    # Perform DFS starting from a specified vertex
    start_vertex = input("Enter the starting vertex for DFS: ").strip()
    g.dfs(start_vertex)

# Run the program
if __name__ == "__main__":
    main()


# In[ ]:




