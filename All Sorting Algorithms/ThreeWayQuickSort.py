import random
# import sys
# sys.setrecursionlimit(1000000)

# Three-Way Quick Sort
def ThreeWayQuickSort(alist):
    n = len(alist)
    Shuffle(alist)
    lo, hi = 0, n-1
    Sort(alist, lo, hi)

def Sort(alist, lo, hi):
    if (hi <= lo):
        return
    if (hi - lo < 10):
        InsertionSort(alist, lo, hi)
        return
    lt, gt = Partition(alist, lo, hi)
    Sort(alist, lo, lt - 1)
    Sort(alist, gt + 1, hi)

# Partition   
def Partition(alist, lo, hi):
    # Find the base point by MedianOf3
    k = MedianOf3(alist, lo, int(lo + (hi - lo) / 2), hi)
    alist[k], alist[lo] = alist[lo], alist[k]
    v = alist[lo]
    i, lt, gt = lo + 1, lo + 1, hi
    # | lo **** ( < v ) **** lt **** ( = v ) **** i **** ( unknown ) **** gt **** ( > v ) **** hi |
    while(i <= gt):
        if(alist[i] > v):
            alist[i], alist[gt] = alist[gt], alist[i]
            gt -= 1
        elif(alist[i] < v):
            alist[i], alist[lt] = alist[lt], alist[i]
            i += 1
            lt += 1
        else:
            i += 1
    # | lo **** ( < v ) **** lt **** ( = v ) **** (i) , gt **** ( > v ) **** hi |
    return lt, gt


def MedianOf3(alist, lo, mid, hi):
    if((alist[lo] - alist[mid]) * (alist[lo] - alist[hi]) < 0):
        return lo
    elif((alist[mid] - alist[lo]) * (alist[mid] - alist[hi]) < 0):
        return mid
    else:
        return hi

# Shuffle
def Shuffle(alist):
    n = len(alist)
    for i in range(1, n):
        j = random.randint(0, i)
        alist[i], alist[j] = alist[j], alist[i]

def InsertionSort(alist, lo, hi):
    for i in range(lo, hi + 1):
        for j in range(i, lo, -1):
            if(alist[j] < alist[j-1]):
                alist[j], alist[j-1] = alist[j-1], alist[j]