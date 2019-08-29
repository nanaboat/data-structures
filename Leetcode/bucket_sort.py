def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = i - 1

        while j >= 0 and val < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j + 1] = val
    return arr

def bucket_sort(nums):
    arr = []
    n = len(nums)
    for i in range(n):
        arr.append([])
    
    for j in nums:
        idx = int(n * j)
        arr[idx].append(j)
    
    # sort the individual buckets
    for i in range(n):
        arr[i] = insertion_sort(arr[i])
    
    # concaatenate the result
    k = 0
    for i in range(n):
        for j in range(len(arr[i])):
            nums[k] = arr[i][j]
            k += 1
    
    return nums

if __name__ == "__main__":
    x = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    print(bucket_sort(x))
