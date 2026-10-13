class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n<=1:
            return 0
        lmin=prices[0]
        profit=0
        for i in range(1,n):
            profit=max(profit,prices[i]-lmin)
            lmin=min(lmin,prices[i])
        return profit