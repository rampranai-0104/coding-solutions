class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        while n>0:
            r=n%2
            if r==1:
                c+=1
            n=n//2
        return c
