class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n=len(nums)
        sm=[0]*n
        sm[-1]=nums[-1]
        for i in range(n-2,-1,-1):
            sm[i]=min(nums[i],sm[i+1])
        ps=0
        ms=-10**30
        for i in range(n-1):
            ps+=nums[i]
            s=ps-sm[i+1]
            ms=max(ms,s)
        return ms
