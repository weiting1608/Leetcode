class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Approach 1: dp 
        res = [0] * len(prices)
        for i in range(1, len(prices)):
            res[i] = max(0, res[i-1] + prices[i] - prices[i-1])
        return max(res)

        # Approach 2
        res = [0] * len(prices)
        for i in range(1, len(prices)):
            res[i] = max(0, res[i-1] + prices[i] - prices[i-1])
        return max(res)
        
        
