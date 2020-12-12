# Index Minimum priority queue implement
# This client can insert and delete the minimum
# and change the key by specifying the index
class IndexMinPQ:
    def __init__(self):
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
    def insert(self, key):
        self.N += 1
        self.keys.append(key)
        self.pq.append(self.N - 1)
        self.qp.append(self.N)

    # Delete the minimum
    def delMin(self):
        # Get the minKey
        minKey = self.keys[self.pq[1]]
        # Exchange the root with the end
        self.exch(1, self.N)
        # Delete the end
        self.keys.pop(self.pq[self.N])
        self.qp.pop(self.pq[self.N])
        self.pq.pop(self.N)
        # Sink to keep the order of heap
        self.sink(1)
        return minKey
    
    # Decrease the key of index i
    def decreaseKey(self, i, key):
        self.keys[i] = key
        self.swim(self.qp[i])

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
    
        
