class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        s=0
        maxe=nums[0]
        for i in range(n):
            s=max(nums[i],s+nums[i])
            maxe=max(maxe,s)
        return maxe
