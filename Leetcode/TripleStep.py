'''
Cracking the coding interview question 8.1
'''
def count(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        import pdb; pdb.set_trace()
        a = count(n-1) + count(n-2) + count(n-3)
        return a

def countWays(n):
    '''
    Top down approach using memoization
    '''
    cache = [-1] * (n + 1)
    cache[0] = 1
    return countUtil(n, cache)

def countUtil(n, cache):
    if n < 0:
        return 0
    elif cache[n] > -1:
        return cache[n]
    else:
        cache[n] = countUtil(n-1, cache) + countUtil(n-2, cache) + countUtil(n-3, cache)
        return cache[n]

def count_ways(n):
    if n < 0:
        return 0
    cache = [-1] * (n + 1)
    cache[0] = 1
    cache[1] = 1
    cache[2] = 2
    for i in range(3, len(cache)):
        cache[i] = cache[i - 1] + cache[i - 2] + cache[i - 3]
    return cache[n]

if __name__ == "__main__":
    print(count_ways(4))