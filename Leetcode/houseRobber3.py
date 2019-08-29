'''
https://leetcode.com/problems/house-robber-iii/discuss/79330/Step-by-step-tackling-of-the-problem
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        h_map = {}
        return self.rob_util(root, h_map)
        
        
    def rob_util(self, root, mapp):
        if not root:
            return 0
        if root in mapp:
            return mapp[root]
        val = 0
        if root.left:
            val += self.rob_util(root.left.left, mapp) + self.rob_util(root.left.right, mapp)
        if root.right:
            val += self.rob_util(root.right.left, mapp) + self.rob_util(root.right.right, mapp)
        
        val = max(val + root.val, self.rob_util(root.left, mapp) + self.rob_util(root.right, mapp))
        mapp[root] = val
        
        return val
    
    def rob1(self, root):
        res = self.robUtil(root)
        return max(res[0], res[1])
    
    def robUtil(self, root):
        if not root:
            return [0, 0]
        left = self.robUtil(root.left)
        right = self.robUtil(root.right)
        res = [0, 0]
        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = root.val + left[0] + right[0]
        return res