# nums = [5,7,7,8,8,10]

def searchRange(nums, target):
    i = 0
    j = len(nums) - 1
    #import pdb; pdb.set_trace()
    # find leftmost index
    while i < j:
        mid = (i + j) // 2 # mid is skewed to the left
        if nums[mid] < target:
            i = mid + 1
        else:
            j = mid
    if nums[i] != target:
        return  [-1, -1]
    result = [i]
    j = len(nums) - 1
    # find the rightmost index
    while i < j:
        mid = ((i + j) // 2) + 1 # mid is skewed to the right 
        if nums[mid] > target:
            j = mid - 1
        else:
            i = mid
        print (i, nums[mid], mid, j)
    result.append(j)
    return result


def searchRange1(nums, target):
    if len(nums) == 0:
        return [-1, -1]
    start = 0
    end = len(nums) - 1
        
    found = False
    while start <= end and not found:
        mid = (start + end) // 2
        if nums[mid] == target:
            found = True
        else:
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
    if found:
        sidx = mid
        jidx = mid
            #if nums[mid - 1] == target:
        while (sidx - 1) >= 0 and nums[sidx - 1] == target:
            sidx -= 1
            #if nums[mid + 1] == target:
        while (jidx + 1) < len(nums) and nums[jidx + 1] == target:
            jidx += 1
            #print(mid, sidx, jidx)
        if sidx < mid and jidx > mid:
            return [sidx, jidx]
        elif mid == sidx and mid == jidx:
            return [mid, mid]
        elif sidx < mid:
            return [sidx, mid]
        elif jidx > mid:
            return [mid, jidx]
    return [-1, -1]

if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    n = [1,1,1,1,1,5,5,7,8,8]
    print(searchRange(nums, 5))
    print(searchRange(n, 1))
