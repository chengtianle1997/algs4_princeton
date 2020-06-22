# Shell Sort
def ShellSort(alist):
    n = len(alist)
    h = 1
    while (h < int(n/3)):
        h = 3*h + 1
    while(h >= 1):
        for i in range(h, n):
            for j in range(i, h-1, -h):
                if alist[j] < alist[j-h]:
                    alist[j], alist[j-h] = alist[j-h], alist[j]
        h = int(h/3)
    return alist