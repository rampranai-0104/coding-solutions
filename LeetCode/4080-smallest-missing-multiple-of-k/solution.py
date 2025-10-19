class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        ns=set(nums)
        mul=k
        while True:
            if mul not in ns:
                return mul
            mul+=k
