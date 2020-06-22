# Selection Sort
def SelectionSort(alist):
    n = len(alist)
    for i in range(n - 1):
        min_index = i
        for j in range(i+1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist