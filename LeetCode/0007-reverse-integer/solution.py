class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        n=0
        if x<0:
            sign=-1
            x=-x
        else:
            sign=1
        while x>0:
            n=x%10
            rev=(rev*10)+n
            x=x//10
        res=sign*rev
        if res < -2**31 or res > 2**31 - 1:
            return 0
        else:
            return res
