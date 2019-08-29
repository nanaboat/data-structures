'''
finding the distance between two nodes in a binary search tree.
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def __repr__(self):
        return str(self.val)


def distBetweenNodes(alist, n, n1, n2):
    if n < 1:
        return -1
    root = buildTree(alist, n)
    lca = LCA(root, n1, n2)
    d1 = levelofNode(lca, n1)
    d2 = levelofNode(lca, n2)
    if d1 == -1 or d2 == -1:
        return -1
    return d1 + d2

def buildTree(alist, n):
    root = Node(alist[0])
    for i in range(1, n):
        build(root, alist, i)
    return root

def build(node, arr, i):
    if node.val > arr[i]:
        if node.left:
            build(node.left, arr, i)
        else:
            node.left = Node(arr[i])
    else:
        if node.right:
            build(node.right, arr, i)
        else:
            node.right = Node(arr[i])

def findLCA(node, n1, n2):
    if node.val > max(n1, n2):
        return findLCA(node.left, n1,n2)
    elif node.val < min(n1, n2):
        return findLCA(node.right, n1, n2)
    else:
        return node

def levelofNode(node, val):
    return depth(node, val, 0)

def depth(node, val, level):
    if node is None:
        return -1
    if node.val == val:
        return level
    if node.val > val:
        return depth(node.left, val, level + 1)
    else:
        return depth(node.right, val, level + 1)

def LCA(node, n1, n2):
    while node:
        if node.val > max(n1, n2):
            node = node.left
        elif node.val < min(n1, n2):
            node = node.right
        else:
            break
    if findNode(node, n1) and findNode(node, n2):
        return node
    return -1

def findNode(node, val):
    while node:
        if node.val > val:
            node = node.left
        elif node.val < val:
            node = node.right
        else:
            return True
    return False
            

if __name__ == "__main__":
    nums = [5, 6, 3, 1, 2, 4]
    print(distBetweenNodes(nums, 6, 2, 4))
    node = buildTree(nums, 6)
    print(LCA(node, 6, 4))
        
