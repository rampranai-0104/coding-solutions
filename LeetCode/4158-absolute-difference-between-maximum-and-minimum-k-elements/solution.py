class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ss=sum(nums[:k])
        ls=sum(nums[-k:])
        return abs(ls-ss)
