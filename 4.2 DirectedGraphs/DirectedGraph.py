import os

# Stack implement
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0

# Queue implement
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0

# Directed Graph
class DiGraph:
    def __init__(self, V=0, E=0):
        self.V = V
        self.E = E
        self.adj = {}
        
    
    def FromFile(self, f):
        str_line = f.read().split('\n')
        # if len(str_line) < self.E + 2:
        #     self.E = len(str_line) - 2
        #     print("Edges number error")
        #     return
        # Actually, it's unnecessary to input E
        self.E = 0
        for i in range(2, len(str_line)):
            str_edge = str_line[i].split(' ')
            # input edges
            if len(str_edge) == 2:
                str_edge[0].replace(' ', '')
                str_edge[1].replace(' ', '')
                if not self.adj.__contains__(str_edge[0]):
                    self.adj[str_edge[0]] = []
                if not self.adj.__contains__(str_edge[1]):
                    self.adj[str_edge[1]] = []
                self.addEdge(str_edge[0], str_edge[1])
            # input single vertice
            elif len(str_edge) == 1:
                str_edge[0].replace(' ', '')
                self.adj[str_edge[0]] = []
        if len(self.adj) < self.V:
            self.V = len(self.adj)
            print("Vertices number error")
            return

    # Add an edge from v to w
    def addEdge(self, v, w):
        if not self.adj.__contains__(v):
            self.adj[v] = []       
        self.adj[v].append(w) 
        self.E += 1
    
    # Add an vertice
    def addVertice(self, v):
        if not self.adj.__contains__(v):
            self.adj[v] = []
            self.V += 1
    
    # Query all the vertices that are pointed directly from v
    def FromV(self, v):
        if not self.adj.__contains__(v):
            return None
        return self.adj[v]
    
    # Print all the vertices adjacent list
    def printAllAdj(self):
        print(self.adj)

    # Return the out degree of v
    def outDegree(self, v):
        if not self.adj.__contains__(v):
            return None
        return len(self.adj[v])
    
    # Reverse all the edges
    def reverse(self):
        new_DiGraph = DiGraph(V=self.V)
        for v in self.adj.keys():
            for w in self.adj[v]:
                new_DiGraph.addEdge(w, v)
        return new_DiGraph

# Path searching algorithms (DFS)
class Path:
    def __init__(self, graph, s):
        self.graph = graph
        self.s = s
        self.marked = {}
        self.edgeTo = {}
        for v in self.graph.adj.keys():
            self.marked[v] = False
            self.edgeTo[v] = None
        self.DepthFirstPaths()
        
    # Is there a path from s to v
    def hasPathTo(self, v):
        return self.marked[v]

    # Path from s to v, return None if no such path
    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        path = Stack()
        x = v
        while not x == self.s:
            path.push(x)
            x = self.edgeTo[x]
        path.push(self.s)
        # Reverse the path by pop opt
        path_ret = []
        while not path.isEmpty():
            path_ret.append(path.pop())
        return path_ret
    
    # Depth first search
    def DepthFirstPaths(self):
        self.dfs(self.s)
    
    def dfs(self, v):
        self.marked[v] = True
        for w in self.graph.FromV(v):
            if self.marked[w] == False:
                self.dfs(w)
                self.edgeTo[w] = v
    


# Test Demo
f = open("tinyDG.txt", "r", encoding="utf-8")
g = DiGraph()
g.FromFile(f)
print("The whole graph adjacent list:")
g.printAllAdj()
print("Vertices adjacent to vertice \"6\": " + str(g.FromV('6')))

# Reverse test
gr = g.reverse()
print("The whole reverse graph adjacent list:")
gr.printAllAdj()

# Path Searching (DFS)
path = Path(g, '0')
print("Path from 0 to 2: " + str(path.pathTo('2')))
print("Path from 0 to 7: " + str(path.pathTo('7')))