import operator

class Vertex:
    name = ""
    def __init__(self, name):
        self.name = name

    def print(self):
        print(self.name)

class Edge:
    vertexStart = None
    vertexEnd = None
    weight = 0
    def __init__(self, vertexStart, vertexEnd, weight):
        self.vertexStart = vertexStart
        self.vertexEnd = vertexEnd
        self.weight = weight
    
    def print(self):
        print("(" + self.vertexStart.name + " -> " + self.vertexEnd.name + " : " + str(self.weight) + ")")

class GraphEL:
    edgeList = None
    def __init__(self):
        self.edgeList = []

    def addEdge(self, edge):
        self.edgeList.append(edge)

    def print(self):
        for edge in self.edgeList:
            edge.print()

class UnionFind:
    map = None
    def __init__(self, set):
        i = 0
        self.map = dict()
        for element in set:
            self.map[element] = i
            i = i + 1
    
    def find(self, key):
        return self.map[key]

    def union(self, key1, key2):
        val1 = self.map[key1]
        val2 = self.map[key2]
        for key in self.map.keys():
            if self.map[key] == val2:
                self.map[key] = val1

    def print(self):
        for key in self.map.keys():
            print(key.name + ":" + str(self.map[key]) + " ", end="")
        print()

class GraphUtil:
    def mst(graph):
        vertices = set()
        for edge in graph.edgeList:
            vertices.add(edge.vertexStart)
            vertices.add(edge.vertexEnd)
        
        res = []
        uf = UnionFind(vertices)

        sortedEdgeList = list(graph.edgeList)
        sortedEdgeList.sort(key = operator.attrgetter("weight"))

        for edge in sortedEdgeList:
            val1 = uf.find(edge.vertexStart)
            val2 = uf.find(edge.vertexEnd)
            if val1 != val2:
                res.append(edge)
                uf.union(edge.vertexStart, edge.vertexEnd)

        return res

#   a---5---b
#   |       |
#   1       2
#   |       |
#   c--10---d

print("graph:")
a = Vertex("a")
b = Vertex("b")
ab = Edge(a, b, 5)
ba = Edge(b, a, 5)

c = Vertex("c")
d = Vertex("d")
cd = Edge(c, d, 10)
dc = Edge(d, c, 10)

ac = Edge(a, c, 1)

ca = Edge(c, a, 1)
bd = Edge(b, d, 2)
db = Edge(d, b, 2)

graph = GraphEL()
graph.addEdge(ab)
graph.addEdge(ba)
graph.addEdge(cd)
graph.addEdge(dc)
graph.addEdge(ac)
graph.addEdge(ca)
graph.addEdge(bd)
graph.addEdge(db)

graph.print()

print()
print("mst: ")
res = GraphUtil.mst(graph)
for edge in res:
    edge.print()
