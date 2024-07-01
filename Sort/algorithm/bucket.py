from algorithm.insertion import insertionSort
import copy

class bucketSort:
    def __init__(self, items):
        self.items = items.copy()
        self.buckets = copy.deepcopy([[] for _ in range(10)])

    def sort(self):
        for item in self.items:
            self.buckets[int(str(item)[2])].append(item)
        for i,li in enumerate(self.buckets):
            self.buckets[i] = insertionSort(li)
        final = []
        for bucket in self.buckets:
            final.extend(bucket)
        self.items = final

    def __str__(self) -> str:
        return 'Bucket Sort'
    
    def getItems(self):
        return self.items