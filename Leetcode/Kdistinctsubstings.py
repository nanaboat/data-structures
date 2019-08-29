'''
Find substrings of size K with K distinct characters
'''

def KdistinctSubStrings(astr, K):
    n = len(astr)
    res = set()
    for i in range(n):
        count = 0
        cache = [0] * 25
        word = []
        for j in range(i, n):
            # If this is a new character for this substring, increment count
            if cache[ord(astr[j]) - ord('a')] == 0:
                count += 1
                word.append(astr[j])
            
            cache[ord(astr[j]) - ord('a')] += 1

            if count == K:
                res.add(''.join(word))
    return res


def kDistinctSubStrings(astr, K):
    n = len(astr)
    res = set()
    for i in range(n):
        count = 0
        cache = [0] * 25
        word = []
        for j in range(i, n):
            # If this is a new character for this substring, increment count
            if cache[ord(astr[j]) - ord('a')] > 0:
                break
                
            
            cache[ord(astr[j]) - ord('a')] += 1
            count += 1
            word.append(astr[j])

            if count == K:
                res.add(''.join(word))
                break
    return res


if __name__ == "__main__":
    print(kDistinctSubStrings('awaglknagawunagwkwagl', 4))
    print(kDistinctSubStrings('abcd', 3))