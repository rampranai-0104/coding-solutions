class Solution(object):
    def maximumMedianSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        return sum(nums[n//3 + i*2] for i in range(n // 3))

