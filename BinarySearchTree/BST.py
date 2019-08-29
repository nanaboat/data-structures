from collections import deque
from Node import Node
import sys

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
        if new_node < current_node:
            if current_node._left:
                self._put(new_node, current_node._left)
            else:
                current_node._left = new_node
                new_node._parent = current_node
        elif new_node > current_node:
            if current_node._right:
                self._put(new_node, current_node._right)
            else:
                current_node._right = new_node
                new_node._parent = current_node
        else:
            return

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

    @staticmethod
    def _find(val, start_node):
        if not start_node:
            return None
        elif start_node._data > val:
            return BST._find(val, start_node._left)
        elif start_node._data < val:
            return BST._find(val, start_node._right)
        else:
            return start_node

    def is_empty(self):
        if self._root:
            return False
        return True

    def get_min(self):
        if not self.is_empty():
            current = self._root
            while current._left:
                current = current._left
            return current
        return None

    def _find_min(self, start_node):
        while start_node._left:
            start_node = start_node._left
        return start_node

    def get_max(self):
        if not self.is_empty():
            current = self._root
            while current._right:
                current = current._right
            return current
        return None

    def _find_max(self, start_node):
        while start_node._right:
            start_node = start_node._right
        return start_node

    @staticmethod
    def inorder(start_node):
        if start_node:
            BST.inorder(start_node._left)
            print(start_node, end=" ")
            BST.inorder(start_node._right)

    @staticmethod
    def preorder(start_node):
        if start_node:
            print(start_node, end=" ")
            BST.preorder(start_node._left)
            BST.preorder(start_node._right)

    @staticmethod
    def postorder(start_node):
        if start_node:
            BST.postorder(start_node._left)
            BST.postorder(start_node._right)
            print(start_node, end=" ")
    
    @staticmethod
    def bfs(start_node):
        '''Breadth-first traversal.'''
        if start_node:
            d = deque()
            d.append(start_node)
            while len(d) != 0:
                node = d.popleft()
                print(node, end=' ')
                if node.has_left():
                    d.append(node._left)
                if node.has_right():
                    d.append(node._right)

    @staticmethod  #change this
    def is_BST(node):
        max_node = BST()._find_max(node._left)
        min_node = BST()._find_min(node._right)
        return max_node <= node and node >= min_node

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
            successor = self._get_inorder_successor(node)
            node._data = successor._data
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

    def _get_inorder_successor(self, node):
        if node is None:
            return None
        # case 1: node has right sub-tree
        elif node.has_right():
            successor = self._find_min(node._right)
        # case 2: node has no right sub-tree
        else:
            successor = None
            ancestor = self._root
            while ancestor != node:
                if node < ancestor:
                    successor = ancestor
                    ancestor = ancestor._left
                else:
                    ancestor = ancestor._right
        return successor

    def __iter__(self):
        return self._root.__iter__()

    def print_values(self, node):
        return self.inorder(node)

if __name__ == "__main__":
    alist = [15,10,20,8,12,17,25,6,11,16,27,10]
    n = BST()
    for i in alist:
        n.insert(i)
    BST.bfs(n._root)
    print()
    n.inorder(n._root)