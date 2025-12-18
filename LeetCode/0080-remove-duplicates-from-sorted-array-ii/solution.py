class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=2
        for j in range(2,len(nums)):
            if nums[j]==nums[k-2]:
                #j=0
                pass
            else:
                nums[k]=nums[j]
                k+=1
        return k
