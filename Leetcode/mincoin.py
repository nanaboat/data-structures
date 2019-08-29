# Find minimum number of coins that make a given value


import sys

def minCoins(coins, m, sumVal):
    '''
    bottom down approach
    '''
    table = [0]
    #import pdb; pdb.set_trace()
    for i in range(1, sumVal + 1):
        table.append(sys.maxsize)
    #print(table)
    for i in range(1, sumVal + 1):
        for j in range(m):
            if (i >= coins[j]):
                table[i] = min(table[i], table[i - coins[j]] + 1)
    print(table)
    return table[sumVal]

def minCoins_1(coins, m, change):
    '''
    top down approach
    '''
    cache = [0]
    cache += [-1] * change
    return makeChange(coins, change, cache)

def makeChange(coins, change, cache):
    if cache[change] >= 0:
        return cache[change]
    minCoin = sys.maxsize
    #import pdb; pdb.set_trace()
    for coin in coins:
        if change - coin >= 0:
            currCoin = makeChange(coins, change - coin, cache)
            minCoin = min(minCoin, currCoin)
    
    cache[change] = minCoin + 1
    return cache[change]


if __name__ == "__main__":
    #print(line, end="")
    val = 4
    coins = [1, 3, 5]
    length = len(coins)
    print(minCoins_1(coins, length, val))