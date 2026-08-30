class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        bl=[0]*101
        n=len(nums)
        for i in range(n):
            if i==0 or nums[i]!=nums[i-1]:
                bl[nums[i]]+=1
        c=0
        for x in range(1,101):
            if bl[x]==1:
                c+=1
        return c
