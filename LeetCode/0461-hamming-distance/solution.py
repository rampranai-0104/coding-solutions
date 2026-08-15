class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z=x^y
        c=0
        while z>0:
            r=z%2
            if r==1:
                c+=1
            z=z//2
        return c
