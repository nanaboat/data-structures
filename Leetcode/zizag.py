'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]
'''

from collections import deque

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def zigzag(root):
    result = []
    if root is None:
        return result
    q = deque()
    q.append(root)
    while q:
        temp = []
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            temp.append(node.val)
        result.append(temp)
    for i, arr in enumerate(result):
        if i%2 != 0:
            temp = []
            while arr:
                temp.append(arr.pop())
            result[i] = temp

    return result

def zigzag1(root):
    result = []
    if root is None:
        return result
    q = deque()
    q.append(root)
    level = 0
    #import pdb; pdb.set_trace()
    while q:
        temp = deque()
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if level % 2 != 0:
                temp.appendleft(node.val)
            #if level % 2 == 0:
            else:
                temp.append(node.val)
        result.append(list(temp))
        level += 1

    return result

def arrayToTreeNode(inputValues):
    if not input:
        return None

    root = TreeNode(inputValues[0])
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = item
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = item
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def printTreeNode(root):
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        print(node.val, end=',')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

if __name__ == '__main__':
    node = arrayToTreeNode([3,9,20,14,'null',15,7,10,9, 40, 23, 56, 54])
    #printTreeNode(node)
    print(zigzag1(node))
