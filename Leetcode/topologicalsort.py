# Course Schedule

# A collection of courses at a University has prerequisite courses that must be taken first. Given an
# array of course pairs [a, B] where A is the prerequisite of B, determine a valid sequence of courses
# a student can take to complete all the courses

# Parameters
# Input: courses [[String]]
# Output: [String]

# Examples
# [[a, b], [a, c], [b, d], [c, d]] --> [a, b, c, d] || [a, c, b, d]
#
#  Example:
#
#  Input: [["a","b"],["a","c"],["b","d"],["c","d"]]
#  Output: ["a","b","c","d"] or ["a","c","b","d"]
#
#  Input: [["a","b"],["b","c"],["c","d"]]
#  Output: ["a","b","c","d"]

"""
  - B - D
a     /
  - C
  
Take a before B
Take C take a first
Take course D, take either B or C 

A: B or C


- use my input to build a graph using adjacent list

vertex: all the courses

{a:[b, c], b:[d], c:[d], d:[]}
-------------------------------------
wrapper(input)
  helper(dfs)

  callhelper(startvertex)


results = []
visited = set()

start vertex(a)
call dfs(a)


resutls = [d, c, b, a] (reverse)
"""
def dfs(vertex, graph, visited, results):
    if vertex in visited:
        return

    visited.add(vertex)
    for child in graph[vertex]:
        dfs(child, graph, visited, results)

    results.append(vertex)
    
    
 # [[a, b], [a, c], [b, d], [c, d]]
def convertgraph(lists_courses):
    graph = {} 
    for courses in lists_courses:
        vertex = courses[0]
        nei = courses[1]

        if vertex not in graph:
            graph[vertex] = []
      
        if nei not in graph:
            graph[nei] = []

        graph[vertex].append(nei)
        # graph ={'a':[b], 'b' = []}
    return graph 


def topologicalsort(graph):
    visited = set()
    results = []
    for vertex in graph:
        dfs(vertex, graph, visited, results)

    # reverse the order of the sort
    seq = []
    while len(results) > 0:    
        seq.append(results.pop())
    return seq


if __name__ == "__main__":
    L = [['a', 'b'], ['a', 'c'], ['b', 'd'], ['c', 'd']]
    g = convertgraph(L)
    r = topologicalsort(g)
    print(r)
    G = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
    graph = topologicalsort(convertgraph(G))
    print(graph)

