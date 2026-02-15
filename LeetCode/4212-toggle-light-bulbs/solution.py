class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        state=[False] * 101
        for b in bulbs:
            state[b]=not state[b]
        res=[i for i in range(1,101) if state[i]]
        return res
