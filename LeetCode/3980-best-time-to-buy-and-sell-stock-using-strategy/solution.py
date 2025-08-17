class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n=len(prices)
        profit=0
        for i in range(n):
            profit+=(prices[i]*strategy[i])
        pprice=[0]*(n+1)
        pprofit=[0]*(n+1)
        for i in range(n):
            pprice[i+1]=pprice[i]+prices[i]
            pprofit[i+1]=pprofit[i]+ strategy[i]*prices[i]
        maxgain=0
        for start in range(n-k+1):
            end=start+k-1
            mid=start+k//2
            oldp=pprofit[end+1]-pprofit[start]
            newp=pprice[end+1]-pprice[mid]
            gain=newp-oldp
            maxgain=max(gain,maxgain)
        return profit+maxgain
            
            
