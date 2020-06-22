# Bubble Sort
def BubbleSort(alist):
    n = len(alist)
    exchange = False
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                exchange = True
        if not exchange:
            break
    return alist    
