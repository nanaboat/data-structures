from collections import deque

def convertToBinary(num):
    res = deque()
    print(bin(num))
    #import pdb; pdb.set_trace()
    while num > 0:
        r = num % 2
        num //= 2
        res.appendleft(str(r))
    while len(res) < 8:
        res.appendleft('0')
    return "".join(res)

def convertIPAddress(ip):
    address = ip.split('.')
    if validIP(address):
        ans = []
        for x in address:
            ans.append(convertToBinary(int(x)))
    return ".".join(ans)

def validIP(address):
    if len(address) < 4:
        return False
    for x in address:
        if int(x) > 255 or int(x) < 0:
            return False
    return True

if __name__ == "__main__":
    print(convertToBinary(169))
    print(convertIPAddress('45.79.78.169'))