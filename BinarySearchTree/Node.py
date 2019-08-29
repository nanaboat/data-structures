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
    
    def __eq__(self, other_node):
        return self._data == other_node._data
    
    def __gt__(self, other_node):
        return self._data > other_node._data
    
    def __lt__(self, other_node):
        return self._data < other_node._data
    
    def __ne__(self, other_node):
        return self._data != other_node._data