'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's 
(representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. 
(If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

Given the above grid, return 6. Note the answer is not 11, because the island 
must be connected 4-directionally.

Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0. 
'''

def maxAreaOfIsland(grid):
    '''
    Approach #1: Depth-First Search (Recursive) [Accepted]

Intuition and Algorithm

We want to know the area of each connected shape in the grid, then take the maximum 
of these.
If we are on a land square and explore every square connected to it 4-directionally 
(and recursively squares connected to those squares, and so on), then the total 
number of squares explored will be the area of that connected shape.

To ensure we don't count squares in a shape more than once, let's use seen to keep 
track of squares we haven't visited before. It will also prevent us from counting 
the same shape more than once.
Time: O(R*C)
Space: O(R*C)
    '''
    seen = set()
    def area(r, c):
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in seen and grid[r][c]):
            return 0
        seen.add((r, c))
        return (1 + area(r+1, c) + area(r-1, c) + area(r, c-1) + area(r, c+1))

    return max(area(r, c) for r in range(len(grid)) for c in range(len(grid[0])))