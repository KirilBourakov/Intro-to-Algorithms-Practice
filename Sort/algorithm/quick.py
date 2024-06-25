class quickSort():
    def __init__(self, items) -> None:
        self.items = items.copy()
        self.inital_end = len(self.items) -1
    
    def sort(self, start, end=None):
        if end is None:
            end = self.inital_end
        if start < end:
            q = self.partition(start, end)
            self.sort(start, q)
            self.sort(q+1, end)

    def partition(self, start, end):
        pivot = self.items[start]
        left = start
        right = end
        while True:
            while self.items[right] > pivot:
                right -= 1
            while self.items[left] < pivot:
                left += 1
            if left < right:
                self.items[left], self.items[right] = self.items[right], self.items[left]
                left += 1
                right -= 1
            else:
                return right
        
    def __str__(self) -> str:
        return 'Quick Sort'
    
    def getItems(self):
        return self.items
            