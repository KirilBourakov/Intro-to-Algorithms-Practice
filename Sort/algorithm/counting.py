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

    def sortbyDigit(self, digit):
        final = [None] * len(self.items)
        counter = [0] * 10
        for item in self.items:
            last = (item // digit) % 10
            counter[last] += 1   
        for i in range(1, 10):
            counter[i] += counter[i-1]
        for i in range(len(self.items)-1, -1, -1):
            last = (self.items[i] // digit) % 10
            final[counter[last]-1] = self.items[i]
            counter[last] -= 1
        self.items = final

    def __str__(self) -> str:
        return 'Counting Sort'
    
    def getItems(self):
        return self.items