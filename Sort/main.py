import sys, time
import tester
from algorithm.insertion import insertionSort
from algorithm.merge import mergeSort
from algorithm.selection import selectionSort
from algorithm.heap import heapSort

def main(length):
    test = tester.Tester(length)
    test.time(selectionSort)
    test.time(mergeSort)
    test.time(insertionSort)
    test.timeClass(heapSort)

main(int(sys.argv[1]))
