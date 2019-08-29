'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''

class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        if length < 1:
            return []
        ans = [0] * length
        ans[0] = 1
        for i in range(1, length):
            ans[i] = ans[i - 1] * nums[i - 1]
        
        R = 1
        for i in range(length - 1, -1, -1):
            ans[i] = ans[i] * R
            R *= nums[i]
        
        return ans
    
    def product(self, nums):
        '''
        where n can be negative and positive
        '''
        count = 0
        for i in nums:
            if i == 0:
                count += 1
        if count > 1:
            return [0] * len(nums)
        return self.productExceptSelf(nums)

if __name__ == "__main__":
    print(Solution().product([5,6,0]))
    print(Solution().product([5,6,0,0]))
    print(Solution().product([5,6,2,1 ]))
    print(Solution().product([5,6,2,0]))
    print(Solution().product([-1,-2,0,-5]))
