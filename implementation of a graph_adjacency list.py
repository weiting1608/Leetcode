class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    # special method for print the connections of all vertices
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0 # like a vertice tracker counter

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key) # use the Vertex class here
        self.vertList[key] = newVertex # add this vertList[key] to the new object
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        # grab all the values in verList to iter object
        return iter(self.vertList.values()) 

g = Graph()
for i in range(6):
    g.addVertex(i)

g.vertList

g.addEdge(0,1,2)

for vertex in g:
    print(vertex)
    print(vertex.getConnections())
    print('\n')

# Example from GeekforGeeks
# Size of the array will be the no. of the vertices "V" 
# A class to represent the adjacency list of the node 
# class AdjNode: 
#     def __init__(self, data): 
#         self.vertex = data 
#         self.next = None
  
# class Graph: 
#     def __init__(self, vertices): 
#         self.V = vertices 
#         self.graph = [None] * self.V 
  
#     # Function to add an edge in an undirected graph 
#     def add_edge(self, src, dest): 
#         # Adding the node to the source node 
#         node = AdjNode(dest) 
#         node.next = self.graph[src] 
#         self.graph[src] = node 
  
#         # Adding the source node to the destination as 
#         # it is the undirected graph 
#         node = AdjNode(src) 
#         node.next = self.graph[dest] 
#         self.graph[dest] = node 
  
#     # Function to print the graph 
#     def print_graph(self): 
#         for i in range(self.V): 
#             print("Adjacency list of vertex {}\n head".format(i), end="") 
#             temp = self.graph[i] 
#             while temp: 
#                 print(" -> {}".format(temp.vertex), end="") 
#                 temp = temp.next
#             print(" \n") 
  
  
# # Driver program to the above graph class 
# if __name__ == "__main__": 
#     V = 5
#     graph = Graph(V) 
#     graph.add_edge(0, 1) 
#     graph.add_edge(0, 4) 
#     graph.add_edge(1, 2) 
#     graph.add_edge(1, 3) 
#     graph.add_edge(1, 4) 
#     graph.add_edge(2, 3) 
#     graph.add_edge(3, 4) 
  
#     graph.print_graph() 