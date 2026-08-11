class Solution:
    def validPalindrome(self, s: str) -> bool:
        n=len(s)
        def isp(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        l=0
        r=n-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return isp(l+1,r) or isp(l,r-1)
        return True
