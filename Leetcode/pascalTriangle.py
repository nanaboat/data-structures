
def generatePascalTriangle(numRows):
    if numRows == 0:
        return []
    S =[[1]]
    if numRows == 1:
        return S
    for i in range(1, numRows):
        temp = [1]
        for j in range(1, i):
            print(temp)
            val = S[i - 1][j - 1] + S[i - 1][j]
            temp.append(val)
        temp.append(1)
        S.append(temp)
        print(S)
    return S


if __name__ == "__main__":
    generatePascalTriangle(6)