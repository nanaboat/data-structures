from collections import deque

'''
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.

Construct the maximum tree by the given array and output the root node of this tree.

Example 1:

Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1

Note:

    The size of the given array will be in the range [1,1000].
https://leetcode.com/problems/maximum-binary-tree/
'''

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    '''
    This is a brute force solution with an O(n^2) time complexity.
    for every node in the array we call the max function ( max function takes O(n) time complexity)
    this gives an overall O(n^2) time complexity for both solutions in this class.
    '''
    def constructMaximumBinaryTree(self, nums):
        start = 0
        end = len(nums)
        def buildTree(arr, start, end):
            if start < end:
                max_num = max(arr[start:end])
                idx = arr.index(max_num)
                node = TreeNode(max_num)
                node.left = buildTree(arr, start, idx)
                node.right = buildTree(arr, idx+1, end)
                return node
        return buildTree(nums, start, end)
    
    def buildMaximumBinaryTree(self, arr):
        start = 0
        end = len(arr)
        if start == end:
            return None
        max_num = max(arr[start:end])
        idx = arr.index(max_num)
        node = TreeNode(max_num)
        if idx == start:
            node.right = self.buildMaximumBinaryTree(arr[idx+1:])
        elif idx == (end - 1):
            node.left = self.buildMaximumBinaryTree(arr[start:idx])
        else:
            node.left = self.buildMaximumBinaryTree(arr[start:idx])
            node.right = self.buildMaximumBinaryTree(arr[idx+1:])
        return node

class Solution2:
    '''
    This is a much optimized solution of the same problem. We use a stack-based algorithm.
    The array/list passed to the fuction builds a cartesian tree. https://en.wikipedia.org/wiki/Cartesian_tree#Efficient_construction
    The link provide more info about cartesian trees.
    '''
    def buildTree(self, nums):
        stack = deque()
        for num in nums:
            cur = TreeNode(num)
            while stack and stack[-1].val < cur.val:
                cur.left = stack.pop()
            if stack:
                stack[-1].right = cur 
            stack.append(cur)
        return stack[0]


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"

if __name__ == '__main__':
    ans1 = Solution().buildMaximumBinaryTree([3,2,1,6,0,5])
    ans2 = Solution2().buildTree([3,2,1,6,0,5])
    print(treeNodeToString(ans1))
    print(treeNodeToString(ans2))