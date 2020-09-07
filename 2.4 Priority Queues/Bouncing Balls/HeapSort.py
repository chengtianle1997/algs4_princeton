class MaxPQ:
    def __init__(self):
        self.key = [None]
        self.N = 0
    
    def insert(self, key):
        self.N += 1
        self.key.append(key)
        self.swim(self.N)

    def delMax(self):
        Max = self.key[1]
        self.exch(1, self.N)
        self.N -= 1
        self.key[N + 1] = None
        sink(1)
        return Max
    
    def swim(self, k):
        # if parent less than child, swim up
        while k > 1 and self.less(int(k/2), k):
            self.exch(int(k/2), k)
            k = int(k/2)
        
    def sink(self, k):
        # if parent less than child, sink down
        # Check if child in the proper range (from 1 to N)
        while 2 * k <= self.N:
            j = 2 * k
            # Choose the larger child
            if j < self.N and self.less(j, j + 1):
                j += 1
            # Compare with the larger child
            if not self.less(k, j):
                break
            self.exch(k, j)
            k = j

    def exch(self, i, j):
        self.key[i], self.key[j] = self.key[j], self.key[i]
    
    def less(self, i, j):
        if self.key[i] < self.key[j]:
            return True
        else:
            return False

# in-place heap sort
def HeapSort(alist):
    pq = MaxPQ()
    pq.key = alist
    pq.N = len(alist)
    # The heap starts from 1
    pq.key.insert(0, None)
    # Build heap using bottom-up method
    for k in range(int(pq.N/2), 0, -1):
        pq.sink(k)
    # Sort Down
    while pq.N > 1:
        # Leave the max root at the end of the array instead of nulling out
        pq.exch(1, pq.N)
        pq.N -= 1
        pq.sink(1)
    return pq.key[1:]

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

if __name__ == '__main__':
    alist = GenerateRandArray(50, 0, 100)
    blist = HeapSort(alist)
    if isSorted(blist):
        print("The arr list is sorted!")
    else:
        print("Sort Error!")
        print(blist)