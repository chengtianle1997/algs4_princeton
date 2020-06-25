# Merge Sort
def MergeSort(alist):
    n = len(alist)
    lo, hi = 0, n-1
    __MergeSort(alist, lo, hi)
    
def InsertionSort(alist, lo, hi):
    for i in range(lo, hi + 1):
        for j in range(i, lo, -1):
            if (alist[j] < alist[j-1]):
                alist[j], alist[j-1] = alist[j-1], alist[j]
    

def __MergeSort(alist, lo, hi):
    if (hi - lo < 7):
        InsertionSort(alist, lo, hi)
        return
    # Avoid Large Num
    mid = int(lo + (hi - lo)/2)
    __MergeSort(alist, lo, mid)
    __MergeSort(alist, mid + 1, hi)
    Merge(alist, lo, mid, hi)


def Merge(alist, lo, mid, hi):
    i, j, k = lo, mid + 1, lo
    blist = alist[lo:hi+1]
    while (k <= hi):
        if(i > mid):
            alist[k] = blist[j-lo]
            j += 1
        elif(j > hi):
            alist[k] = blist[i-lo]
            i += 1
        elif(blist[i-lo] <= blist[j-lo]):
            alist[k] = blist[i-lo]
            i += 1
        else:
            alist[k] = blist[j-lo]
            j += 1
        k += 1
    
