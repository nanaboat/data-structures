from unittest import main, TestCase

# Implements the binary search algo for a sorted sequence.
# Binary search is O(logN)


def BinarySearch(aList, item):
    '''Search for an item in a given list. Uses the iterative method.
       Args:
         -aList: Python List
         -item: item being searched for (Integer)
       Returns:
         Returns a tuple of a boolean and index of item in list.
    '''
    start = 0
    stop = len(aList) - 1

    while start <= stop:
        mid = (stop + start) // 2
        if aList[mid] == item:
            return True, mid

        if aList[mid] > item:
            stop = mid - 1
        if aList[mid] < item:
            start = mid + 1
    return False, None


def RecursiveBinarySearch(aList, item, start, stop):
    '''Search for an item in a given list. Uses the recursive method.
       Args:
         -aList: Python List
         -item: item being searched for (Integer)
         -start: start index
         -stop: stop index
       Returns:
         Returns a tuple of a boolean and index of item in list.
    '''
    length = len(aList)
    if length == 0 or stop <= start:
        return False, None
    else:
        mid = (start + stop) // 2
        if aList[mid] == item:
            return True, mid
        else:
            if aList[mid] > item:
                stop = mid - 1
                return RecursiveBinarySearch(aList, item, start, stop)
            else:
                start = mid + 1
                return RecursiveBinarySearch(aList, item, start, stop)


class TestBinarySearch(TestCase):
    def test_search_empty_array(self):
        array = []
        val = (False, None)
        self.assertEqual(val, BinarySearch(array, 56))
        self.assertEqual(val, RecursiveBinarySearch(array, 56, 0, len(array)))

    def test_search_array(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        val = (True, 3)
        self.assertEqual(val, BinarySearch(array, 4))
        self.assertEqual(val, RecursiveBinarySearch(array, 4, 0, len(array)))

    def test_search_outside_array(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        val = (False, None)
        self.assertEqual(val, BinarySearch(array, 11))
        self.assertEqual(val, RecursiveBinarySearch(array, 11, 0, len(array)))


if __name__ == '__main__':
    main()
