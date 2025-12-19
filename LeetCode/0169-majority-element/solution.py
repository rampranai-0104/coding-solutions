class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        can=nums[0]
        c=1
        for i in range(len(nums)):
            if nums[i]==can:
                c+=1
            else:
                c-=1
            if c==0:
                can=nums[i]
                c=1
        return can
        
