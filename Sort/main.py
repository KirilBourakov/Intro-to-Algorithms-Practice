import sys
import tester
from algorithm.insertion import insertionSort
from algorithm.merge import mergeSort
from algorithm.selection import selectionSort

def main(length):
    test = tester.Tester(length)
    test.time(selectionSort)
    test.time(mergeSort)
    test.time(insertionSort)

main(int(sys.argv[1]))
