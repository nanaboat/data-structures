# From Cracking the coding interview Q4.7
# Input: 
#      projects: a, b, c, d, e, f
#      dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c


class GraphNode:
    def __init__(self, name):
        self.name = name
        self.children = set()
        self.state = 0       # 0 --> not visited  1 --> visiting   2 --> visited
    
    def addNeighbor(self, node):
        self.children.add(node)

    def getChildren(self):
        return self.children

    def setState(self, new_state):
        self.state = new_state 
    

class Graph:
    def __init__(self):
        self.nodes = {}
    
    def addEdge(self, start, end):
        if start not in self.nodes:
            self.addNode(start)
        if end not in self.nodes:
            self.addNode(end)
        self.nodes[start].addNeighbor(self.nodes[end])
    
    def addNode(self, node):
        self.nodes[node] = GraphNode(node)


class BuildOrder:
    def buildGraph(self, projects, dependencies):
        graph = Graph()
        for d in dependencies:
            start, end = d
            graph.addEdge(start, end)
        
        for p in projects:
            if p not in graph.nodes:
                graph.addNode(p)
        
        return graph
    
    def dfs(self, node, results):
        if node.state == 1:
            return False  # We have a cycle
        if node.state == 0:
            node.state = 1
            for child in node.getChildren():
                if not self.dfs(child, results):
                    return False
            node.state = 2
            results.append(node.name)
        return True
    
    def buildOrder(self, projects, graph):
        results = []
        for project in projects:
            node = graph.nodes[project]
            if node.state == 0:
                if not self.dfs(node, results):
                    return self.error()
        
        stack = []
        while len(results) > 0:
            stack.append(results.pop())
        return stack

    def error(self):
        return "Error: No build"
    
    def main(self):
        projects = ['a', 'b', 'c', 'd', 'e', 'f']
        dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
        g = self.buildGraph(projects, dependencies)
        print(self.buildOrder(projects, g))


if __name__ == "__main__":
    BuildOrder().main()