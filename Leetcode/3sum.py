def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Time: O(n^2) space: O(1)
        sort array first
        """
        result = []
        nums.sort()
        length = len(nums)
        for i in range(length - 2):
            if i == 0 or nums[i] > nums[i - 1]:
                start = i + 1
                end = length - 1
                while start < end:
                    res = nums[i] + nums[start] + nums[end]
                    if res == 0:
                        result.append([nums[i], nums[start], nums[end]])
                    if res < 0:
                        curr = start
                        while nums[curr] == nums[start] and start < end:
                            start += 1
                    else:
                        val = end
                        while nums[val] == nums[end] and start < end:
                            end -= 1
        return result


class Solution:
    def threeSum(self, nums):
        n = len(nums)
        result = []
        nums.sort()
        for i in range(n - 1):
            if i == 0 or nums[i] > nums[i - 1]:
                l = i + 1
                r = n - 1
                while l < r:
                    x = nums[i] + nums[l] + nums[r]
                    if x == 0:
                        result.append([nums[i], nums[l], nums[r]])
                    if x < 0:
                        curr = l
                        while nums[curr] == nums[l] and l < r:
                            l += 1
                    else:
                        curr = r
                        while nums[curr] == nums[r] and l < r:
                            r -= 1
        return result

if __name__ == '__main__':
    print(Solution().threeSum([-1,0,1,2,-1,-4]))