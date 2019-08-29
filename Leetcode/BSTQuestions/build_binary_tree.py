# Given inorder and postorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]

# Return the following binary tree:

#    3
#   / \
#  9  20
#    /  \
#   15   7

# Solution:
# Note that for postorder traversal of a tree the right-most element/value
# in the array/list is the parent/root of the sub-tree/tree

# Note that for preorder traversal of a tree the left-most element/value
# in the array/list is the parent/root of the sub-tree/tree

# Note also that from the either the postorder or prorder the parent's
# corresponding index/place in the order traversal shows which elements/value
# belong to either the left/right subtree.


class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def buildtree1(inorder, postorder):
    '''This is an inefficient solution.
       Time complexity of O(n^2)
       Space complexity of O(n)
    '''
    if len(inorder) == 0:
        return
    p_val = postorder.pop()
    p_idx = inorder.index(p_val)

    t_node = Tree(p_val)

    t_node.left = buildtree1(inorder[:p_idx], postorder[:p_idx])
    t_node.right = buildtree1(inorder[p_idx + 1:], postorder[p_idx:])

    return t_node


def buildtree2(inorder, postorder):
    '''This is an efficient solution.
       Time complexity is O(n). This is achieved by using a map so searching
       for index is O(1). Also you pass the pointers to the function instead
       of slicing which is an expensive operation.
       Space complexity is O(n)
    '''
    n = len(inorder)
    in_map = _buildmap(inorder)
    return _build_util(in_map, postorder, 0, n-1)


def _build_util(inorder, postorder, in_start, in_end):
    if in_start > in_end:
        return
    
    p_val = postorder.pop()
    t_node = Tree(p_val)

    # if node has no children is a leaf node.
    if in_start == in_end:
        return t_node
    
    idx = inorder[p_val]

    t_node.right = _build_util(inorder, postorder, idx + 1, in_end)
    t_node.left = _build_util(inorder, postorder, in_start, idx - 1)
    

    return t_node

def _buildmap(inorder):
    mp = {}
    for i, val in enumerate(inorder):
        mp[val] = i
    return mp

if __name__ == "__main__":
    import pdb; pdb.set_trace()
    node = buildtree2([9,3,15,20,7], [9,15,7,20,3])
    
