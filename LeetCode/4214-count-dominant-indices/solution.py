class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        for i in range(n-1):
            rs=sum(nums[i+1:])
            rc=n-i-1
            if nums[i]>rs/rc:
                c+=1
        return c
