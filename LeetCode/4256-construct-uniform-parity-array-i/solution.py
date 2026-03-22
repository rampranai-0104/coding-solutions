class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd=sum(x%2 for x in nums1)
        even=len(nums1)-odd
        return True
