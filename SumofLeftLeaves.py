# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def helperFunction(root):
            if root is None:
                return 
            if root.left and root.left.left is None and root.left.right is None:
                self.ans += root.left.val
            helperFunction(root.left)
            helperFunction(root.right)

        helperFunction(root)
        return self.ans