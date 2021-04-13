class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # amount+1 is considered the quite large value, meaning that no result is found.
        dp = [(amount+1) for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i-coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i-coin]+1)

        return dp[amount] if dp[amount] != amount+1 else -1
