class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        i=0
        j=n-1
        mw=0
        while i<j:
            area=min(height[i],height[j])*(j-i)
            if area>mw:
                mw=area
            if height[i]<height[j]:
                i+=1
            elif height[i]>=height[j]:
                j-=1
        return mw
