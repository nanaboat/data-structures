# Test picked from
# https://github.com/jwasham/practice-python/blob/master/merge_sort/main.py
from MergeSort import mergeSort


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


def main():
    original = [325432, 989, 547510, 3, -93, 189019, 5042, 123,
                597, 42, 7506, 184, 184, 2409, 45, 824,
                4, -2650, 9, 662, 3928, -170, 45358, 395,
                842, 7697, 110, 14, 99, 221]

    numbers = original[:]

    mergeSort(original)

    if is_sorted(original):
        print("** SUCCESS! **")
    else:
        print("Uh oh - not in order.")

    if contain_same_ints(original, numbers):
        print("** Contain the same elements! **")
    else:
        print("Uh oh - something is missing.")

    print(original)


if __name__ == '__main__':
    main()
