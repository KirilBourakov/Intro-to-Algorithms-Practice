def insertionSort(items):
    i = 1
    while i < len(items):
        inspected = items[i]
        j = i-1
        while j >= 0:
            if inspected <= items[j]:
                items[j], items[i] = inspected, items[j]
                i -= 1
            j -= 1
        i += 1
    return items        
x = [12, 6, 7, 15, 42, 0, 1, 8]
print(insertionSort(x))