class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        profit=0
        d=0
        for i in range(0,n-1):
            if prices[i+1]>prices[i]:
                d=prices[i+1]-prices[i]
                profit+=d
        return profit
