# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        reverseValue = 0
        ans = []
        tempAns = []
        dq = deque([root, None])
        while dq:
            tempRoot = dq.popleft()
            if tempRoot is None:
                if tempAns:
                    if reverseValue % 2:
                        tempAns = tempAns[::-1]
                    ans.append(tempAns[:])
                    reverseValue += 1
                    tempAns.clear()
                    if dq:
                        dq.append(None)
            else:
                tempAns.append(tempRoot.val)
                if tempRoot.left:
                    dq.append(tempRoot.left)
                if tempRoot.right:
                    dq.append(tempRoot.right)
        return ans
