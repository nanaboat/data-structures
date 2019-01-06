import sys


class Node:

    def __init__(self, data, left=None, right=None, parent=None):
        self._parent = parent
        self._data = data
        self._left = left
        self._right = right

    def is_leaf(self):
        return not (self._left or self._right)

    def is_root(self):
        if self._parent:
            return False
        return True

    def has_both_children(self):
        return self._left and self._right

    def is_left_child(self):
        return self._parent._left == self

    def is_right_child(self):
        return self._parent._right == self

    def has_left(self):
        if self._left:
            return True
        return False

    def has_right(self):
        if self._right:
            return True
        return False

    def __repr__(self):
        return str(self._data)

    def __iter__(self):
        ''' inorder iteration of elements in BST.'''
        if self:
            if self.has_left():
                for i in self._left:
                    yield i
            yield self._data
            if self.has_right():
                for i in self._right:
                    yield i


class BST:

    def __init__(self):
        self._root = None
        self._size = 0

    def insert(self, val):
        node = Node(val)
        if not self._root:  # empty BST
            self._root = node
        else:
            self._put(node, self._root)
        self._size += 1

    def _put(self, new_node, current_node):
        if new_node._data < current_node._data:
            if current_node._left:
                self._put(new_node, current_node._left)
            else:
                current_node._left = new_node
                new_node._parent = current_node
        else:
            if current_node._right:
                self._put(new_node, current_node._right)
            else:
                current_node._right = new_node
                new_node._parent = current_node

    def size(self):
        return self._size

    def __len__(self):
        return self._size

    def is_in_tree(self, val):
        found = self._find(val, self._root)
        if found:
            return True
        return False

    def __contains__(self, val):
        return self.is_in_tree(val)

    def _find(self, val, start_node):
        if not start_node:
            return None
        elif start_node._data > val:
            return self._find(val, start_node._left)
        elif start_node._data < val:
            return self._find(val, start_node._right)
        else:
            return start_node

    def is_empty(self):
        if self._root:
            return False
        return True

    def get_min(self):
        if not self.is_empty():
            min_node = self._find_min(self._root)
            if min_node:
                return min_node._data
        return None

    def _find_min(self, start_node):
        while start_node._left:
            start_node = start_node._left
        return start_node

    def get_max(self):
        if not self.is_empty():
            max_node = self._find_max(self._root)
            if max_node:
                return max_node._data
        return None

    def _find_max(self, start_node):
        while start_node._right:
            start_node = start_node._right
        return start_node

    def inorder(self, start_node):
        if start_node:
            self.inorder(start_node._left)
            print(start_node, end=" ")
            self.inorder(start_node._right)

    def preorder(self, start_node):
        if start_node:
            print(start_node, end=" ")
            self.preorder(start_node._left)
            self.preorder(start_node._right)

    def postorder(self, start_node):
        if start_node:
            self.postorder(start_node._left)
            self.postorder(start_node._right)
            print(start_node, end=" ")

    @staticmethod
    def is_BST(node):
        prev = - sys.maxsize - 1
        return BST.is_BST_Util(node, prev)

    @staticmethod
    def is_BST_Util(start_node, min_val):
        if not start_node:
            return True
        if BST.is_BST_Util(start_node._left, min_val) is not True:
            return False
        if start_node._data < min_val:
            return False
        prev = min_val
        return BST.is_BST_Util(start_node._right, prev)

    def delete(self, val):
        if self._size > 1:
            node_to_remove = self._find(val, self._root)
            if node_to_remove:
                self._remove(node_to_remove)
                self._size -= 1
            else:
                raise ValueError('value does not exist in tree')
        elif self._size == 1 and self._root._data == val:
            self._root = None
            self._size -= 1
        else:
            raise ValueError('Tree is empty')

    def _remove(self, node):
        # Case 1: removing the leaf node
        if node.is_leaf():
            if node.is_left_child():
                node._parent._left = None
            else:
                node._parent._right = None

        # Case 2 : node has both left and right children
        elif node.has_both_children():
            successor = self._get_successor(node)
            self._remove(successor)

        # Case 3: node has either left or right node
        else:
            if node.has_left():
                if node.is_left_child():
                    node._parent._left = node._left
                    node._left._parent = node._parent
                if node.is_right_child():
                    node._parent._right = node._left
                    node._left._parent = node._parent
                if node.is_root():
                    self._root = node._left
                    node._left._parent = None
                    node._left = None

            else:
                if node.is_left_child():
                    node._parent._left = node._right
                    node._right._parent = node._parent
                if node.is_right_child():
                    node._parent._right = node._right
                    node._right._parent = node._parent
                if node.is_root():
                    self._root = node._right
                    node._right._parent = None
                    node._right = None

    def __delitem__(self, val):
        self.delete(val)

    def _get_successor(self, node):
        if node.has_right():
            successor = self._find_min(node._right)
        else:
            successor = None
            ancestor = self._root
            while ancestor != node:
                if node._data < ancestor._data:
                    successor = ancestor
                    ancestor = ancestor._left
                else:
                    ancestor = ancestor._right
        return successor

    def get_inorder_successor(self, value):
        node = self._find(value, self._root)
        if node:
            successor = self._get_successor(node)
            if successor:
                return successor._data

        return None

    def __iter__(self):
        return self._root.__iter__()

    def print_values(self, node):
        return self.inorder(node)
