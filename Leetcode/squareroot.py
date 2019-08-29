'''
find the square root of a num without using the sq. root fxn
'''

def squareroot(num):
    if num == 0 or num == 1:
        return num
    
    start = 1
    end = num

    while start <= end:
        mid = (start + end) // 2

        if mid * mid == num:
            return mid
        
        if (mid * mid) < num:
            start = mid + 1
            res = mid
        else:
            end = mid - 1
    
    return res


if __name__ == "__main__":
    print(squareroot(16))