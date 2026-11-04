class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0 # buy day
        profit = 0

        #  R is sell day
        for R in range(len(prices)):
            if prices[L] < prices[R]:
                profit = max(prices[R] - prices[L], profit)
            else:
                L = R
            
        return profit