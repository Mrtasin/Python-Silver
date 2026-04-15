# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(root, low, high):
            if root is None:
                return True

            if not (low < root.val < high):
                return False

            ansLeft = helper(root.left, low, root.val)
            ansRight = helper(root.right, root.val, high)

            return ansLeft and ansRight

        return helper(root, float("-inf"), float("inf"))