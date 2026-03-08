class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        mc=float('inf')
        ri=-1
        for i in range(len(capacity)):
            if capacity[i]>=itemSize and capacity[i]<mc:
                mc=capacity[i]
                ri=i
        return ri
