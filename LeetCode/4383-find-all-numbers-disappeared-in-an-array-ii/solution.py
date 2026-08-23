class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        n=len(nums)
        nums.sort()
        next=lower
        r=[]
        for x in nums:
            if x<next:
                continue
            if x>upper:
                break
            if x>next:
                r.append([next,x-1])
            next=x+1
        if next<=upper:
            r.append([next,upper])
        return r
