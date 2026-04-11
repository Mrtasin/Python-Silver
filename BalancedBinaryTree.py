# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def isBalancedOrNot(root):
            if root == None:
                return 0
            leftHt = isBalancedOrNot(root.left)
            if leftHt == -1:
                return -1
            rightHt = isBalancedOrNot(root.right)
            if rightHt == -1:
                return -1
            if abs(leftHt - rightHt) > 1:
                return -1

            return max(leftHt, rightHt) + 1

        return isBalancedOrNot(root) != -1
