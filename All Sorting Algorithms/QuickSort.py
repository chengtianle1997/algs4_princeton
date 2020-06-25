import random
# Quick Sort
def QuickSort(alist):
    n = len(alist)
    lo, hi = 0, n - 1
    # Shuffle alist to avoid the worst case
    Shuffle(alist)
    Sort(alist, lo, hi)

def Sort(alist, lo, hi):
    if(hi <= lo):
        return
    if (hi - lo < 10):
        InsertionSort(alist, lo, hi)
    k = Partition(alist, lo, hi)
    # Sort the two sides of k
    Sort(alist, lo, k - 1)
    Sort(alist, k + 1, hi)

def Partition(alist, lo, hi):
    i, j = lo + 1, hi
    # Method 1 : Choose a base point randomly
    #k = random.randint(lo, hi)
    # Method 2 : Choose a base point by MedianOf3 (Faster)
    mid = int(lo + (hi - lo) / 2)
    k = MedianOf3(alist, lo, mid, hi)
    # swap k and lo first
    alist[k], alist[lo] = alist[lo], alist[k]
    while(True):
        while(alist[i] < alist[lo]):
            i += 1
            if(i >= hi):
                break
        while(alist[j] > alist[lo]):
            j -= 1
            if(j <= lo):
                break
        # i cross j
        if (i >= j):
            break
        # swap
        alist[i], alist[j] = alist[j], alist[i]
    # swap k to the proper position
    alist[lo], alist[j] = alist[j], alist[lo]
    return j

def MedianOf3(alist, lo, mid, hi):
    if((alist[lo] - alist[mid]) * (alist[lo] - alist[hi]) < 0):
        return lo
    elif((alist[mid] - alist[lo]) * (alist[mid] - alist[hi]) < 0):
        return mid
    else:
        return hi

def Shuffle(alist):
    n = len(alist)
    for i in range(n):
        j = random.randint(0, i)
        alist[i], alist[j] = alist[j], alist[i]

def InsertionSort(alist, lo, hi):
    for i in range(lo, hi + 1):
        for j in range(i, lo, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]

