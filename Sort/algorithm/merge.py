def merge(left, right):
    lp = 0
    rp = 0
    final = [None] * (len(left)+len(right))
    i = 0
    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            final[i] = left[lp]
            lp += 1
        else:
            final[i] = right[rp]
            rp += 1
        i += 1
    if lp < len(left):
        final[i:] = left[lp:]
    if rp < len(right):    
        final[i:] = right[rp:]
    return final


def mergeSort(items, s=0,e=None):
    final = []
    if e is None: e = len(items) - 1

    if e > s:
        n = (e+s) // 2
        left = mergeSort(items,s,n)
        right = mergeSort(items,n+1,e)
        final = merge(left,right)
    else:
        final = [items[e]]
    return final


# Create version to use insertion sort of small array