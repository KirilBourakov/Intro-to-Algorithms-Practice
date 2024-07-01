import sys, time
import tester
from algorithm.insertion import insertionSort
from algorithm.merge import mergeSort
from algorithm.selection import selectionSort
from algorithm.heap import heapSort
from algorithm.quick import quickSort
from algorithm.counting import countingSort
from algorithm.radix import radixSort
from algorithm.bucket import bucketSort

def main(length):
    test = tester.Tester(length)
    test.time(selectionSort)
    test.time(mergeSort)
    test.time(insertionSort)
    test.timeClass(heapSort)
    test.timeClass(quickSort, 0)
    test.timeClass(countingSort)
    test.timeClass(radixSort)
    test.timeClassLimRange(bucketSort)

main(int(sys.argv[1]))
