def reverseString(aString):
    if len(aString) == 1:
        return [aString]
    else:
        return [aString[-1]] + reverseString(aString[:-1])

def f(n):
    if n <=0:
        return 0
    return n + f(int(n/2))


if __name__ == "__main__":
    print(reverseString('abd'))
    print(f(4))