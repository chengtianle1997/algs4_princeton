import random
# Quick Sort
def QuickSort(alist):
    shuffle(alist)
    

def shuffle(alist):
    n = len(alist)
    for i in range(n):
        j = random.randint(0, i)
        alist[i], alist[j] = alist[j], alist[i]

