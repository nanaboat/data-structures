# Q10.3 in CTCI

class SearchRotatedArray:
    ''' Searching in a rotated array.'''
    def search(self, arr, num):
        return self.searchUtil(arr, 0, len(arr) - 1, num)
    
    def searchUtil(self, arr, start, end, num):
        if end > start:
            return -1
        mid = (start + end) // 2
        if arr[mid] == num:
            return mid
        if start < arr[mid]:
            # ordered on the left side
            if arr[start] < num and num < arr[end]:
                # search the left side
                return self.searchUtil(arr, start, mid - 1, num)
            # search the right side
            self.searchUtil(arr, mid + 1, end, num)

        elif arr[mid] < end:
            # ordered on the right side 
            if arr[mid] < num and num < arr[end]:
                # search the right side
                return self.searchUtil(arr, mid + 1, end, num)
            # search the left side
            return self.searchUtil(arr, start, mid - 1, num)
        
        else:
            index = -1
            if start == arr[mid]:
                # search right side
                index = self.searchUtil(arr, mid + 1, end, num)
            if index == -1 and end == arr[mid]:
                # search left side
                index = self.searchUtil(arr, start, mid - 1, num)
            
            return  index
    
    def search_iterative(self, nums, target):
        if not nums or len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            
            # case 1
            if nums[mid] == target:
                return mid
            
            # case 2
            elif nums[start] <= nums[mid]:
                if nums[start] <= target and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            
            # case 3
            else:
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
    
    def search_2(self, nums, target):
        if not nums or len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if (target >= nums[0]) == (nums[mid] >= nums[0]):
                c = nums[mid]
            else:
                if target < nums[0]:
                    c = - 2**32
                else:
                    c = 2 ** 32
            
            if target == c:
                return mid
            elif target > c:
                start = mid + 1
            else:
                end = mid - 1
        
        return -1
    
    def search_with_dupes(self, nums, target):
        if not nums:
            return False
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] > nums[r]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                r -= 1
        return nums[l] == target


# Q10.4 in CTCI

class Listy:
    def __init__(self):
        self.arr = []
    
    def elementAt(self, i):
        val = -1
        try:
           val = self.arr[i]
        except IndexError:
            pass
        return val

class sortedSearch:
    ''' Search in a sorted array with positive integers with unknown size.'''
    def search(self, alist, val):
        idx = 1
        while alist[idx] != -1 and alist[idx] < val:
            idx = 2 ** idx
        return self.binSearch(alist, idx // 2, idx, val)
    
    def binSearch(self, alist, low, high, val):
        while low <= high:
            mid = low + high
            if alist[mid] > val | alist[mid] == -1:
                high = mid - 1
            elif alist[mid] < val:
                low = mid + 1
            else:
                return mid
        return -1