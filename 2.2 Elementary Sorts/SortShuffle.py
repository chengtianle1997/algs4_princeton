from random import randint

def GenerateRandArray(n, min, max):
    arr = []
    arr = [randint(min, max) for x in range(n)]
    return arr

test_arr = GenerateRandArray(20, 0, 10)

# Take Shell Sort for example
# alist: random in range [0,1), nlist: to be shuffled
def ShellSort(alist, nlist):
    n = len(alist)
    h = 1
    # find the proper h value
    while(h < int(n/3)):
        h = 3*h + 1
    # decrease the h
    while(h >= 1):
        for i in range(h, n):
            for j in range(i, h-1, -h):
                if(alist[j] < alist[j-h]):
                    alist[j], alist[j-h] = alist[j-h], alist[j]
                    nlist[j], nlist[j-h] = nlist[j-h], nlist[j]
        h = int(h / 3)
    return alist, nlist

# Shuffle
def SortShuffle(nlist):
    n = len(nlist)
    alist = [randint(0, 1) for x in range(n)]
    alist, nlist = ShellSort(alist, nlist)
    return nlist

#Unit Test
print("SortShaffle:")
print("Origin Sequence: ")
print(test_arr)
res_arr = SortShuffle(test_arr)
print("Shuffled Sequence: ")
print(res_arr)
