class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def findMid(start, end, nums):
            if start <= end:
                mid = (start + end) // 2
                root = TreeNode(nums[mid])
                root.left = findMid(start, mid - 1, nums)
                root.right = findMid(mid + 1, end, nums)
                
                return root
        import pdb; pdb.set_trace()
        return findMid(0, len(nums) - 1, nums)

if __name__ == "__main__":
    print()