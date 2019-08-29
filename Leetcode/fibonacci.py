def fib(num):
    '''
    bottom -up approach using memoization
    '''
    if num == 0:
        return 0
    cache = [0] * (num + 1)
    cache[1] = 1
    for i in range(2, num + 1):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[num]


if __name__ == '__main__':
    print(fib(6))