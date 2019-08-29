'''
 Given n nodes labeled from 0 to n - 1 and a list of undirected edges 
 (each edge is a pair of nodes), write a function to find the number of 
 connected components in an undirected graph.

Example 1:

     0          3
     |          |
     1 --- 2    4

Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:

     0           4
     |           |
     1 --- 2 --- 3

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0, 1] is the same as [1, 0] and
thus will not appear together in edges. 
'''

class Solution:
    def countComponents(self, n, edges):
        graph = {}
        for edge in edges:
            start, end = edge
            graph.setdefault(start, []).append(end)
            graph.setdefault(end, []).append(start)
        
        count = 0
        visited = set()

        for i in range(n):
            if i not in visited:
                count += 1
                self.dfs_visit(graph, i, visited)
        return count
    
    def dfs_visit(self, graph, node, visited_nodes):
        stack = []
        stack.append(node)

        while stack:
            n = stack.pop()
            for nei in graph[n]:
                if nei not in visited_nodes:
                    stack.append(nei)
            visited_nodes.add(n)
    
    def numIslands(self, grid):
        '''
        Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

        Example 1:
        Input:
        11110
        11010
        11000
        00000

       Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 

          3

        '''
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j)
        return count
    
    def dfs(self, grid, x, y):
        # check if we are in bounds
        if y < 0 or y >= len(grid[0]) or x < 0 or x >= len(grid) or grid[x][y] != '1':
            return
        # mark as visited
        grid[x][y] = '*'
        self.dfs(grid, x + 1, y)
        self.dfs(grid, x - 1, y)
        self.dfs(grid, x, y + 1)
        self.dfs(grid, x, y - 1)

if __name__ == "__main__":
    print(Solution().countComponents(5, [[0, 1], [1, 2], [3, 4]]))
