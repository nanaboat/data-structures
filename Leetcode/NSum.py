'''
The core is to implement a fast 2- pointer to solve 2Sum problem (base case)
Use recursion to reduce the N-sum to a 2Sum problem.
https://leetcode.com/problems/4sum/discuss/8545/Python-140ms-beats-100-and-works-for-N-sum-(Ngreater2)
'''

def twoSum(arr, target):
    
    if len(arr) < 2:
        return
    arr.sort()
    l, r = 0, len(arr) - 1
    res = []
    while l < r:
        x = arr[l] + arr[r]
        if x == target:
            res.append([arr[l], arr[r]])
        if x < target:
            c = l
            while l < r and arr[c] == arr[l]:
                l += 1
        else:
            c = r
            while l < r and arr[c] == arr[r]:
                r -= 1
    return res

def fourSum(arr, target):
    if len(arr) == 4:
        if sum(arr) == target:
            return [arr]
        return []
    arr.sort()
    result = []
    findNSum(arr, target, 4, [], result)
    return result

def findNSum(arr, target, N, res, results):
    #import pdb; pdb.set_trace()
    if len(arr) < N or N < 2 or target < arr[0] * N or target > arr[-1] * N:
        return
    #if len(arr) == N and sum(arr) == target:
    #    results.append(arr)
    if N == 2:
        l, r = 0, len(arr) - 1
        while l < r:
            x = arr[l] + arr[r]
            if x == target:
                import pdb; pdb.set_trace()
                results.append(res + [arr[l], arr[r]])
            if x < target:
                c = l
                while l < r and arr[c] == arr[l]:
                    l += 1
            else:
                c = r
                while l < r and arr[c] == arr[r]:
                    r -= 1
    else:
        for i in range(len(arr) - N + 1):
            if i == 0 or arr[i] != arr[i - 1]:
                findNSum(arr[i+1:], target - arr[i], N-1, res + [arr[i]], results)

if __name__ == "__main__":
    #print(twoSum([2,7,11,15,-2], 9))
    print(fourSum([-1,0,1,2,-1,-4], -1))