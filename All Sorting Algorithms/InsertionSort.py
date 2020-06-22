# Insertion Sort
def InsertionSort(alist):
    n = len(alist)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
    return alist
    