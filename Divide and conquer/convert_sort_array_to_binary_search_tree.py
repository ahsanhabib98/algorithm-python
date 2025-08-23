# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def arrToBST(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            node = TreeNode(nums[m])
            node.left = arrToBST(l, m - 1)
            node.right = arrToBST(m + 1, r)
            return node
        return arrToBST(0, len(nums) - 1)
        