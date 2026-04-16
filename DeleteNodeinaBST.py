# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def deleteItem(root, data):
            if root is None:
                return None

            if root.val > data:
                root.left = deleteItem(root.left, data)

            elif root.val < data:
                root.right = deleteItem(root.right, data)

            else:
                if root.left is None and root.right is None:
                    return None
                elif root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left

                else:
                    curr = root.left
                    while curr.right:
                        curr = curr.right

                    root.val = curr.val
                    root.left = deleteItem(root.left, curr.val)
            return root

        return deleteItem(root, key)
