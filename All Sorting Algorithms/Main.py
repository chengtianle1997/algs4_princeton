from UnitTest import UnitTest
import time
import BubbleSort
import SelectionSort
import InsertionSort
import ShellSort
import MergeSort
import BottomUpMergeSort
import QuickSort
import ThreeWayQuickSort

n, min, max = 100000, -999999999, 999999999
rand_arr = UnitTest.GenerateRandArray(n, min, max)
'''
testarr = rand_arr[:]
# Bubble Sort
start_time = time.time()
BubbleSort.BubbleSort(testarr)
end_time = time.time()
if(not UnitTest.isSorted(testarr)):
    print("Sorting Error!\n")
print("Bubble Sort Time: {}\n".format(end_time - start_time))

testarr = rand_arr[:]
# Selection Sort
start_time = time.time()
SelectionSort.SelectionSort(testarr)
end_time = time.time()
if(not UnitTest.isSorted(testarr)):
    print("Sorting Error!\n")
print("Selection Sort Time: {}\n".format(end_time - start_time))

testarr = rand_arr[:]
# Insertion Sort
start_time = time.time()
InsertionSort.InsertionSort(testarr)
end_time = time.time()
if(not UnitTest.isSorted(testarr)):
    print("Sorting Error!\n")
print("Insertion Sort Time: {}\n".format(end_time - start_time))

testarr = rand_arr[:]
# Shell Sort
start_time = time.time()
ShellSort.ShellSort(testarr)
end_time = time.time()
if(not UnitTest.isSorted(testarr)):
    print("Sorting Error!\n")
print("Shell Sort Time: {}\n".format(end_time - start_time))

testarr = rand_arr[:]
# Merge Sort
start_time = time.time()
MergeSort.MergeSort(testarr)
end_time = time.time()
if(not UnitTest.isSorted(testarr)):
    print("Sorting Error!")
    print(testarr)
print("Merge Sort Time: {}\n".format(end_time - start_time))

testarr = rand_arr[:]
# Bottom-Up Merge Sort
start_time = time.time()
BottomUpMergeSort.BottomUpMergeSort(testarr)
end_time = time.time()
if(not UnitTest.isSorted(testarr)):
    print("Sorting Error!")
    print(testarr)
print("Bottom-Up Merge Sort Time: {}\n".format(end_time - start_time))
'''
testarr = rand_arr[:]
# Quick Sort
start_time = time.time()
QuickSort.QuickSort(testarr)
end_time = time.time()
if(not UnitTest.isSorted(testarr)):
    print("Sorting Error!")
    print(testarr)
print("Quick Sort Time: {}\n".format(end_time - start_time))

testarr = rand_arr[:]
# Three-Way Quick Sort
start_time = time.time()
ThreeWayQuickSort.ThreeWayQuickSort(testarr)
end_time = time.time()
if(not UnitTest.isSorted(testarr)):
    print("Sorting Error!")
    print(testarr)
print("Three-Way Quick Sort Time: {}\n".format(end_time - start_time))