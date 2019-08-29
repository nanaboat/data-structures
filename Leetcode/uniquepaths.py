'''
CTCI Q8.2 similar to unique path problem on leetcode
'''

def findPath(grid):
    '''
    Start from finish and going to origin.
    '''
    if not grid or len(grid) == 0:
        return None
    path = []
    if getpath(grid, len(grid) - 1, len(grid[0]) - 1, path):
        return path
    return None

def getpath(grid, row, col, path):
    if col < 0 or row < 0 or not grid[row][col]:
        return False
    isAtOrigin = (row == 0) and (col == 0)

    if isAtOrigin or getpath(grid, row, col - 1, path) or getpath(grid, row - 1, col, path):
        path.append((row, col))
        return True
    
    return False

def findPath_DP(grid):
    if not grid or len(grid) == 0:
        return None
    path = []
    failed_points = set()
    if getpath_DP(grid, len(grid) - 1, len(grid[0]) - 1, path, failed_points):
        return path
    return None

def getpath_DP(grid, row, col, path, failed_points):
    if col < 0 or row < 0 or not grid[row][col]:
        return False
    p = (row, col)
    if p in failed_points:
        return False
    isAtOrigin = (row == 0) and (col == 0)

    if isAtOrigin or getpath_DP(grid, row, col - 1, path, failed_points) or getpath_DP(grid, row - 1, col, path, failed_points):
        path.append((row, col))
        return True
    failed_points.add(p)
    return False

def unique_paths(grid):
    '''
    start from origin to destination (m,n)
    '''
    if not grid or len(grid) == 0:
        return [], 0
    paths = []
    getpaths(grid, 0, 0, paths, [])
    return paths, len(paths)

def getpaths(grid, row, col, paths, path):
    if col > len(grid[0]) or row > len(grid):
        return
    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        paths.append(path + [(row, col)])
    getpaths(grid, row + 1, col, paths, path + [(row, col)])
    getpaths(grid, row, col + 1, paths, path + [(row, col)])

def unique_paths_DP(grid):
    if not grid or len(grid) == 0:
        return 0
    cache = [[-1] * len(grid[0]) for i in range(len(grid))]
    num_paths(grid, cache)
    #print(cache)
    return cache[-1][-1]

def num_paths(grid, cache):
    for i in range(len(cache)):
        for j in range(len(cache[0])):
            if i == 0 or j == 0:
                cache[i][j] = grid[i][j]
            else:
                cache[i][j] = cache[i][j - 1] + cache[i - 1][j]

def minPathSum(grid):
        if not grid or len(grid) == 0:
            return 0
        row = len(grid)
        col = len(grid[0])
        cache = [[-1] * col for i in range(row)]
        for i in range(row):
            for j in range(col):
                #import pdb; pdb.set_trace()
                if i == 0 and j == 0:
                    cache[i][j] = grid[i][j]
                elif i == 0:
                    cache[i][j] = cache[i][j - 1] + grid[i][j]
                elif j == 0:
                    cache[i][j] = cache[i - 1][j] + grid[i][j]
                else:
                    cache[i][j] = min(cache[i-1][j], cache[i][j-1]) + grid[i][j]
        print(cache)
        return cache[-1][-1]            

if __name__ == "__main__":
    maze = [[1] * 3 for i in range(3)]
    #print(maze)
    #maze[2][0] = 0
    #print(findPath(maze))
    #print(unique_paths_DP(maze))
    a = [[1,3,1],[1,5,1],[4,2,1]]
    print(minPathSum(a))