class countingSort:
    def __init__(self, items) -> None:
        self.items = items.copy()
        self.k = max(items)
    
    def sort(self):
        final = [None] * len(self.items)
        counter = [0] * self.k
        for item in self.items:
            counter[item-1] += 1
        for i in range(1, self.k, 1):
            counter[i] += counter[i-1]
        for i in range(len(self.items)-1, -1, -1):
            final[counter[self.items[i]-1]-1] = self.items[i]
            counter[self.items[i]-1] -= 1
        self.items = final

    def __str__(self) -> str:
        return 'Counting Sort'
    
    def getItems(self):
        return self.items