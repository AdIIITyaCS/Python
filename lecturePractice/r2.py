# class Graph:
#     def __init__(self, vertices):
#         self.vertices = vertices
#         self.adj_matrix = []  # Initialize the matrix as an instance variable
#         for i in range(vertices):
#             row = []
#             for i in range(vertices):
#                 row.append(0)
#             self.adj_matrix.append(row)  # Move this line outside the inner loop

#     def add_edge(self, u, v):
#         self.adj_matrix[u][v] = 1
#         self.adj_matrix[v][u] = 1

#     def remove_edge(self, u, v):
#         self.adj_matrix[u][v] = 0
#         self.adj_matrix[v][u] = 0

#     def display_matrix(self):
#         for row in self.adj_matrix:
#             print(row)

# # Example usage
# num_vertices = 5
# graph = Graph(num_vertices)

# graph.add_edge(0, 1)
# graph.add_edge(0, 2)
# graph.add_edge(1, 3)
# graph.add_edge(3, 4)

# print("Initial adjacency matrix:")
# graph.display_matrix()

# print("\nAdding edge between 2 and 4:")
# graph.add_edge(2, 4)
# graph.display_matrix()

# print("\nRemoving edge between 1 and 3:")
# graph.remove_edge(1, 3)
# graph.display_matrix()


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = []  # Initialize the matrix as an instance variable
        for i in range(vertices):
            row = []
            for i in range(vertices):
                row.append(0)
            self.adj_matrix.append(row)  # Move this line outside the inner loop

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def remove_edge(self, u, v):
        self.adj_matrix[u][v] = 0
        self.adj_matrix[v][u] = 0

    def display_matrix(self):
        for row in self.adj_matrix:
            print(row)

# Example usage
num_vertices = int(input("No. of vertices you want:: "))
graph = Graph(num_vertices)

capacity=4

for i in range(capacity):
    u=int(input("enter edge as u/v: "))
    v=int(input("enter edge as v/u: "))
    graph.add_edge(u, v)

print("Initial adjacency matrix:")
graph.display_matrix()

print("\nAdding vertex between add_u and add_v:")
add_u=int(input("1st vertex you want to add: "))
add_v=int(input("2nd vertex you want to add: "))
graph.remove_edge(add_u,add_v)
graph.display_matrix()

print("\nRemoving edge between rev_u and rev_v:")
rev_u=int(input("1st vertex you want to remove: "))
rev_v=int(input("2nd vertex you want to remove: "))
graph.remove_edge(rev_u,rev_v)
graph.display_matrix()
