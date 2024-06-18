def selectionSort(items):
    final = [None] * len(items)

    i = len(items) - 1
    while i >= 0:
        smallest = (float('inf'), float('inf'))
        j = i
        while j >= 0:
            if items[j] < smallest[0]:
                smallest = (items[j], j)
            j -= 1
        final[len(items) - 1 - i] = smallest[0]
        items[i], items[smallest[1]] = items[smallest[1]], items[i]
        i -= 1
    return final