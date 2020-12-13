# Index Minimum priority queue implement
# This client can insert and delete the minimum
# and change the key by specifying the index
class IndexMinPQ:
    def __init__(self):
        # node[i] to save extra info for keys[i]
        self.node = []
        # keys[i] is the priority of index i
        self.keys = []
        # pq[i] is the index of the key in heap position i
        # Note: the index of heap position start from 1
        self.pq = [None]
        # qp[i] is the heap position of the key with index i
        self.qp = []
        # N is the number of keys
        self.N = 0
    
    def isEmpty(self):
        return self.N == 0
    
    # Insert a key to the end
    def insert(self, node, key):
        self.N += 1
        self.node.append(node)
        self.keys.append(key)
        self.pq.append(len(self.node) - 1)
        self.qp.append(self.N)
        self.swim(self.N)

    # Delete the minimum
    def delMin(self):
        # Get the minKey
        minNode = self.node[self.pq[1]]
        minKey = self.keys[self.pq[1]]
        # Exchange the root with the end
        self.exch(1, self.N)
        # Exchange the key, node and qp to the end
        # self.node[self.pq[self.N]], self.node[len(self.node) - 1] = \
        #     self.node[len(self.node) - 1], self.node[self.pq[self.N]]
        # self.keys[self.pq[self.N]], self.keys[len(self.keys) - 1] = \
        #     self.keys[len(self.keys) - 1], self.keys[self.pq[self.N]]
        # self.qp[self.pq[self.N]], self.qp[len(self.qp) - 1] = \
        #     self.qp[len(self.qp) - 1], self.qp[self.pq[self.N]]
        # Delete the end
        # self.node.pop(self.N - 1)
        # self.keys.pop(self.N - 1)
        # self.qp.pop(self.N - 1)
        
        # delete operation: set qp as None and maintain key and node 
        # at the same position, check whether qp is None to ensure that
        # the key and node has been deleted or not
        self.qp[self.pq[self.N]] = None
        self.pq.pop(self.N)
        self.N -= 1
        # Sink to keep the order of heap
        self.sink(1)
        return minNode, minKey
    
    # Decrease the key of index i
    def decreaseKey(self, i, key):
        self.keys[i] = key
        self.swim(self.qp[i])

    # Whether contains node or not
    def contains(self, node):
        for i in range(len(self.node)):
            if node == self.node[i]:
                if not self.qp[i] == None:
                    return i
                else:
                    return False
        return False

    def swim(self, k):
        while k > 1 and self.more(int(k / 2), k):
            self.exch(int(k / 2), k)
            k = int(k / 2)
    
    def sink(self, k):
        # Remember to include the equal condition
        while 2 * k <= self.N:
            # Find the less child
            j = 2 * k
            if j < self.N and self.more(j, j + 1):
                j += 1
            # Compare the less child with parent
            if not self.more(k, j):
                break
            self.exch(k, j)
            # Set k = j to do cycling
            k = j

    def exch(self, i, j):
        self.qp[self.pq[i]], self.qp[self.pq[j]] = \
            self.qp[self.pq[j]], self.qp[self.pq[i]]
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
    
    def more(self, i, j):
        if self.keys[self.pq[i]] > self.keys[self.pq[j]]:
            return True
        else:
            return False
    
        
