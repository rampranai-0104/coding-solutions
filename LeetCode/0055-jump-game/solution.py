class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        msum=0
        for i in range(0,n):
            if i >msum:
                return False
            else:
                msum=max(msum,i+nums[i])
            if msum>=n-1:
                return True
