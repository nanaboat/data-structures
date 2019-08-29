'''
Finding the longest common prefix
'''

def LCP(arr):
    if arr is None:
        return ""
    pre = arr[0]
    for i in range(1, len(arr)):
        while arr[i].find(pre) != 0:
            pre = pre[0: len(pre) - 1]
            if len(pre) == 0 :
                return ""
    return pre

def findDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 1
        high = len(nums)-1
    
        while low < high:
            mid = low+(high-low)//2
            count = 0
            for i in nums:
                if i <= mid:
                    count+=1
            if count <= mid:
                low = mid+1
            else:
                high = mid
        return low
    

if __name__ == "__main__":
    print(LCP(["flow", "Glower", "flight"]))
    print(findDuplicate([1,4,6,6,6,2,3]))