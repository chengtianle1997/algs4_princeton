import os
import MinPQ.MinPQ as MinPQ
import UnionFind.UnionFind as UnionFind

# Weighted edge api
class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight
    
    # Either endpoint
    def either(self):
        return self.v
    
    # Other endpoint
    def other(self, v):
        if v == self.v:
            return self.w
        else:
            return self.v
    
    # Compare edges by weight
    def compareTo(self, that):
        if self.weight < that.weight:
            return -1
        elif self.weight > that.weight:
            return 1
        else:
            return 0

    # Convert to str
    def toString(self):
        # e_str = "[{}, {}, {}]".format(self.v, self.w, self.weight)
        e_str = [self.v, self.w, self.weight]
        return e_str


# Edge weighted graph api
class EdgeWeightedGraph:
    def __init__(self, V=0):
        self.V = V
        self.adj = {}
    
    # Read a edge weighted graph from txt file
    def fromFile(self, f):
        str_line = f.read().split('\n')
        for i in range(2, len(str_line)):
            str_edge = str_line[i].split(' ')
            # input edges
            if len(str_edge) == 3:
                str_edge[0].replace(' ', '')
                str_edge[1].replace(' ', '')
                str_edge[2].replace(' ', '')
                if not self.adj.__contains__(str_edge[0]):
                    self.adj[str_edge[0]] = []
                if not self.adj.__contains__(str_edge[1]):
                    self.adj[str_edge[1]] = []
                self.addEdge(str_edge[0], str_edge[1], float(str_edge[2]))
        self.V = len(self.adj)

    # Add an edge between v and w
    def addEdge(self, v, w, weight):
        e = Edge(v, w, weight)
        if not self.adj.__contains__(v):
            self.adj[v] = []
        if not self.adj.__contains__(w):
            self.adj[w] = []
        self.adj[v].append(e)
        self.adj[w].append(e)

    # Return all the edge connected to v
    def adjTo(self, v):
        if not self.adj.__contains__(v):
            return None
        return self.adj[v]

    # Print all the vertices adjacent list
    def printAllAdj(self):
        for v in self.adj.keys():
            edge_list = []
            for e in self.adj[v]:
                edge_list.append([e.v, e.w, e.weight])
            print("{}:{}".format(v, edge_list))

# Kruskal MST
class KruskalMST:
    def __init__(self, graph):
        self.graph = graph


def printAdjList(adj_list):
    adj_list_str = []
    for e in adj_list:
        adj_list_str.append(e.toString())
    return adj_list_str

# Test Demo
f = open("tinyEWG.txt", "r", encoding="utf-8")
ewg = EdgeWeightedGraph()
ewg.fromFile(f)
print("The whole graph adjacent list:")
ewg.printAllAdj()
print("Vertices adjacent to vertice \"6\": " + str(printAdjList(ewg.adjTo('6'))))
print('\n')

