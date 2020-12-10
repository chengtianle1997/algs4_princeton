# Minimum priority queue implement
class MinPQ:
    # In the binary heap, item index starts from 1
    # k's parent is int(k/2), k's child are 2*k and 2*k+1
    def __init__(self):
        self.key = [None]
        self.N = 0
    
    def isEmpty(self):
        return self.N == 0
    
    # Insert a key to the end
    def insert(self, key):
        # Insert a key to the end
        self.N += 1
        self.key.append(key)
        # Swim up
        self.swim(self.N)
    
    # Delete the minimum
    def delMin(self):
        # Get the minKey
        minKey = self.key[1]
        # Exchange the root with the end
        self.exch(1, self.N)
        # Delete the end
        self.key[self.N] = None
        self.N -= 1
        # Sink to keep the order of heap
        self.sink(1)
        return minKey
    
    def swim(self, k):
        while k > 1 and self.more(int(k / 2), k):
            self.exch(int(k / 2), k)
            k = int(k / 2)

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
            # Set k = j to do cycling
            k = j
            
    def exch(self, i, j):
        self.key[i], self.key[j] = self.key[j], self.key[i]
    
    def more(self, i, j):
        if self.key[i].weight > self.key[j].weight:
            return True
        else:
            return False
    