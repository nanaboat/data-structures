# Test picked from
# https://github.com/jwasham/practice-python/blob/master/merge_sort/main.py
# Test methods

from MergeSort import *
from QuickSort import *


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

def test_mergesort():
    original = [325432, 989, 547510, 3, -93, 189019, 5042, 123,
                597, 42, 7506, 184, 184, 2409, 45, 824,
                4, -2650, 9, 662, 3928, -170, 45358, 395,
                842, 7697, 110, 14, 99, 221]

    numbers = original[:]

    mergeSort(original)

    check_sort(original, numbers)

def test_quickSort():
    original = [325432, 989, 547510, 3, -93, 189019, 5042, 123,
                597, 42, 7506, 184, 2409, 45, 824,
                4, -2650, 9, 662, 3928, -170, 45358, 395,
                842, 7697, 110, 14, 99, 221] 

    numbers = original[:]

    quickSort(original)
    check_sort(original, numbers)

def test_quicksort():
    original = [325432, 989, 547510, 3, -93, 189019, 5042, 123,
                597, 42, 7506, 184, 184, 2409, 45, 824,
                4, -2650, 9, 662, 3928, -170, 45358, 395,
                842, 7697, 110, 14, 99, 221,5, 5, 5, 6, 7, 4, 5,
                6, 7, 8, 8, 8, 8, 8, 8]
    test = original[:]
    quicksort(original)
    check_sort(original, test)

def test_three_way_quicksort():
    original = [325432, 989, 547510, 3, -93, 189019, 5042, 123,
                597, 42, 7506, 184, 184, 2409, 45, 824,
                4, -2650, 9, 662, 3928, -170, 45358, 395,
                842, 7697, 110, 14, 99, 221,5, 5, 5, 6, 7, 4, 5,
                6, 7, 8, 8, 8, 8, 8, 8]
    test = original[:]
    three_way_quicksort(original)
    check_sort(original, test)


if __name__ == "__main__":
    test_mergesort()
    test_quickSort()
    test_quicksort()
    test_three_way_quicksort()
