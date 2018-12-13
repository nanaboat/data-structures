# Sorting functions
from unittest import main, TestCase


def bubble_sort(aList):
    for numpass in range(len(aList) - 1, 0, -1):
        for i in range(numpass):
            if aList[i] > aList[i + 1]:
                temp = aList[i]
                aList[i] = aList[i + 1]
                aList[i + 1] = temp


def ShortBubbleSort(aList):
    found = False
    numpass = len(aList) - 1
    while numpass > 0 and not found:
        found = True
        for i in range(numpass):
            if aList[i] > aList[i + 1]:
                temp = aList[i]
                aList[i] = aList[i + 1]
                aList[i + 1] = temp
                found = False
        numpass -= 1


def selection_sort(aList):
    for numpass in range(len(aList) - 1, 0, -1):
        maxpos = numpass
        for i in range(numpass):
            if aList[i] > aList[maxpos]:
                maxpos = i
        temp = aList[numpass]
        aList[numpass] = aList[maxpos]
        aList[maxpos] = temp


def insertion_sort(aList):
    for index in range(1, len(aList)):
        currentValue = aList[index]
        pos = index
        while pos > 0 and aList[pos - 1] > currentValue:
            aList[pos] = aList[pos - 1]
            pos -= 1
        aList[pos] = currentValue


def ShellSort(aList, increment):
    numSubList = len(aList) // increment

    while numSubList > 0:
        for startpos in range(numSubList):
            gapInsertionSort(aList, startpos, numSubList)
        print("After increments of size", numSubList, "the List is", aList)

        numSubList //= 2


def gapInsertionSort(aList, start, gap):
    for i in range(start + gap, len(aList), gap):
        currentValue = aList[i]
        pos = i
        while pos >= gap and aList[pos - gap] > currentValue:
            aList[pos] = aList[pos - gap]
            pos -= gap
        aList[pos] = currentValue


class TestSorting(TestCase):

    def is_sorted(self, numbers):
        last_num = float("-inf")
        in_order = True

        for n in numbers:
            if n < last_num:
                in_order = False
                break
            last_num = n

        return in_order

    def contain_same_ints(self, arr1, arr2):
        for i in arr1:
            found = False
            for j in arr2:
                if i == j:
                    found = True
                    break
            if not found:
                return False

        return True

    def test_insertion_sort(self):
        arr = [325432, 989, 547510, 3, -93, 189019, 5042, 123,
               597, 42, 7506, 184, 184, 2409, 45, 824,
               4, -2650, 9, 662, 3928, -170, 45358, 395,
               842, 7697, 110, 14, 99, 221]
        self.assertEqual(False, self.is_sorted(arr))
        insertion_sort(arr)
        self.assertEqual(True, self.is_sorted(arr))

    def test_bubble_sort(self):
        arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        self.assertEqual(False, self.is_sorted(arr))
        bubble_sort(arr)
        self.assertEqual(True, self.is_sorted(arr))

    def test_selection_sort(self):
        arr = [325432, 989, 547510, 3, -93, 189019, 5042, 123,
               597, 42, 7506, 184, 184, 2409, 45, 824,
               4, -2650, 9, 662, 3928, -170, 45358, 395,
               842, 7697, 110, 14, 99, 221]
        self.assertEqual(False, self.is_sorted(arr))
        selection_sort(arr)
        self.assertEqual(True, self.is_sorted(arr))


if __name__ == '__main__':
    main()
