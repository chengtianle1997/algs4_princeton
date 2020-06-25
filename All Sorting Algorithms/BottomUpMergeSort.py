# Bottom-Up Merge Sort
def BottomUpMergeSort(alist):
    n = len(alist)
    sz = 1
    while (sz < n):    
        # |lo*****(sz)****lo+sz-1, lo+sz****(sz)****lo+sz+sz-1| 
        # For the last one consider condition : lo+sz+sz-1 > n , so we need to take the minimum of them
        for lo in range(0, n - sz, sz + sz):
            Merge(alist, lo, lo + sz - 1, min(lo + sz + sz -1, n - 1))
        sz += sz
        
        
def Merge(alist, lo, mid, hi):
    i, j, k = lo, mid + 1, lo
    # Copy valid part only to save time and space
    blist = alist[lo:hi+1]
    while (k <= hi):
        if (i > mid):
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





