from BinarySearchTree.BST import BST
from unittest import TestCase, main


class Test_BST(TestCase):
    def setUp(self):
        self.tree = BST()
        self.tree.insert(15)
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(8)
        self.tree.insert(12)
        self.tree.insert(17)
        self.tree.insert(25)
        self.tree.insert(6)
        self.tree.insert(11)
        self.tree.insert(16)
        self.tree.insert(27)

    def test_insert(self):
        self.tree.insert(45)
        self.assertEqual(12, self.tree.size())

    def test_is_in_tree(self):
        self.assertFalse(self.tree.is_in_tree(3))
        self.assertTrue(self.tree.is_in_tree(16))

    def test_get_max(self):
        self.assertEqual(27, self.tree.get_max())

    def test_get_max_from_empty_tree(self):
        tree = BST()
        self.assertIsNone(tree.get_max())

    def test_get_min(self):
        self.assertEqual(6, self.tree.get_min())

    def test_get_min_from_empty_tree(self):
        tree = BST()
        self.assertIsNone(tree.get_min())

    def test_delete(self):
        self.tree.delete(11)
        self.assertEqual(10, len(self.tree))
        self.tree.delete(20)
        self.assertEqual(9, len(self.tree))

    def test_delete_val(self):
        self.assertRaises(ValueError, self.tree.delete, 45)

    def test_get_inorder_successor(self):
        succ = self.tree._get_inorder_successor(12)
        self.assertEqual(15, succ)


if __name__ == '__main__':
    main()
