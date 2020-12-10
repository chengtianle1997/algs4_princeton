# UnionFind implement
class UnionFind:
    def __init__(self, items):
        self.id = {}
        self.sz = {}
        for item in items:
            self.id[item] = item
            self.sz[item] = 1
    
    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
            # path compression
            self.id[i] = self.id[self.id[i]]
        return i
    
    def connected(self, p, q):
        return self.root(p) == self.root(q)
    
    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        



