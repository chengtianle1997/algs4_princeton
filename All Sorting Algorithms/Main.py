from UnitTest import UnitTest
import time
import BubbleSort
import SelectionSort
import InsertionSort
import ShellSort
import MergeSort
import BottomUpMergeSort

n, min, max = 1000000, -999999999, 999999999

testarr = UnitTest.GenerateRandArray(n, min, max)
'''
# Bubble Sort
start_time = time.time()
BubbleSort.BubbleSort(testarr)
end_time = time.time()
if(not UnitTest.isSorted(testarr)):
    print("Sorting Error!\n")
print("Bubble Sort Time: {}\n".format(end_time - start_time))

testarr = UnitTest.GenerateRandArray(n, min, max)
# Selection Sort
start_time = time.time()
SelectionSort.SelectionSort(testarr)
end_time = time.time()
if(not UnitTest.isSorted(testarr)):
    print("Sorting Error!\n")
print("Selection Sort Time: {}\n".format(end_time - start_time))

testarr = UnitTest.GenerateRandArray(n, min, max)
# Insertion Sort
start_time = time.time()
InsertionSort.InsertionSort(testarr)
end_time = time.time()
if(not UnitTest.isSorted(testarr)):
    print("Sorting Error!\n")
print("Insertion Sort Time: {}\n".format(end_time - start_time))

testarr = UnitTest.GenerateRandArray(n, min, max)
# Shell Sort
start_time = time.time()
ShellSort.ShellSort(testarr)
end_time = time.time()
if(not UnitTest.isSorted(testarr)):
    print("Sorting Error!\n")
print("Shell Sort Time: {}\n".format(end_time - start_time))
'''
testarr = UnitTest.GenerateRandArray(n, min, max)
# Merge Sort
start_time = time.time()
MergeSort.MergeSort(testarr)
end_time = time.time()
if(not UnitTest.isSorted(testarr)):
    print("Sorting Error!")
    print(testarr)
print("Merge Sort Time: {}\n".format(end_time - start_time))

testarr = UnitTest.GenerateRandArray(n, min, max)
# Bottom-Up Merge Sort
start_time = time.time()
BottomUpMergeSort.BottomUpMergeSort(testarr)
end_time = time.time()
if(not UnitTest.isSorted(testarr)):
    print("Sorting Error!")
    print(testarr)
print("Bottom-Up Merge Sort Time: {}\n".format(end_time - start_time))
