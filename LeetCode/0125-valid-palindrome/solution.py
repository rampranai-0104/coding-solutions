class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        n=len(s)
        left=0
        right=n-1
        while right>left:
            if s[left].isalnum() and s[right].isalnum():
                if s[left]==s[right]:
                    left+=1
                    right-=1
                else:
                    return False
            elif not s[left].isalnum():
                left+=1
            elif not s[right].isalnum():
                right-=1
        return True
           
