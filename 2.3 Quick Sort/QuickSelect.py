import random

class UnitTest():

    def GenerateRandArray(self, n, min, max):
        arr = []
        arr = [random.randint(min, max) for x in range(n)]
        return arr

    def isSorted(self, alist):
        for i in range(len(alist) - 1):
            if alist[i] > alist[i + 1]:
                return False
        return True

class QuickSort():

    def Sort(alist):
        n = len(alist)
        lo, hi = 0, n - 1
        random.shuffle(alist)
        __Sort(alist, lo, hi)

    def __Sort(alist, lo, hi):
        
    
