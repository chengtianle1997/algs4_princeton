# UnionFind implement
class UnionFind:
    def __init__(self, items):
        self.id = {}
        self.sz = {}
        for item in items:
            self.id[item] = item
            self.sz[item] = 1
    
    def add_item(self, item):
        if item == None:
            return
        self.id[item] = item
        self.sz[item] = 1

    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
            # path compression: 
            # make every other node in path point to its grandparent
            self.id[i] = self.id[self.id[i]]
        return i
    
    def connected(self, p, q):
        return self.root(p) == self.root(q)
    
    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        # If root j is larger
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        # If root i is larger
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
        


