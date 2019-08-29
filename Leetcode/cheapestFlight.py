import collections
import heapq

def findCheapestPrice(n, flights, src, dst, k):
    import pdb; pdb.set_trace()
    f = collections.defaultdict(dict)
    for a, b, p in flights:
        f[a][b] = p
    heap = [(0, src, k + 1)]
    while heap:
        p, i, k = heapq.heappop(heap)
        if i == dst:
            return p
        if k > 0:
            for j in f[i]:
                heapq.heappush(heap, (p + f[i][j], j, k - 1))
    return -1

def calculate(self, s):
        num, stack, sign = 0, [], "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                num = 0
                sign = s[i]
        return sum(stack)

if __name__ == "__main__":
    n = 3
    edges = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 0
    print(findCheapestPrice(n, edges, src, dst, k))