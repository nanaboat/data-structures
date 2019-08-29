'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

def spiral_matrix(matrix):
    m = len(matrix)   # rows
    result = []
    if m < 1:
        return result
    n = len(matrix[0])  # columns
    a, b = 0, 0  # row_start and col_start
    size = m * n
    while len(result) != size:
        # move right from (a,b) ----> (a,n)
        for j in range(b, n):
            result.append(matrix[a][j])
        a += 1

        # move down from (a,n) -----> (m,n)
        for j in range(a, m):
            result.append(matrix[j][n - 1])
        n -= 1

        # move left from (m,n) -----> (m,b)
        if a < m:
            for j in range(n-1, b-1, -1):
                result.append(matrix[m - 1][j])
            m -= 1
            
        # move up from (m,b) ----> (a,b)
        if b < n:
            for j in range(m-1, a-1, -1):
                result.append(matrix[j][b])
            b += 1
        
    return result


if __name__ == "__main__":
    arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9,10,11,12]]
    print(spiral_matrix(arr))
    print()
    arr1 = [[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]]
    print(spiral_matrix(arr1))