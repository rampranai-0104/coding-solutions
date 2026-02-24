class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        left=0
        wsum=0
        mfreq=0
        for right in range(0,n):
            wsum+=nums[right]
            cost=nums[right]*(right-left+1)-wsum
            while cost>k:
                wsum-=nums[left]
                left+=1
                cost=nums[right]*(right-left+1)-wsum
            mfreq=max(mfreq,right-left+1)
        return mfreq
