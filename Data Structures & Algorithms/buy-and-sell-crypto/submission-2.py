class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = max(prices[j] - prices[i], profit)
        
        # time complexity O(n ^ 2)
        # space complexity O(n)
        # need to reduce this to O(n) time complexity
        
        return profit