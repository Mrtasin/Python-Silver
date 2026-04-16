# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def halperFunction(root, path, tar):
            if root is None :
                return 
            path.append(root.val)

            if root.left is None and root.right is None:
                if sum(path) == tar:
                    ans.append(path[:])

            halperFunction(root.left, path, tar)
            halperFunction(root.right, path, tar)
            path.pop()

        halperFunction(root, [], targetSum)
        return ans