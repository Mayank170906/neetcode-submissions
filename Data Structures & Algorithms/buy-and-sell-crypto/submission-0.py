class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n<=1:
            return 0
        profit=0
        for i in range(n):
            lmin=min(prices[0:i+1])
            rmax=max(prices[i:n])
            if rmax-lmin>profit:
                profit=rmax-lmin
        return profit