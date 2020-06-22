from random import randint

def GenerateRandArray(n, min, max):
    arr = []
    arr = [randint(min, max) for x in range(n)]
    return arr

def isSorted(alist):
    for i in range(0, len(alist)-1):
        if alist[i] > alist[i+1]:
            return False
    return True

