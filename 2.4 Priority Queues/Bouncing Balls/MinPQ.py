class MinPQ:
    # In the Binary heap, k's parent is k/2(int), k's child is 2*k and 2*k+1
    # Note that the index of the root is 1 
    def __init__(self):
        # Initialize
        self.key = [None]
        self.N = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def insert(self, key):
        # Insert a key to the end
        self.N += 1
        # self.key[self.N] = key
        self.key.append(key)
        self.swim(self.N)
    
    def delMin(self):
        # Get the minKey
        minKey = self.key[1]
        # Exchange the root with the end
        self.exch(1, self.N)
        # Delete the end
        self.key[self.N] = None
        self.N -= 1
        # Sink Approach to keep the order of the heap
        self.sink(1)
        return minKey

    def swim(self, k):
        while k > 1 and self.more(int(k/2), k):
            self.exch(k, int(k/2))
            k = int(k/2)

    def sink(self, k):
        # Remember to include the equal condition
        while(2 * k <= self.N):
            # Find the less child
            j = 2 * k
            if j < self.N and self.more(j, j + 1):
                j += 1
            # Compare the less child with parent
            if not self.more(k, j):
                break
            self.exch(k, j)
            # set k = j to iterate
            k = j
    
    def exch(self, i, j):
        self.key[i], self.key[j] = self.key[j], self.key[i]
    
    def more(self, i, j):
        if self.key[i] > self.key[j]:
            return True
        else:
            return False

# Test Demo
from random import randint

def GenerateRandArray(n, min, max):
    arr = []
    arr = [randint(min, max) for x in range(n)]
    return arr

# Check sorting in ascending order
def isSorted(alist):
    for i in range(len(alist) - 1):
        if alist[i] > alist[i + 1]:
            return False
    return True

def SortTest(alist):
    pq = MinPQ()
    blist = []
    # Insert Operation
    for i in range(len(alist)):
        pq.insert(alist[i])
    # DelMax Operation
    for j in range(len(alist)):
        blist.append(pq.delMin())
    return blist

if __name__ == '__main__':
    alist = GenerateRandArray(30000, 0, 10000)
    blist = SortTest(alist)
    if isSorted(blist):
        print("The arr list is sorted!")
    else:
        print("Sort Error!")
        print(blist)