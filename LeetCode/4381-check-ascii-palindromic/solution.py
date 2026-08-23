class Solution:
    def isPalindromic(self, s: str) -> bool:
        b=""
        for i in s:
            n=ord(i)
            for i in range(7,-1,-1):
                if n & (1<<i):
                    b+="1"
                else:
                    b+="0"
        return b==b[::-1]
