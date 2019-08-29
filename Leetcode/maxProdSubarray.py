'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

'''

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxprod = nums[0]
        curr_min = nums[0]
        curr_max = nums[0]
        for n in range(1, len(nums)):
            p_max = max(curr_max * nums[n], curr_min * nums[n],  nums[n])
            p_min = min(curr_min * nums[n], curr_max* nums[n], nums[n])
            maxprod = max(maxprod, p_max)
            curr_max = p_max
            curr_min = p_min
        
        return maxprod