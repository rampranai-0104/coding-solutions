class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        fs=0
        ss=0
        af=True
        for i,p in enumerate(nums):
            if p%2==1:
                af=not af
            if (i+1)%6==0:
                af=not af
            if af:
                fs+=p
            else:
                ss+=p
        return fs-ss
