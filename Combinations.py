class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        temp = []
        def helperFunction(start, end, k):
            if k <= 0:
                result.append(temp[:])
                return
            if start > end:
                return
            temp.append(start)
            helperFunction(start + 1, end, k-1)
            temp.pop()
            helperFunction(start + 1, end, k)
        
        helperFunction(1,n,k)
        return result
        