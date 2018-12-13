# Test picked from
# https://github.com/jwasham/practice-python/blob/master/merge_sort/main.py
import random


def quickSort(aList):
    _quickSort(aList, 0, len(aList) - 1)


def _quickSort(aList, first, last):
    if first < last:
        splitPoint = partition(aList, first, last)
        _quickSort(aList, first, splitPoint - 1)
        _quickSort(aList, splitPoint + 1, last)


def partition(aList, first, last):
    if first == last:
        return
    pivot_index = random.randint(first, last)
    pivot = aList[pivot_index]

    # place pivot at the the left
    if pivot_index != first:
        aList[pivot_index], aList[first] = aList[first], aList[pivot_index]
        pivot_index = first
    i = first + 1
    j = last
    done = False

    while not done:
        while i <= j and aList[i] <= pivot:
            i += 1

        while j >= i and aList[j] >= pivot:
            j -= 1

        if i > j:
            done = True

        else:
            aList[i], aList[j] = aList[j], aList[i]

    aList[pivot_index], aList[j] = aList[j], aList[pivot_index]

    return j


# Test methods
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

    quickSort(original)

    check_sort(original, numbers)


if __name__ == '__main__':
    main()
