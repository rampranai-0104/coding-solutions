from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        def inc(start, end):
            for i in range(start, end):
                if nums[i] >= nums[i+1]:
                    return False
            return True

        def dec(start, end):
            for i in range(start, end):
                if nums[i] <= nums[i+1]:
                    return False
            return True

        for p in range(1, n - 2):
            for q in range(p + 1, n - 1):
                if inc(0, p) and dec(p, q) and inc(q, n - 1):
                    return True
        return False

