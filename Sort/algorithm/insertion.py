def insertionSort(items):
    i = 1
    while i < len(items):
        inspected = items[i]
        j = i-1
        while j >= 0 and items[j] > inspected:
            items[j+1] = items[j]
            j -= 1
        items[j+1] = inspected
        i += 1

    return items        