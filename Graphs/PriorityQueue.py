# Prince Nana O. Boateng
# 2016
from unittest import TestCase, main

# this implementation of a max binary heap uses a node of key value pairs.
# priority in queue is determined by the value of the key


class QNode:

    def __init__(self, key, value):
        self._key = key
        self._value = value

    def __repr__(self):
        return str((self._key, self._value))


class PriorityQueue:

    def __init__(self):
        self._heap = [None]
        self._size = 0

    def insert(self, key, val):
        self._heap.append(QNode(key, val))
        self._size += 1
        self._sift_up(self._size)

    def _sift_up(self, i):
        while i > 1:
            if self._heap[i]._key > self._heap[i // 2]._key:
                # swap positions
                temp = self._heap[i]
                self._heap[i] = self._heap[i // 2]
                self._heap[i // 2] = temp

            i = i // 2

    def get_max(self):
        return self._heap[1]._value

    def del_max(self):
        val = self.get_max()
        self._heap[1] = self._heap.pop()
        self._size -= 1
        self._sift_down(1)
        return val

    def _sift_down(self, i):
        k = self._size
        while i * 2 <= k:
            j = self._max_child(i)
            if self._heap[i]._key < self._heap[j]._key:
                # swap positions
                self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
            i = j

    def _max_child(self, index):
        if index * 2 + 1 > self._size:
            return index * 2
        else:
            if self._heap[index * 2]._key > self._heap[index * 2 + 1]._key:
                return index * 2
            return index * 2 + 1

    def remove(self, index):
        val = self._heap[index]
        self._heap[index] = self._heap.pop()
        self._size -= 1
        self._sift_down(index)
        return val

    def heapify(self, alist):
        for item in alist:
            self._heap.append(item)
        self._size = len(alist)
        i = self._size // 2
        while i > 0:
            self._sift_down(i)
            i -= 1

    def change_priority(self, index, newkey):
        old_key = self._heap[index]._key
        self._heap[index]._key = newkey
        if newkey > old_key:
            self._sift_up(index)
        else:
            self._sift_down(index)

    def size(self):
        return self._size

    def __len__(self):
        return self._size

    def __repr__(self):
        return self._heap[1:].__repr__()

    def __iter__(self):
        return self._heap[1:].__iter__()

    @staticmethod
    def heap_sort(alist):
        heap = PriorityQueue()
        heap.heapify(alist)
        while heap._size > 0:
            temp = heap._heap[1]
            heap._heap[1] = heap._heap[heap._size]
            heap._heap[heap._size] = temp
            heap._size -= 1
            heap._sift_down(1)
        alist = heap._heap[1:]
        return alist


class Test_Priority_Queue(TestCase):

    def setUp(self):
        self.heap = PriorityQueue()
        self.heap.insert(2, 'x')
        self.heap.insert(3, 'y')
        self.heap.insert(5, 'z')
        self.heap.insert(6, 'a')
        self.heap.insert(4, 'd')
        self.heap.insert(12, 'Sheneice')

    def test_insert(self):
        self.assertEqual(6, len(self.heap))

    def test_del_max(self):
        val = self.heap.del_max()
        self.assertEqual('Sheneice', val)
        self.assertEqual('a', self.heap.del_max())

    def test_get_max(self):
        val = self.heap.get_max()
        self.assertEqual('Sheneice', val)

    def test_higher_priority(self):
        self.heap.change_priority(4, 15)
        self.assertEqual('x', self.heap.get_max())

    def test_heapify(self):
        alist = [QNode(34, 'Frank'), QNode(12, 'G'), QNode(9, 'm')]
        heap = PriorityQueue()
        heap.heapify(alist)
        self.assertEqual('Frank', heap.del_max())

    def test_heap_sort(self):
        alist = [QNode(34, 'Frank'), QNode(12, 'G'), QNode(9, 'm')]
        res = self.heap.heap_sort(alist)
        self.assertEqual(res[0]._value, alist[2]._value)
        self.assertEqual(res[1]._value, alist[1]._value)
        self.assertEqual(res[2]._value, alist[0]._value)


if __name__ == '__main__':
    main()
