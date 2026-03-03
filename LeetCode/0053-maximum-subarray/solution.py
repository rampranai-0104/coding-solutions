class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums=0
        n=len(nums)
        maxs=nums[0]
        for i in range(0,n):
            sums=max(nums[i],sums+nums[i])
            maxs=max(maxs,sums)
        return maxs
