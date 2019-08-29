from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        Recursive solution
        """
        if not root:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root

    def invertTree1(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        q = deque([root])
        while len(q) > 0:
            node = q.popleft()
            temp = node.left
            node.left = node.right
            node.right = temp
            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)
        return root