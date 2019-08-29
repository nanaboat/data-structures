from maxbinarytree import Solution2, TreeNode
'''
We are given the root node of a maximum tree: a tree where every node has a value greater than any other value in its subtree.

Just as in the previous problem, the given tree was constructed from an list A (root = Construct(A)) recursively with the following Construct(A) routine:

    If A is empty, return null.
    Otherwise, let A[i] be the largest element of A.  Create a root node with value A[i].
    The left child of root will be Construct([A[0], A[1], ..., A[i-1]])
    The right child of root will be Construct([A[i+1], A[i+2], ..., A[A.length - 1]])
    Return root.

Note that we were not given A directly, only a root node root = Construct(A).

Suppose B is a copy of A with the value val appended to it.  It is guaranteed that B has unique values.

Return Construct(B).

Example 1:

Input: root = [4,1,3,null,null,2], val = 5
Output: [5,4,null,1,3,null,null,2]
Explanation: A = [1,4,2,3], B = [1,4,2,3,5]

Example 2:

Input: root = [5,2,4,null,1], val = 3
Output: [5,2,4,null,1,null,3]
Explanation: A = [2,1,5,4], B = [2,1,5,4,3]

Example 3:

Input: root = [5,2,3,null,1], val = 4
Output: [5,2,4,null,1,3]
Explanation: A = [2,1,5,3], B = [2,1,5,3,4] 

Note:

    1 <= B.length <= 100

'''

class Solution1:
    '''
    Since root is the root node of a cartesian tree, you can do an inorder traversal and get
    the same sequence of the numbers.
    After getting the sequence I append the new val to my sequence and then build
    a new cartesian tree witn my new number sequence and return the root.
    Time complexity: O(n)
    Space complexity: O(2n) --> O(n)
    '''
    def insertIntoMaxTree(self, root, val):
        if root is None:
            return None
        def inorder(node, arr):
            if node:
                inorder(node.left, arr)
                if node.val != None:
                    arr.append(node.val)
                inorder(node.right, arr)
        nums = []
        inorder(root, nums)
        nums.append(val)
        stack = []
        for num in nums:
            node = TreeNode(num)
            while stack and stack[-1].val < num:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]


class Solution_2:
    '''
    Time Complexity: O(n)
    Use the property of the cartesian tree to traverse and insert new val.
    '''
    def insertIntoMaxTree(self, root, val):
        if root is None:
            return None
        if root.val < val:
            node = TreeNode(val)
            node.left = root
            return node
        curr = root
        while curr and curr.val > val:
            prev = curr
            curr = curr.right
        
        if not curr:
            prev.right = TreeNode(val)
        else:
            node = TreeNode(val)
            prev.right = node
            node.left = curr
        return root


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"

if __name__ == '__main__':
    ans1 = Solution1().insertIntoMaxTree(Solution2().buildTree([3,2,1,6,0,5]), 8)
    ans2 = Solution_2().insertIntoMaxTree(Solution2().buildTree([3,2,1,6,0,5]), 4)
    print(treeNodeToString(ans1))
    print(treeNodeToString(ans2))