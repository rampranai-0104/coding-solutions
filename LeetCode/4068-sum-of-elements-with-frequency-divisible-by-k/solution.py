from collections import Counter 
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        freq=Counter(nums)
        ts=0
        for n,c in freq.items():
            if c%k==0:
                ts+=n*c
        return ts
