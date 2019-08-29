def findUniqueNums(arr):
    res = []
    get_count(arr, 0, len(arr) - 1, res)
    return len(res)

def get_count(arr, start, end, res):
    if end < start:
        return None
    if arr[start] == arr[end]:
        res.append(arr[start])
        while end + 1 < len(arr) and arr[end + 1] == arr[start]:
            end += 1
        return end
    else:
        mid = (start + end) // 2
        left = get_count(arr, start, mid - 1, res)
        right = get_count(arr, left + 1, end, res)
        return right


def findrepeatingNum(arr):
    pass



if __name__ == "__main__":
    arr = [1,1,1,5,5,5,9,10,10]
    print(findUniqueNums(arr))