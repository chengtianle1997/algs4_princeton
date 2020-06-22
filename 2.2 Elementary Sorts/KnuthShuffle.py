from random import randint

def GenerateRandArray(n, min, max):
    arr = []
    arr = [randint(min, max) for x in range(n)]
    return arr

test_arr = GenerateRandArray(20, 0, 10)

# Knuth Shuffle
def KnuthShuffle(nlist):
    n = len(nlist)
    for i in range(1, n):
        rand = randint(0, i-1)
        nlist[i], nlist[rand] = nlist[rand], nlist[i]
    return nlist

#Unit Test
print("KnuthShaffle:")
print("Origin Sequence: ")
print(test_arr)
res_arr = KnuthShuffle(test_arr)
print("Shuffled Sequence: ")
print(res_arr)
