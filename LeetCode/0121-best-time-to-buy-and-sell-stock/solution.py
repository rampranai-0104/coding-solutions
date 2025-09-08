class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        minprice=float('inf')
        maxprofit=0
        for p in prices:
            if p<minprice:
                minprice=p
            if p>=minprice:
                profit=p-minprice
            if profit>maxprofit:
                maxprofit=profit
        return maxprofit
        


