class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Approach 1: dp
        res = [0] * len(prices)
        for i in range(1, len(prices)):
            res[i] = max(0, res[i-1] + prices[i] - prices[i-1])
        return max(res)

        # Approach 2: one pass
        maxProfit = 0
        minPrice = float('inf')
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice

        return maxProfit
