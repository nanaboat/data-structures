# Test picked from
# https://github.com/jwasham/practice-python/blob/master/merge_sort/main.py


def is_sorted(numbers):
    last_num = float("-inf")
    in_order = True

    for n in numbers:
        if n < last_num:
            in_order = False
            break
        last_num = n

    return in_order


def contain_same_ints(arr1, arr2):
    for i in arr1:
        found = False
        for j in arr2:
            if i == j:
                found = True
                break
        if not found:
            return False

    return True


def check_sort(arr, arr1):
    print(arr)
    if is_sorted(arr):
        print("** SUCCESS! **")
    else:
        print("Uh oh - not in order.")

    if contain_same_ints(arr, arr1):
        print("** Contain the same elements! **")
    else:
        print("Uh oh - something is missing.")

    print("--------------------------------------")


def main():
    original = [325432, 989, 547510, 3, -93, 189019, 5042, 123,
                597, 42, 7506, 184, 184, 2409, 45, 824,
                4, -2650, 9, 662, 3928, -170, 45358, 395,
                842, 7697, 110, 14, 99, 221]

    numbers = original[:]

    mergeSort(original)

    check_sort(original, numbers)


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


if __name__ == '__main__':
    main()
