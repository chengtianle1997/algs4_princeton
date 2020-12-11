import os
import MinPQ
import UnionFind
import Queue

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
    
    # Return all the edges
    def Edges(self):
        edge_list = []
        for v in self.adj.keys():
            for e in self.adj[v]:
                edge_list.append(e)
        return edge_list
    
    # Return all the vertices
    def Vertices(self):
        return list(self.adj.keys())

# Kruskal MST
class KruskalMST:
    def __init__(self, graph):
        self.graph = graph
        # MST queue
        self.mst = Queue.Queue()
        # Build priority queue
        pq = MinPQ.MinPQ()
        for e in graph.Edges():
            pq.insert(e)
        # Build union find to find cycle 
        # (instead of dfs: log*V(faster) for union-find and V(slower) for dfs)
        uf = UnionFind.UnionFind(graph.Vertices())
        # Cycle when pq is not empty and MST does not have enough nodes
        while not pq.isEmpty() and self.mst.size() < graph.V - 1:
            e = pq.delMin()
            v = e.either()
            w = e.other(v)
            # Ensure that edge v-w does not create cycle
            if not uf.connected(v, w):
                uf.union(v, w)
                self.mst.enqueue(e)
    
    # Return all the edges in MST
    def Edges(self):
        return self.mst.queue

    # Return the weigt
    def Weight(self):
        weight_sum = 0
        for e in self.mst.queue:
            weight_sum += e.weight
        return weight_sum

# Prim's MST (lazy implement)
class LazyPrimMST:
    def __init__(self, graph):
        self.graph = graph
        self.marked = {}
        self.mst = Queue.Queue()
        self.pq = MinPQ.MinPQ()
        for v in graph.Vertices():
            self.marked[v] = False
        # Visit the first vertice
        V = self.graph.Vertices()
        self.visit(V[0])
        # Cycle until pq is empty or MST have enough nodes
        while not self.pq.isEmpty() and self.mst.size() < self.graph.V - 1:
            e = self.pq.delMin()
            v = e.either()
            w = e.other(v)
            if self.marked[v] and self.marked[w]:
                continue
            self.mst.enqueue(e)
            if not self.marked[v]:
                self.visit(v)
            if not self.marked[w]:
                self.visit(w)

    # Return all the edges in MST
    def Edges(self):
        return self.mst.queue
    
    # Return weight
    def Weight(self):
        weight_sum = 0
        for e in self.mst.queue:
            weight_sum += e.weight
        return weight_sum

    # Visit v in the edge-weighted graph
    def visit(self, v):
        self.marked[v] = True
        for e in self.graph.adjTo(v):
            if not self.marked[e.other(v)]:
                self.pq.insert(e)

# Prim's MST (eager version)
class PrimMST:
    def __init__(self):
        # Shortest edge from tree vertex
        self.edgeTo = {}
        # distTo[w] = edgeTo[w].weight
        self.distTo = {}
        # true if v is on tree
        self.marked = {}
        # eligible crossing edges





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

# Kruskal MST
print("--- Kruskal Minimum Spanning Tree ---")
kruskal_mst = KruskalMST(ewg)
print(printAdjList(kruskal_mst.Edges()))
print("Weight Sum: " + str(kruskal_mst.Weight()))
print('\n')

# Prim's MST (lazy implement)
print("--- Prim's Minimum Spanning Tree (Lazy implement) ---")
lazy_prim_mst = LazyPrimMST(ewg)
print(printAdjList(lazy_prim_mst.Edges()))
print("Weight Sum: " + str(lazy_prim_mst.Weight()))
print('\n')


