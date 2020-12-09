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


class Graph:
    # Create a graph with v vertices
    def __init__(self, f):
        str_line = f.read().split('\n')
        self.V = int(str_line[0])
        self.E = int(str_line[1])
        self.adj = {}
        # if len(str_line) < self.E + 2:
        #     self.E = len(str_line) - 2
        #     print("Edges number error")
        #     return
        # Actually, it's unnecessary to input E
        self.E = 0
        for i in range(2, len(str_line)):
            str_vertice_pair = str_line[i].split(' ')
            # input edges pairs
            if len(str_vertice_pair) == 2:
                str_vertice_pair[0].replace(' ', '')
                str_vertice_pair[1].replace(' ', '')
                if not self.adj.__contains__(str_vertice_pair[0]):
                    self.adj[str_vertice_pair[0]] = []
                if not self.adj.__contains__(str_vertice_pair[1]):
                    self.adj[str_vertice_pair[1]] = []
                self.addEdge(str_vertice_pair[0], str_vertice_pair[1])
            # input single vertice
            elif len(str_vertice_pair) == 1:
                str_vertice_pair[0].replace(' ', '')
                self.adj[str_vertice_pair[0]] = []
        if len(self.adj) < self.V:
            self.V = len(self.adj)
            print("Vertices number error")
            return
        
    # Add an edge between v and w
    def addEdge(self, v, w):       
        self.adj[v].append(w) 
        self.adj[w].append(v)
        self.E += 1
    
    # Add an vertice
    def addVertice(self, v):
        if not self.adj.__contains__(v):
            self.adj[v] = []
            self.V += 1
       
    # Query all the vertices that connect to v directly
    def adjto(self, v):
        if not self.adj.__contains__(v):
            return None
        return self.adj[v]

    # Print all the vertices adjacent list
    def printAllAdj(self):
        print(self.adj)
    
    # Return the degree of v
    def degree(self, v):
        return len(self.adj[v])
    
    # Return the max degree of all graph
    def maxDegree(self):
        maxdegree = 0
        for v in self.adj.keys():
            if len(self.adj[v]) > maxdegree:
                maxdegree = len(self.adj[v])
        return maxdegree

    # Return the number of self loops
    def numberOfSelfLoops(self):
        count = 0
        for v in self.adj.keys():
            for w in self.adj[v]:
                if v == w:
                    count += 1
        return int(count / 2)

# Path searching algorithms (DFS)
class Path:
    # Find paths in graph from source s
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
        for w in self.graph.adjto(v):
            if self.marked[w] == False:
                self.dfs(w)
                self.edgeTo[w] = v

# Path searching algorithms (DFS)
class Path_b:
    # Find paths in graph
    def __init__(self, graph, s):
        self.graph = graph
        self.s = s
        self.marked = {}
        self.edgeTo = {}
        self.distTo = {}
        for v in self.graph.adj.keys():
            self.marked[v] = False
            self.edgeTo[v] = None
            self.distTo[v] = None
        self.BreadthFirstPaths()
    
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
    
    # Breadth First Search
    def BreadthFirstPaths(self):
        self.bfs(self.s)
    
    def bfs(self, s):
        q = Queue()
        dist_q = Queue()
        q.enqueue(s)
        dist_q.enqueue(0)
        self.marked[s] = True
        while not q.isEmpty():
            v = q.dequeue()
            v_dist = dist_q.dequeue()
            for w in self.graph.adjto(v):
                if not self.marked[w]:
                    q.enqueue(w)
                    dist_q.enqueue(v_dist + 1)
                    self.marked[w] = True
                    self.edgeTo[w] = v
                    self.distTo[w] = v_dist + 1
    
# Finding connected components with DFS
class CC:
    def __init__(self, graph):
        self.graph = graph
        self.marked = {}
        self.id = {}
        # Component id start from 1
        self.count = 1
        for v in graph.adj.keys():
            self.marked[v] = False
            self.id[v] = None
    
    # Find connected components
    def cc(self):
        for v in self.graph.adj.keys():
            if not self.marked[v]:
                # Run dfs from one vertex in each component
                self.dfs(v)
                self.count += 1

    # Return the number of components
    def cc_count(self):
        return self.count

    # Return the id of component containing v
    def cc_id(self, v):
        return self.id[v]

    # dfs search
    def dfs(self, v):
        self.marked[v] = True
        self.id[v] = self.count
        for w in self.graph.adjto(v):
            if not self.marked[w]:
                self.dfs(w)

    # Print all the components
    def cc_print(self):
        cc_list = {}
        n = self.cc_count()
        for i in range(1, n):
            cc_list[i] = []
        for v in self.graph.adj.keys():
            cc_list[self.id[v]].append(v)
        return cc_list

# Test Demo
f = open("graph.txt", "r", encoding="utf-8")
g = Graph(f)
print("The whole graph adjacent list:")
g.printAllAdj()
print("Vertices adjacent to vertice \"1\": " + str(g.adjto('1')))
print("Degree of vertice \"1\": " + str(g.degree('1')))
print("Max Degree of graph: " + str(g.maxDegree()))
print("Number of self loops: " + str(g.numberOfSelfLoops()))

# Path Searching (DFS)
path = Path(g, '0')
print("Path from 0 to 4: " + str(path.pathTo('4')))
print("Path from 0 to 7: " + str(path.pathTo('7')))

# Path Searching (BFS)
path = Path_b(g, '0')
print("Path from 0 to 4: " + str(path.pathTo('4')))
print("Path from 0 to 7: " + str(path.pathTo('7')))

# Find Connected Components with DFS
cc = CC(g)
cc.cc()
print("The graph contains {} components".format(cc.cc_count()))
print(cc.cc_print())
