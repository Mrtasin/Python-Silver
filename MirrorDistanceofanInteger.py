class Solution:
    def mirrorDistance(self, n: int) -> int:
        temp = n
        rev = 0
        while n:
            rev = (rev * 10) + (n % 10)
            n //= 10
        return abs(temp - rev)
