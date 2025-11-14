# ------------------------------
# Generic Graph Data Structure
# ------------------------------


class Graph:
    def __init__(self):
        # graph stores vertices and their outgoing connections
        self.graph = dict()

    def addVertex(self, vertex):
        # Adds a vertex to the graph if it doesn't already exist.
        if vertex in self.graph:
            print(f"Vertex '{vertex}' already exists.")
            return
        self.graph[vertex] = []

    def addEdge(self, from_vertex, to_vertex):
        # Adds a directed edge from one vertex to another.
        neighbours = self.graph[from_vertex]
        if to_vertex not in neighbours:
            neighbours.append(to_vertex)

    def removeEdge(self, from_vertex, to_vertex):
        # Removes a directed edge if it exists.
        neighbours = self.graph.get(from_vertex)
        if neighbours and to_vertex in neighbours:
            neighbours.remove(to_vertex)

    def listOutgoingAdjacentVertex(self, vertex):
        # Lists all vertices with outgoing edges from a given vertex.
        if vertex not in self.graph:
            print(f"Vertex '{vertex}' does not exist.")
            return []
        return self.graph[vertex]

    def listIncomingAdjacentVertex(self, vertex):
        # Lists all vertices that have an edge directed to the given vertex.
        incoming = []
        for v, neighbours in self.graph.items():
            if vertex in neighbours:
                incoming.append(v)
        return incoming

    def displayAllVertices(self):
        # Displays all vertices in the graph.
        return list(self.graph.keys())

    def __str__(self):
        result = "\nGraph:\n"
        result += "--------------------\n"
        for vertex, neighbours in self.graph.items():
            result += f"{vertex:<10} -> {neighbours}\n"
        return result
