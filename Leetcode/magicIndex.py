'''
CTCI Q8.3: Finding the magic index in a sorted array
'''

def magicIndex(arr):
    '''
    Arr has no dupes. Time: O(n)
    '''
    return getIndex(arr, 0, len(arr) - 1)

def getIndex(arr, start, end):
    if end < start:
        return -1
    mid = (start + end) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return getIndex(arr, start, mid - 1)
    else:
        return getIndex(arr, mid + 1, end)


def magic_index(arr):
    '''
    arr has dupes
    '''
    return get_index(arr, 0, len(arr) - 1)

def get_index(arr, start, end):
    if end < start:
        return -1
    
    mid = (start + end) // 2
    if arr[mid] == mid:
        return mid
    
    left_index = min(mid - 1, arr[mid])
    left = get_index(arr, start, left_index)
    if left >= 0:
        return left
    
    right_index = max(mid + 1, arr[mid])
    return get_index(arr, right_index, end)

if __name__ == "__main__":
    print(magicIndex([-40,-20,-1,1,2,3,5,7,9,12,13]))
    print(magic_index([-10,-5,2,2,2,3,4,5,9,12,13]))