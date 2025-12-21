class Solution:
    def mirrorDistance(self, n: int) -> int:
        rn=int(str(n)[::-1])
        return abs(n-rn)
