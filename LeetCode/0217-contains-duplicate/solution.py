class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        res=False
        seen=set()
        for i in range(0,n):
            if nums[i] in seen:
                res=True
            else:
                seen.add(nums[i])
        return res
