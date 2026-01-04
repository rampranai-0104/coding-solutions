class Solution:
    def largestEven(self, s: str) -> str:
        lti=s.rfind('2')
        if lti==-1:
            return ""
        return s[:lti+1]
