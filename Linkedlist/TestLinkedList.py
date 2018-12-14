from LinkedList import *
import unittest


class TestUnorderedList(unittest.TestCase):
    def setUp(self):
        self.collection = UnorderedList()

    def testIsEmpty(self):
        self.assertEqual(self.collection.isEmpty(), True)

    def _addItems(self):
        self.collection.add_front(5)
        self.collection.add_front(89)
        self.collection.add_front(6)

    def test_add(self):
        self._addItems()
        size = self.collection.size()
        self.assertEqual(3, size)

    def test_search(self):
        self._addItems()
        self.assertTrue(self.collection.search(5))
        self.assertTrue(self.collection.search(89))
        self.assertTrue(self.collection.search(6))

    def test_remove(self):
        self._addItems()
        self.collection.remove(5)
        size = len(self.collection)
        self.assertEqual(2, size)
        self.assertRaises(IndexError, self.collection.remove, 25)

    def test_append(self):
        self._addItems()
        self.collection.append(33)
        self.assertEqual(4, len(self.collection))

    def test_insert(self):
        self._addItems()
        self.assertRaises(IndexError, self.collection.insert, 5, 46)
        self.collection.insert(2, 46)
        index = self.collection.index(46)
        self.assertEqual(index, 2)
        value = self.collection[2]
        self.assertEqual(value, 46)

    def test_pop(self):
        self._addItems()
        self.collection.append(33)
        self.assertEqual(self.collection.pop(), 33)
        result = self.collection.pop(1)
        self.assertEqual(result, 89)

    def test_pop_front(self):
        self.assertRaises(IndexError, self.collection.pop_front)
        self._addItems()
        size = len(self.collection)
        self.assertEqual(6, self.collection.pop_front())
        self.assertNotEqual(size, len(self.collection))

    def test_value_at(self):
        self._addItems()
        self.assertEqual(self.collection.value_at(1), 89)
        self.assertRaises(IndexError, self.collection.value_at, 4)

    def test_front(self):
        self.assertRaises(IndexError, self.collection.front)
        self._addItems()
        size = len(self.collection)
        self.assertEqual(6, self.collection.front())
        self.assertEqual(size, len(self.collection))

    def test_back(self):
        self.assertRaises(IndexError, self.collection.back)
        self._addItems()
        size = len(self.collection)
        self.assertEqual(5, self.collection.back())
        self.assertEqual(size, len(self.collection))

    def test_reverse(self):
        self.assertRaises(IndexError, self.collection.reverse)
        self._addItems()
        head = self.collection.front()
        self.collection.reverse()
        new_head = self.collection.front()
        self.assertNotEqual(head, new_head)


class TestUnorderedListTail(TestUnorderedList):
    def setUp(self):
        self.collection = UnorderedListTail()

    def test_back(self):
        self.assertRaises(IndexError, self.collection.back)
        self._addItems()
        tail = self.collection.back()
        self.assertEqual(tail, 5)

    def test_pop(self):
        self._addItems()
        self.collection.append(33)
        self.assertEqual(self.collection.pop(), 33)
        result = self.collection.pop(1)
        self.assertEqual(result, 89)

    def test_reverse(self):
        self.assertRaises(IndexError, self.collection.reverse)
        self._addItems()
        head = self.collection.front()
        self.collection.reverse()
        new_head = self.collection.front()
        self.assertNotEqual(head, new_head)

    def test_append(self):
        self._addItems()
        self.collection.append(33)
        self.assertEqual(4, len(self.collection))

    def test_add_front(self):
        self._addItems()
        size = self.collection.size()
        self.assertEqual(3, size)


if __name__ == '__main__':
    unittest.main()
