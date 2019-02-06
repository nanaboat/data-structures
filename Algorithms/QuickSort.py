import random

# Difference between quickSort and quicksort methods is, for quicksort you randomize
# the list/array first before you start working on the list/array.
# For quickSort method I select a random integer as my pivot index everytime I try
# to partition the list/array.
# quicksort method should be slightly faster since you only randomize the array/list
# once while in quickSort method you randomize for every recursive call.
# Also for repeated numbers in your array/list use quicksort method or
# 3-way quicksort method

def quickSort(aList):
    _quickSort(aList, 0, len(aList) - 1)


def _quickSort(aList, first, last):
    if first < last:
        splitPoint = partition(aList, first, last)
        _quickSort(aList, first, splitPoint - 1)
        _quickSort(aList, splitPoint + 1, last)


def partition(aList, first, last):
    if first < last:
        pivot_index = random.randint(first, last)
        pivot = aList[pivot_index]

        #place the pivot the first index of array/list
        if pivot_index != first:
            aList[pivot_index], aList[first] = aList[first], aList[pivot_index]
            pivot_index = first
        i = first + 1
        j = last
        done = False

        while not done:
            while i <= j and aList[i] < pivot:
                i += 1

            while j >= i and aList[j] > pivot:
                j -= 1

            if i > j:
                done = True

            else:
                aList[i], aList[j] = aList[j], aList[i]

        aList[pivot_index], aList[j] = aList[j], aList[pivot_index]

        return j


def quicksort(alist):
    random.shuffle(alist)  # randomize the list/array
    _helper(alist, 0, len(alist) - 1)


def _helper(alist, start, end):
    if start < end:
        p_idx = _split(alist, start, end)
        _helper(alist, start, p_idx - 1)
        _helper(alist, p_idx + 1, end)


def _split(alist, first, last):
    if first < last:
        idx = first
        pivot = alist[idx]
        i = first + 1
        j = last

        while i <= j:
            if alist[i] <= pivot:
                i += 1
            elif alist[j] >= pivot:
                j -= 1
            else:
                alist[i], alist[j] = alist[j], alist[i]
        alist[idx], alist[j] = alist[j], alist[idx]
        return j


def three_way_quicksort(alist):
    '''improves performance for traditional quicksort algorithm when
       you have duplicates in your list/array.
    '''
    random.shuffle(alist)  # randomize the list/array
    _quickhelper(alist, 0, len(alist) - 1) 


def _quickhelper(alist, start, end):
    if start < end:
        p_idx1, p_idx2 = _partition(alist, start, end)
        _quickhelper(alist, start, p_idx1 - 1)
        _quickhelper(alist, p_idx2 + 1, end)


def _partition(alist, first, last):
    if first < last:
        idx = first
        pivot = alist[idx]
        i = first + 1
        j = last

        while i <= j:
            if alist[i] < pivot:
                alist[i], alist[idx] = alist[idx], alist[i]
                i += 1
                idx += 1
            elif alist[i] == pivot:
                i += 1
            elif alist[j] > pivot:
                j -= 1
            else:
                alist[i], alist[j] = alist[j], alist[i]

        return idx, j