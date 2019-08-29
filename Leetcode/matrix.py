'''
542. 01 Matrix
Medium

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]

 

Note:

    The number of elements of the given matrix will not exceed 10,000.
    There are at least one 0 in the given matrix.
    The cells are adjacent in only four directions: up, down, left and right.

Concluding thoughts on BFS :
    - Problems in which you have to find shortest path are most likely calling for a
      BFS.
    - For graphs having unit edge distances, shortest paths from any point is just a
      BFS starting at that point, no need for Dijkstra’s algorithm.
    - Maze solving problems are mostly shortest path problems and every maze is just
      a fancy graph so you get the flow.

Time complexity: O(row * col)
'''

from collections import deque
class Solution:
    def updateMatrix(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        q = deque()
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    q.append((i,j))
                else:
                    matrix[i][j] = 2 ** 32
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def validposition(i, j):
            if i < 0 or i >= n or j < 0 or j >=m:
                return False
            return True
        
        def isgreater(new_i, new_j, curr_i, curr_j):
            if matrix[new_i][new_j] > matrix[curr_i][curr_j] + 1:
                return True
            return False
        
        while len(q) > 0:
            curr = q.popleft()
            for d in directions:
                new_i = curr[0] + d[0]
                new_j = curr[1] + d[1]
                #check new_position is valid and new_dist is greater than curr_dist + 1
                if validposition(new_i, new_j):
                    if isgreater(new_i, new_j, curr[0], curr[1]):
                        matrix[new_i][new_j] = matrix[curr[0]][curr[1]] + 1
                        q.append((new_i, new_j))
        return matrix