class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        profit = 0

        for i in range(len(prices)):
            min_buy = min(prices[L: i + 1])
            curr_profit = prices[i] - min_buy
            profit = max(curr_profit, profit)

            if curr_profit < 0:
                L = i
        
        return profit
