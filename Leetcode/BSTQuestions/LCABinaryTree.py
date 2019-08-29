'''
find the lowest common ancestor of a binary tree
'''

def LowestCommonAncestorInBinaryTree(root, node1, node2):
    '''
    space: O(h)
    time: O(n)
    '''
    if root is None:
        return None
    if root == node1 or root == node2:
        return root
    
    left = LowestCommonAncestorInBinaryTree(root.left, node1, node2)
    right = LowestCommonAncestorInBinaryTree(root.right, node1, node2)

    if left and right:
        return root
    if left:
        return left
    return right