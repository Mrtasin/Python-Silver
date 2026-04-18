# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def halperFunction(left, right):
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False

            if (
                (left.val == right.val)
                and halperFunction(left.left, right.right)
                and halperFunction(left.right, right.left)
            ):
                return True
            return False

        return halperFunction(root.left, root.right)
