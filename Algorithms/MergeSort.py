# Mergesort Algorithm
def mergeSort(aList):
    '''sort a list using mergesort method.'''
    start = 0
    end = len(aList) - 1
    _mergeSort(aList, start, end)


def _mergeSort(aList, first, last):
    '''Function that implements the mergesort algorithm'''
    if first < last:
        mid = (first + (last - 1)) // 2
        _mergeSort(aList, first, mid)
        _mergeSort(aList, mid + 1, last)
        merge(aList, first, mid, last)


def merge(aList, first, mid, last):
    '''Merge two sorted lists.'''
    sList = []
    i = first
    j = mid + 1

    while i <= mid and j <= last:
        if aList[i] <= aList[j]:
            sList.append(aList[i])
            i += 1
        else:
            sList.append(aList[j])
            j += 1

    while i <= mid:
        sList.append(aList[i])
        i += 1
    while j <= last:
        sList.append(aList[j])
        j += 1

    for index, val in enumerate(sList):
        aList[first + index] = val
