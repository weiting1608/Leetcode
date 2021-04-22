# This problem is widely used for machine translation and speech recognition. 
# Classical dp problem
# time complexity: O(mn), nested loop.
# space complexity: O(mn), for the dp matrix.
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        
        if n*m == 0: return n+m
        
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = i
            
        for j in range(m+1):
            dp[0][j] = j
            
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # dp[i-1][j] for delete, dp[i][j-1] for insert
                    # dp[i-1][j-1] for replace
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    
        return dp[n][m]
                    
                    
        
        
        