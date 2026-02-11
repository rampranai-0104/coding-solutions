class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        msum=0
        far=0
        ce=0
        for i in range(0,n-1):
            far=max(far,i+nums[i])
            if i==ce:
                msum+=1
                ce=far
        return msum


