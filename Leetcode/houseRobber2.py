'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.

Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Hint:
Since House[1] and House[n] are adjacent, they cannot be robbed together.
Therefore, the problem becomes to rob either House[1]-House[n-1] or House[2]-House[n],
depending on which choice offers more money. Now the problem has degenerated to
the House Robber, which is already been solved.

'''

class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)
        
        max_val1 = self.robUtil(nums[:-1])
        max_val2 = self.robUtil(nums[1:])
        return max(max_val1, max_val2)
    
    def robUtil(self, nums):
        import pdb; pdb.set_trace()
        n = len(nums)
        cache = [-1] * (n + 1)
        cache[0] = 0
        cache[1] = nums[0]
        for i in range(1, n):
            cache[i + 1] = max(nums[i] + cache[i - 1], cache[i])
        print(cache)
        return cache[-1]

if __name__ == "__main__":
    print(Solution().rob([1,2,3,1]))