# Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, 
# and return them in any order.

# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] 
# is a list of all nodes j for which the edge (i, j) exists.

# Example:
# Input: [[1,2], [3], [3], []] 
# Output: [[0,1,3],[0,2,3]] 
# Explanation: The graph looks like this:
# 0--->1
# |    |
# v    v
# 2--->3
# There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

# Note:

#     The number of nodes in the graph will be in the range [2, 15].
#     You can print different paths in any order, but you should keep the order of nodes inside one path.


def allPathsSourceTarget(graph):
    '''recursive solution.'''
    target = len(graph) - 1
    return dfs(0, target, graph)

def dfs(src, dest, graph):
    if src == dest:
        return [[src]]
    ans = []
    for nei in graph[src]:
        for path in dfs(nei, dest, graph):
            ans.append([src] + path)
    
    return ans

def allPaths(graph):
    '''Iterative solution.'''
    target = len(graph) - 1
    def dfs(start):
        stack = [(start, [])]
        path = []
        result = []
        while stack:
            # get current node and path to current node from stack
            node, path_to_node = stack.pop()
            j = len(graph[node])
            if j > 0:  # if node has neighbors
                for i in range(j -1, -1, -1):
                    nei = graph[node][i]
                    stack.append((nei, path_to_node + [node]))
                path.append(node)
            else:  # node has no neighbors
                if node == target:
                    path.append(node)
                    result.append(path)
                    if stack:
                        # get path to last node in the stack
                        path = stack[-1][1]
                    else:
                        path = []
        return result
    return dfs(0)


def dfs1(data, path, paths = []): 
    '''
    https://stackoverflow.com/questions/20262712/enumerating-all-paths-in-a-directed-acyclic-graph#20264123
    '''  
    datum = path[-1]              
    if datum in data:
        for val in data[datum]:
            new_path = path + [val]
            paths = dfs1(data, new_path, paths)
    else:
        paths += [path]
    return paths

if __name__ == '__main__':
    print(allPathsSourceTarget([[1],[]]))
    print(allPaths([[4,3,1],[3,2,4],[3],[4],[]] ))
    data = {1 : [2,3], 2 : [3], 3 : [4,5], 4 : [5]}  # Directed acyclic graph adjacency list
    print(dfs1(data, [1], []))

