'''
Implements Morris inorder and preorder traversal.
This is a binary tree traversal with O(1) space
https://www.youtube.com/watch?v=wGXB9OWhPTg
https://github.com/mission-peace/interview/blob/master/src/com/interview/tree/MorrisTraversal.java
'''

def inorder(node):
    '''
    iterative approach using constant space
    '''
    current = node
    while current is not None:
        if current.left is None:
            print(current.val)
            current = current.right
        else:
            pred = current.left
            while pred.right != current and pred.right is not None:
                pred = pred.right
            
            if pred.right is None:
                pred.right = current
                current = current.left
            else:
                pred.right = None
                print(current.val)
                current = current.right

def preorder(node):
    '''
    iterative approach using constant space
    '''
    current = node
    while current is not None:
        if current.left is None:
            print(current.val)
            current = current.right
        else:
            pred = current.left
            while pred.right != current and pred.right is not None:
                pred = pred.right
            
            if pred.right is None:
                pred.right = current
                print(current.val)
                current = current.left
            else:
                pred.right = None
                current = current.right

def preorderTraversal(root):
    '''
    iterative approach using a stack
    '''
    if root is None or root.val is None:
        return []
    stack = []
    res = []
    while root is not None or len(stack) > 0:
        if root is not None:
            res.append(root.val)
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            root = node.right
    return res

def postorderTraversal(root):
    '''
    Iterative approach using a stack
    '''
    if root is None or root.val is None:
        return []
    stack = []
    res = []
    while root is not None or len(stack) > 0:
        if root is not None:
            stack.append(root)
            root = root.left
        else:
            node = stack[-1]
            if node.right:
                root = node.right
            else:
                res.append(stack.pop())
                if stack:
                    root = stack[-1].right


'''
114. Flatten Binary Tree to Linked List
Medium

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6

The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
'''

class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        current = root
        while current is not None:
            if current.left is None:
                current = current.right
            else:
                pred = current.left
                while pred.right != current and pred.right is not None:
                    pred = pred.right
                
                pred.right = current.right
                current.right = current.left
                current.left = None
                current = current.right
