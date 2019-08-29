
def removeDuplicates(nums):
    i = 0
    for n in nums:
        if i < 2 or n > nums[i-2]:
            nums[i] = n
            i += 1
    return i

def removeDuplicates2(nums):
    if len(nums) < 3:
        return len(nums)
    i = 2
    for j in range(2, len(nums)):
        if nums[i - 2] != nums[j]:
            nums[i] = nums[j]
            i += 1
    return i

def removeDuplicatesK(nums, K):
    i = 0
    for n in nums:
        if i < K or n > nums[i-K]:
            nums[i] = n
            i += 1
    return i