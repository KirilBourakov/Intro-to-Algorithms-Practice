from algorithm.counting import countingSort

class radixSort:
    def __init__(self, items) -> None:
        self.items = []
        self.highestOrder = len(str(max(items)))
        self.sorter = countingSort(items)
        pass

    def sort(self):
        for i in range(self.highestOrder):
            self.sorter.sortbyDigit(10**i)
        self.items = self.sorter.getItems()
            

    def __str__(self) -> str:
        return 'Radix Sort'
    
    def getItems(self):
        return self.items