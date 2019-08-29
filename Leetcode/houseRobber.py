'''
There is some frustration when people publish their perfect fine-grained algorithms without sharing any information abut how they were derived. This is an attempt to change the situation. There is not much more explanation but it's rather an example of higher level improvements. Converting a solution to the next step shouldn't be as hard as attempting to come up with perfect algorithm at first attempt.

This particular problem and most of others can be approached using the following sequence:

    Find recursive relation
    Recursive (top-down)
    Recursive + memo (top-down)
    Iterative + memo (bottom-up)
    Iterative + N variables (bottom-up)

Step 1. Figure out recursive relation.
A robber has 2 options: a) rob current house i; b) don't rob current house.
If an option "a" is selected it means she can't rob previous i-1 house but can safely proceed to the one before previous i-2 and gets all cumulative loot that follows.
If an option "b" is selected the robber gets all the possible loot from robbery of i-1 and all the following buildings.
So it boils down to calculating what is more profitable:

    robbery of current house + loot from houses before the previous
    loot from the previous house robbery and any loot captured before that

rob(i) = Math.max( rob(i - 2) + currentHouseValue, rob(i - 1) )
'''
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        cache = [-1] * len(nums)
        return self.robutil(nums, len(nums)-1, cache)
    
    def robutil(self, nums, i, cache):
        if i < 0:
            return 0
        if cache[i] > -1:
            return cache[i]
        s = max(self.robutil(nums, i-2, cache) + nums[i], self.robutil(nums, i-1, cache))
        cache[i] = s
        return s
    
    def rob_1(self, nums):
        if not nums:
            return 0
        return self.robutil_1(nums, len(nums) - 1)
    
    def robutil_1(self, nums, i):
        if i < 0:
            return 0
        s = max(self.robutil_1(nums, i-2) + nums[i], self.robutil_1(nums, i-1))
        return s
    
    def rob3(self, nums):
        if not nums:
            return 0
        cache = [-1] * (len(nums) + 1)
        cache[0] = 0
        cache[1] = nums [0]
        for i in range(1, len(nums)):
            cache[i+1] = max(nums[i] + cache[i - 1], cache[i])
        return cache[-1]

    def rob2(self, nums):
        if not nums:
            return 0
        j = 0
        k = 0
        for i in nums:
            temp = k
            k = max(i + j, k)
            j = temp
        return k
