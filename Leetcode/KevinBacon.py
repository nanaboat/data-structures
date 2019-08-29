'''
This is part two of the Breadth-First Search algorithm is and
implement it in Python. This implements "6 Degrees of Kevin Bacon" 
(finding the closest relationship between Kevin Bacon and another actor).
https://stackoverflow.com/questions/47586428/shortest-path-graph-traversal-for-kevin-bacon-game
'''
from collections import deque


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = set()
        self.parent = None


class SixDegrees:
    def buildGraph(self, data):
        G = {}
        for key, val in data.items():
            for v in val:
                if key not in G:
                    G[key] = Node(key)
                if v not in G:
                    G[v] = Node(v)
                G[key].neighbors.add(G[v])
                G[v].neighbors.add(G[key])
        return G
    
    def traverse(self, name, nodes, target="Kevin Bacon"):
        q = deque()
        v = set()
        q.append(nodes.get(name))
        v.add(nodes.get(name))
        while len(q) > 0:
            curr = q.popleft()
            if curr.name == target:
                return curr

            for nei in curr.neighbors:
                if nei not in v:
                    nei.parent = curr
                    q.append(nei)
                    v.add(nei)
    
    def listPath(self, node):
        result = []
        while node:
            result.append(node.name)
            node = node.parent
        return result


if __name__ == "__main__":
    data = {'Apollo 13': ['Kevin Bacon', 'Tom Hanks', 'Gary Sinise'],
            'Hollow Man': ['Elizabeth Sue', 'Kevin Bacon', 'Josh Brolin'],
            'A Few Good Men': ['Tom Cruise', 'Demi Moore', 'Jack Nicholson', 'Kevin Bacon'],
            'One Crazy Summer': ['John Cusack', 'Demi Moore'],
            'Davinci Code': ['Tom Hanks', 'Ian Mckellen', 'Audrey Tautou']
            }
    graph = SixDegrees().buildGraph(data)
    found = SixDegrees().traverse('John Cusack', graph)
    if found:
        print(SixDegrees().listPath(found))