'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
https://leetcode.com/problems/maximal-square/

'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        if row < 1:
            return 0
        col = len(matrix[0])
        if col < 1:
            return 0
        if row == 1 and col == 1:
            return int(matrix[0][0])
        cache = [[0] * col for i in range(row)]
 
        max_len = 0
        for i in range(row):
            for j in range(col):
                if i == 0 or j == 0:
                    cache[i][j] = matrix[i][j]
                elif matrix[i][j] == '1':
                    cache[i][j] = min(int(cache[i-1][j]), int(cache[i][j-1]), int(cache[i-1][j-1])) + 1
                #max_len = max(cache[i][j], max_len)
                
                if int(cache[i][j]) > int(max_len):
                    max_len = cache[i][j]
        #print(cache)
        return int(max_len) * int(max_len)