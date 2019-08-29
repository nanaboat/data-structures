'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Return:

[
   [5,4,11,2],
   [5,8,4,5]
]


'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        def check(node, rem):
            if node is None:
                return False
            if  node.left is None and node.right is None:
                if rem == node.val:
                    return True
                else:
                    return False

            
            if check(node.left, rem - node.val) or check(node.right, rem - node.val):
                return True
            
            return False
        
        return check(root, sum)
    
    def hasPathSum1(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        return self.dfs(root, sum) or False
    
    def dfs(self, node, rem):
        if not node:
            return False
        if rem == node.val and not node.left and not node.right:
            return True
        if node.left or node.right:
            return self.dfs(node.left, rem - node.val) or self.dfs(node.right, rem - node.val)
        
        return False
    
    def pathSum2(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []
        self.findpath(root, sum, [], res)
        return res
    
    def findpath(self, node, total, path, result):
        if total == node.val and not node.left and not node.right:
            result.append(path + [node.val])
        
        if node.left:
            self.findpath(node.left, total - node.val, path + [node.val], result)
        
        if node.right:
            self.findpath(node.right, total - node.val, path + [node.val], result)