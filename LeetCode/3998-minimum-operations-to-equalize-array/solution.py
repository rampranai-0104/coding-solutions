from typing import List 
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if all(x==nums[0] for x in nums):
            return 0
        return 1
