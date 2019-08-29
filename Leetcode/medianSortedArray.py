def findMedianSortedArrays1(nums1, nums2) :
    ''' This solution is O(m+n)'''
    def merge(num1, num2):
        sorted_nums = []
        m = len(num1)
        n = len(num2)
        i = 0
        j = 0
        while i < m and j < n:
            if num1[i] <= num2[j]:
                sorted_nums.append(num1[i])
                i += 1
            else:
                sorted_nums.append(num2[j])
                j += 1
        while i < m:
            sorted_nums.append(num1[i])
            i += 1
        while j < n:
            sorted_nums.append(num2[j])
            j += 1
        return sorted_nums
    arr = merge(nums1, nums2)
    print(arr)
    size = len(arr)
    if size % 2 == 0:
        idx = size // 2
        idx1 = idx - 1
        median = (arr[idx] + arr[idx1]) / 2
        return median
    return float(arr[size // 2])


def findMedianSortedArrays(nums1, nums2):
    '''This solution is O(log(min(m,n)))'''
    if len(nums1) > len(nums2):
        return findMedianSortedArrays(nums2, nums1)
    X = len(nums1)
    Y = len(nums2)
    start = 0
    end = X
    while start <= end:
        partitionX = (start + end) // 2
        partitionY = ((X + Y + 1) // 2) - partitionX
            
        if partitionX == 0:
            maxLeftX = float('-inf')
        else:
            maxLeftX = nums1[partitionX - 1]
            
        if partitionX == X:
            minRightX = float('inf')
        else:
            minRightX = nums1[partitionX]
            
        if partitionY == 0:
            maxLeftY = float('-inf')
        else:
            maxLeftY = nums2[partitionY - 1]
            
        if partitionY == Y:
            minRightY = float('inf')
        else:
            minRightY = nums2[partitionY]
            
        if maxLeftX > minRightY:
            # move towards left in X
            end = partitionX - 1
        elif maxLeftY > minRightX:
            # move towards right in X
            start = partitionX + 1
        else:
            #found the perfect position
            if (X + Y) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            return float(max(maxLeftX, maxLeftY))