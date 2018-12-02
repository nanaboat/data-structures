from Hashtable import HashTable
from unittest import TestCase, main


class TestHashTable(TestCase):
    def setUp(self):
        self.test_table = HashTable()
        self.test_table.add(5, 'Hello')
        self.test_table.add('Hello', 5)

    def test_add(self):
        test_table = HashTable()
        test_table.add(5, 'Hello')
        test_table.add('Hello', 5)
        self.assertEqual(2, len(test_table))

    def test_exist(self):
        self.assertEqual(True, self.test_table.exists(5))
        self.assertEqual(False, self.test_table.exists(7))

    def test_get(self):
        self.assertEqual('Hello', self.test_table.get(5))

    def test_remove(self):
        size = len(self.test_table)
        self.test_table.remove('Hello')
        new_size = len(self.test_table)
        self.assertEqual(2, size)
        self.assertEqual(1, new_size)
        self.assertNotEqual(size, new_size)

    def add_random_items(self):
        items = [('Here', 45), (34, 32), (23, 12), (123, 129), ('Jam', 45),
                 ('Beer', 45.0), ('Tues', 2), ('12', 12), ('33', 'Her'),
                 ('Happy', 'Man'), (12, ['k', 'g'])]
        for k, v in items:
            self.test_table[k] = v

    def test_add_to_resize(self):
        self.add_random_items()
        self.assertEqual(13, len(self.test_table))

    def test_remove_to_resize(self):
        self.add_random_items()
        self.test_table.remove('Here')
        self.test_table.remove('12')
        self.test_table.remove(12)
        self.test_table.remove('33')
        self.test_table.remove('Happy')
        self.test_table.remove('Tues')
        self.test_table.remove(23)
        self.assertEqual(6, len(self.test_table))


if __name__ == '__main__':
    main()
