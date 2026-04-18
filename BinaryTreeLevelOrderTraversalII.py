# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        dq = deque([root, None])
        tempAns = []
        while dq:
            temp = dq.popleft()
            if temp is None:
                if tempAns:
                    ans.append(tempAns[:])
                    tempAns.clear()
                    if dq:
                        dq.append(None)
            else:
                tempAns.append(temp.val)
                if temp.left:
                    dq.append(temp.left)
                if temp.right:
                    dq.append(temp.right)

        return ans[::-1]