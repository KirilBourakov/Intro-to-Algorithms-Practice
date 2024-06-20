class heapSort:
    def __init__(self, items) -> None:
        self.items = items.copy()
        self.heapsize = len(items)

    def heapify(self, i):
        left = self.getLeft(i)
        right = self.getRight(i)
        largest = i
        if left < self.heapsize and self.items[left] > self.items[i]:
            largest = left
        if right < self.heapsize and self.items[right] > self.items[largest]:
            largest = right
        if largest != i:
            self.items[i], self.items[largest] = self.items[largest], self.items[i]
            self.heapify(largest)

    def buildHeap(self):
        for i in range(len(self.items)//2, -1, -1):
            self.heapify(i)

    def sort(self):
        self.buildHeap()
        for i in range(len(self.items)-1, 0, -1):
            self.items[0], self.items[i] = self.items[i], self.items[0]
            self.heapsize -= 1
            self.heapify(0)


    def getParent(self, i):
        return max((i//2)-1, 0)
    def getLeft(self, i):
        return 2*(i+1)
    def getRight(self, i):
        return 2*(i+1)-1
    
    def __str__(self) -> str:
        return 'Heap Sort'
    
    def getItems(self):
        return self.items