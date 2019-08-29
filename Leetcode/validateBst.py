# Validate if a binary tree is a BST

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def iterativeInorder(node):
    if node is None:
        return
    
    stack = []
    while node is not None or len(stack) > 0:
        if node is not None:
            stack.append(node)
            node = node.left
        else:
            cur = stack.pop()
            print(cur.val)
            node = cur.right

def validBst(root):
    # modify iterative inorder traversal
    if root is None:
        return True
    
    stack = []
    prev = - 2 ** 31
    while root is not None or len(stack) > 0:
        if root is not None:
            stack.append(root)
            root = root.left
        else:
            cur = stack.pop()
            if prev > cur.val:
                return False
            prev = cur.val
            root = cur.right
    return True

def isBst(root):
    min_val = [-2 ** 32]
    return isBstUtil(root, min_val)

    
def isBstUtil(node, min_val):
    if node is None:
        return True
    if not isBstUtil(node.left, min_val): return False
    
    if min_val[0] > node.val: return False
    
    min_val[0] = node.val

    if not isBstUtil(node.right, min_val): return False
    
    return True


def checkBst(root):
    min_val = - 2 ** 32
    max_val = 2 ** 32
    return checkBstUtil(root, min_val, max_val)


def checkBstUtil(node, min_val, max_val):
    if node is None:
        return True
    
    if node.val <= min_val or node.val > max_val:
        return False
    
    if not checkBstUtil(node.left, min_val, node.val):
        return False
    
    if not checkBstUtil(node.right, node.val, max_val):
        return False
    
    return True


def printTree(root):
    if root:
        printTree(root.left)
        print(root.val, sep=',', end=' ')
        printTree(root.right)

if __name__ == '__main__':
    root = TreeNode(20)
    root.left = TreeNode(10)
    root.left.right = TreeNode(25)
    root.right = TreeNode(30)
    printTree(root)
    print(checkBst(root))